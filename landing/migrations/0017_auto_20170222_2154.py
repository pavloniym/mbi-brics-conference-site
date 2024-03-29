# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 18:54
from __future__ import unicode_literals

from django.db import migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0016_baseinfo_submission_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseinfo',
            name='practical_main_text',
            field=django_markdown.models.MarkdownField(default='', verbose_name='Practical Info Main Text'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='visa_main_text',
            field=django_markdown.models.MarkdownField(default='', verbose_name='Visa Main Text'),
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='works_invitation',
            field=django_markdown.models.MarkdownField(default='', verbose_name='Works invitation text'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=django_markdown.models.MarkdownField(),
        ),
        migrations.AlterField(
            model_name='practical',
            name='description',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='practicalblock',
            name='text',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
