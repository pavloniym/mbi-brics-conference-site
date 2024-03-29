# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 18:38
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0014_auto_20170219_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='submission_details',
            field=django_markdown.models.MarkdownField(default='', verbose_name='Submission details text'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='submission_help',
            field=django_markdown.models.MarkdownField(default='', verbose_name='Submission help text'),
        ),
    ]
