# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 21:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0020_fees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='title',
            field=models.CharField(choices=[('', ''), ('Prof', 'Prof'), ('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], help_text='Select an item\u2026', max_length=255),
        ),
    ]
