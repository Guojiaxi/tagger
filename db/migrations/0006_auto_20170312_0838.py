# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0005_auto_20170226_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(default=2048),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(default=2448),
            preserve_default=False,
        ),
    ]