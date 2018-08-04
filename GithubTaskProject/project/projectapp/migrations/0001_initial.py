# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-27 05:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default=b'', max_length=100)),
                ('mail', models.CharField(blank=True, default=b'', max_length=100)),
                ('contact', models.CharField(blank=True, default=b'', max_length=100)),
                ('address', models.CharField(blank=True, default=b'', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]