# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 20:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_auto_20170217_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='anchor',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]