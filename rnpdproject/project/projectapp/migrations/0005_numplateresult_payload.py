# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-17 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0004_uploadmedia_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='numplateresult',
            name='payload',
            field=models.CharField(blank=True, default=b'', max_length=10),
        ),
    ]
