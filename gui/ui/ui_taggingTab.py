# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_taggingTab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TaggingTab(object):
    def setupUi(self, TaggingTab):
        TaggingTab.setObjectName("TaggingTab")
        TaggingTab.resize(1498, 856)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TaggingTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_taggingControls = QtWidgets.QVBoxLayout()
        self.layout_taggingControls.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_taggingControls.setSpacing(6)
        self.layout_taggingControls.setObjectName("layout_taggingControls")
        self.groupBox_2 = QtWidgets.QGroupBox(TaggingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_tags = QtWidgets.QTableWidget(self.groupBox_2)
        self.list_tags.setMaximumSize(QtCore.QSize(16777215, 150))
        self.list_tags.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_tags.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.list_tags.setObjectName("list_tags")
        self.list_tags.setColumnCount(4)
        self.list_tags.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.list_tags)
        self.layout_tagsButtons = QtWidgets.QHBoxLayout()
        self.layout_tagsButtons.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.layout_tagsButtons.setObjectName("layout_tagsButtons")
        self.button_addTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_addTag.setObjectName("button_addTag")
        self.layout_tagsButtons.addWidget(self.button_addTag)
        self.button_editTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_editTag.setObjectName("button_editTag")
        self.layout_tagsButtons.addWidget(self.button_editTag)
        self.button_removeTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_removeTag.setObjectName("button_removeTag")
        self.layout_tagsButtons.addWidget(self.button_removeTag)
        self.verticalLayout_2.addLayout(self.layout_tagsButtons)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.layout_taggingControls.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(TaggingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_reviewed = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_reviewed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_reviewed.setObjectName("radioButton_reviewed")
        self.image_status_buttons = QtWidgets.QButtonGroup(TaggingTab)
        self.image_status_buttons.setObjectName("image_status_buttons")
        self.image_status_buttons.addButton(self.radioButton_reviewed)
        self.horizontalLayout_3.addWidget(self.radioButton_reviewed)
        self.radioButton_notReviewed = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_notReviewed.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_notReviewed.setObjectName("radioButton_notReviewed")
        self.image_status_buttons.addButton(self.radioButton_notReviewed)
        self.horizontalLayout_3.addWidget(self.radioButton_notReviewed)
        self.radioButton_allImages = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_allImages.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_allImages.setObjectName("radioButton_allImages")
        self.image_status_buttons.addButton(self.radioButton_allImages)
        self.horizontalLayout_3.addWidget(self.radioButton_allImages)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.images_list = QtWidgets.QListWidget(self.groupBox_3)
        self.images_list.setObjectName("images_list")
        self.verticalLayout_3.addWidget(self.images_list)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_addImage = QtWidgets.QPushButton(self.groupBox_3)
        self.button_addImage.setObjectName("button_addImage")
        self.gridLayout_2.addWidget(self.button_addImage, 2, 1, 1, 1)
        self.button_toggleView = QtWidgets.QPushButton(self.groupBox_3)
        self.button_toggleView.setObjectName("button_toggleView")
        self.gridLayout_2.addWidget(self.button_toggleView, 2, 0, 1, 1)
        self.button_previous = QtWidgets.QPushButton(self.groupBox_3)
        self.button_previous.setObjectName("button_previous")
        self.gridLayout_2.addWidget(self.button_previous, 1, 0, 1, 1)
        self.button_fitScreen = QtWidgets.QPushButton(self.groupBox_3)
        self.button_fitScreen.setObjectName("button_fitScreen")
        self.gridLayout_2.addWidget(self.button_fitScreen, 2, 2, 1, 1)
        self.button_next = QtWidgets.QPushButton(self.groupBox_3)
        self.button_next.setObjectName("button_next")
        self.gridLayout_2.addWidget(self.button_next, 1, 2, 1, 1)
        self.button_toggleReviewed = QtWidgets.QPushButton(self.groupBox_3)
        self.button_toggleReviewed.setObjectName("button_toggleReviewed")
        self.gridLayout_2.addWidget(self.button_toggleReviewed, 0, 0, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.minimap = MiniMap(self.groupBox_3)
        self.minimap.setMinimumSize(QtCore.QSize(300, 190))
        self.minimap.setMaximumSize(QtCore.QSize(500, 400))
        self.minimap.setObjectName("minimap")
        self.verticalLayout_3.addWidget(self.minimap)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 6)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 2)
        self.layout_taggingControls.addWidget(self.groupBox_3)
        self.layout_taggingControls.setStretch(0, 1)
        self.layout_taggingControls.setStretch(1, 2)
        self.horizontalLayout.addLayout(self.layout_taggingControls)
        self.layout_taggingImage = QtWidgets.QVBoxLayout()
        self.layout_taggingImage.setObjectName("layout_taggingImage")
        self.viewer_single = PhotoViewer(TaggingTab)
        self.viewer_single.setObjectName("viewer_single")
        self.layout_taggingImage.addWidget(self.viewer_single)
        self.horizontalLayout.addLayout(self.layout_taggingImage)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(TaggingTab)
        QtCore.QMetaObject.connectSlotsByName(TaggingTab)

    def retranslateUi(self, TaggingTab):
        _translate = QtCore.QCoreApplication.translate
        TaggingTab.setWindowTitle(_translate("TaggingTab", "Form"))
        self.groupBox_2.setTitle(_translate("TaggingTab", "Tags"))
        item = self.list_tags.horizontalHeaderItem(0)
        item.setText(_translate("TaggingTab", "Type"))
        item = self.list_tags.horizontalHeaderItem(1)
        item.setText(_translate("TaggingTab", "Subtype"))
        item = self.list_tags.horizontalHeaderItem(2)
        item.setText(_translate("TaggingTab", "Current (Total)"))
        item = self.list_tags.horizontalHeaderItem(3)
        item.setText(_translate("TaggingTab", "Icon"))
        self.button_addTag.setText(_translate("TaggingTab", "Add"))
        self.button_editTag.setText(_translate("TaggingTab", "Edit"))
        self.button_removeTag.setText(_translate("TaggingTab", "Remove"))
        self.groupBox_3.setTitle(_translate("TaggingTab", "Images"))
        self.radioButton_reviewed.setText(_translate("TaggingTab", "Reviewed"))
        self.radioButton_notReviewed.setText(_translate("TaggingTab", "Not Reviewed"))
        self.radioButton_allImages.setText(_translate("TaggingTab", "All Images"))
        self.button_addImage.setText(_translate("TaggingTab", "Add Image"))
        self.button_toggleView.setText(_translate("TaggingTab", "Toggle View"))
        self.button_previous.setText(_translate("TaggingTab", "Previous"))
        self.button_fitScreen.setText(_translate("TaggingTab", "Fit to Screen"))
        self.button_next.setText(_translate("TaggingTab", "Next"))
        self.button_toggleReviewed.setText(_translate("TaggingTab", "Mark as Reviewed"))

from gui.miniMap import MiniMap
from gui.photoViewer import PhotoViewer
