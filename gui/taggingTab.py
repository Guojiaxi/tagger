from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from ui.ui_taggingTab import Ui_TaggingTab
from tagDialog import TagDialog
from db.dbHelper import *
from observer import *
from utils.imageInfo import createImageWithExif
from gui.imageListItem import ImageListItem
from gui.tagTableItem import TagTableItem
from tagContextMenu import TagContextMenu
from markerItem import MarkerItem


class TaggingTab(QtWidgets.QWidget, Ui_TaggingTab, Observable):
    def __init__(self):
        super(TaggingTab, self).__init__()
        Observable.__init__(self)

        self.currentFlight = None
        self.currentImage = None

        self.setupUi(self)
        self.connectButtons()

    def notify(self, event, id, data):
        for observer in self.observers:
            observer.notify(event, id, data)

        if event is "MARKER_CREATE":
            self.addMarker(data)

        elif event is "MARKER_DELETED":
            self.viewer_single.getScene().removeItem(data)

    def connectButtons(self):
        self.button_addTag.clicked.connect(self.addTag)
        self.button_editTag.clicked.connect(self.editTag)
        self.button_removeTag.clicked.connect(self.removeTag)

        self.list_images.currentItemChanged.connect(self.currentImageChanged)
        self.button_toggleReviewed.clicked.connect(self.toggleImageReviewed)
        self.button_previous.clicked.connect(self.previousImage)
        self.button_next.clicked.connect(self.nextImage)
        self.button_addImage.clicked.connect(self.addImage)

    def addTag(self):
        dialog = TagDialog(title="Create tag")
        if dialog.exec_() == QDialog.Accepted:
            if len(dialog.subtype.text()) > 0:
                tagType = dialog.tagType.text()
                subtype = dialog.subtype.text()
                count = "0"
                icon = dialog.icons.currentText()
                t = create_tag(type=tagType, subtype=subtype, symbol=icon, num_occurrences=int(count))
                self.addTagToUi(t)
                self.notifyObservers("TAG_CREATED", None, t)

    def addTagToUi(self, tag):
        row = self.list_tags.rowCount()
        self.list_tags.insertRow(row)

        # update all columns in row with these texts
        texts = [tag.type, tag.subtype, str(tag.num_occurrences), tag.symbol]
        [self.list_tags.setItem(row, col, TagTableItem(text, tag)) for col, text in enumerate(texts)]
        self.tag_context_menu.addTagToContextMenu(tag.subtype)

        # add tag to context men
        self.viewer_single.getPhotoItem().context_menu.addTagToContextMenu(tag)

    def addMarker(self, data):
        _event, _tag = data
        # TODO
        # Create db marker object here
        # Pass marker.pk or the marker db object to the addMarkerToUi function. Remove association with tag object.

        self.addMarkerToUi(data)

    def addMarkerToUi(self, data):
        _event, _tag = data

        marker = MarkerItem(parent_tag=_tag, initial_zoom=self.viewer_single.zoomFactor())
        marker.addObserver(self)

        scenePoint = _event.scenePos()
        markerXPos = scenePoint.x() - marker.pixmap().size().width() / 2  # To position w.r.t. center of pixMap
        markerYPos = scenePoint.y() - marker.pixmap().size().height() / 2  # To position w.r.t. center of pixMap
        marker.setPos(markerXPos, markerYPos)

        # The following line makes sure that the scaling happens w.r.t. center of pixMap
        marker.setTransformOriginPoint(marker.pixmap().size().width() / 2, marker.pixmap().size().height() / 2)

        self.viewer_single.getScene().addItem(marker)

    def editTag(self):
        row = self.list_tags.currentRow()
        if row >= 0:
            tag = self.list_tags.item(row, 0).getTag()
            tagType = tag.type
            subtype = tag.subtype
            count = "0"
            icon = tag.symbol
            dialog = TagDialog(title="Edit tag")
            dialog.tagType.setText(tagType)
            dialog.subtype.setText(subtype)
            index = dialog.icons.findText(icon)
            dialog.icons.setCurrentIndex(index)
            if dialog.exec_() == QDialog.Accepted:
                if len(dialog.subtype.text()) > 0:
                    tag.type = dialog.tagType.text()
                    tag.subtype = dialog.subtype.text()
                    tag.num_occurrences = -1
                    tag.symbol = dialog.icons.currentText()

                    # update all columns in row with these texts
                    texts = [tag.type, tag.subtype, str(tag.num_occurrences), tag.symbol]
                    [self.list_tags.setItem(row, col, TagTableItem(text, tag)) for col, text in enumerate(texts)]

                    tag.save()
                    self.notifyObservers("TAG_EDITED", None, tag)
                    self.viewer_single.getPhotoItem().context_menu.updateTagItem(old_subtype, subtype)

    def removeTag(self):
        row = self.list_tags.currentRow()
        tag = self.list_tags.item(row, 0).getTag()
        if row >= 0:
            self.viewer_single.getPhotoItem().context_menu.removeTagItem(self.list_tags.item(row, 1).text())
            self.list_tags.removeRow(row)
            self.notifyObservers("TAG_DELETED", None, tag)

    def toggleImageReviewed(self):
        item = self.list_images.currentItem()
        if item:
            font = item.font()
            font.setBold(not font.bold())
            item.setFont(font)

            # image was marked as reviewed
            if not font.bold():
                self.nextImage()

    def addImage(self):
        paths = QtWidgets.QFileDialog.getOpenFileNames(self, "Select images", ".", "Images (*.jpg)")[0]
        for path in paths:
            image = createImageWithExif(path, self.currentFlight)
            self.addImageToUi(image)

    def addImageToUi(self, image):
        item = ImageListItem(image.filename, image)
        self.list_images.addItem(item)

    def currentImageChanged(self, current, _):
        self.currentImage = current.getImage()
        self.openImage(self.currentImage.filename, self.viewer_single)
        self.notifyObservers("CURRENT_IMG_CHANGED", None, self.currentImage.filename)

    def openImage(self, path, viewer):
        viewer.setPhoto(QtGui.QPixmap(path))
        viewer.getPhotoItem().addObserver(self)

    def previousImage(self):
        self.setImageRow(self.list_images.currentRow() - 1)

    def nextImage(self):
        self.setImageRow(self.list_images.currentRow() + 1)

    def setImageRow(self, row):
        if 0 <= row < self.list_images.count():
            self.list_images.setCurrentRow(row)

    def getSelectedImageSize(self):
        return self.viewer_single.getImageSize()

    def getCurrentImage(self):
        return self.currentImage

    def getCurrentFlight(self):
        return self.currentFlight
