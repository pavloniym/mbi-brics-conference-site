# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import landing.helpers
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_title', models.CharField(max_length=255, verbose_name='Area title')),
            ],
            options={
                'verbose_name_plural': 'Areas',
            },
        ),
        migrations.CreateModel(
            name='BaseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=255, verbose_name='Type')),
                ('event_title', models.CharField(max_length=255, verbose_name='Title')),
                ('event_date', models.CharField(max_length=255, verbose_name='Date')),
                ('event_place', models.CharField(max_length=255, verbose_name='Place')),
                ('language', models.CharField(max_length=255, verbose_name='Working language')),
                ('submission_open', models.BooleanField(default=True, verbose_name='Open submission')),
                ('submission_details', models.TextField(default='', verbose_name='Submission details text')),
                ('submission_help', models.TextField(default='', verbose_name='Submission help text')),
                ('works_invitation', models.TextField(default='', verbose_name='Works invitation text')),
            ],
            options={
                'verbose_name': 'Base information',
                'verbose_name_plural': 'Base information',
            },
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_text', models.TextField(verbose_name='Left Text')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('site', models.URLField(verbose_name='Site')),
                ('address_text', models.CharField(max_length=255, verbose_name='Address Text')),
                ('address_link', models.CharField(max_length=255, verbose_name='Address Link')),
            ],
            options={
                'verbose_name_plural': 'Footer',
            },
        ),
        migrations.CreateModel(
            name='ImportantDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('since', models.CharField(blank=True, max_length=255, verbose_name='Since')),
                ('till', models.CharField(blank=True, max_length=255, verbose_name='Till')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('svg', models.TextField(verbose_name='Icon')),
            ],
            options={
                'verbose_name': 'Important Date',
                'verbose_name_plural': 'Important Dates',
            },
        ),
        migrations.CreateModel(
            name='Organizers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('university', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('photo', models.ImageField(upload_to=landing.helpers.RandomFileName('ogranizers'))),
                ('committie', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('org', 'Organising Committie'), ('prog', 'Programme Committie')], max_length=8)),
            ],
            options={
                'verbose_name': 'Organizers',
                'verbose_name_plural': 'Organizers',
            },
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Speakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('university', models.CharField(max_length=255, verbose_name='University')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.URLField(verbose_name='Link')),
                ('photo', models.ImageField(upload_to=landing.helpers.RandomFileName('speakers'), verbose_name='Photo')),
            ],
            options={
                'verbose_name_plural': 'Speakers',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('', ''), ('prog', 'Prof'), ('dr', 'Dr'), ('mr', 'Mr'), ('mrs', 'Mrs'), ('ms', 'Ms')], help_text='Select an item\u2026', max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255)),
                ('second_name', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('job_position', models.CharField(max_length=255)),
                ('attendance_status', models.CharField(choices=[('', ''), ('reporter', 'Reporter'), ('participant', 'Participant, without a report')], help_text='Select an item\u2026', max_length=255)),
                ('abstract_title', models.CharField(blank=True, max_length=255)),
                ('abstract_text', models.TextField(blank=True, help_text='Not more than 500 words')),
                ('section_1', models.CharField(choices=[('', ''), (b'1', b'Global challenges for innovation in management and business'), (b'2', b'Quantitative methods in management, economy and finance'), (b'3', b'National and regional innovation systems in BRICS and recently emerging economies'), (b'4', b'University-industry links and innovation in BRICS countries'), (b'5', b'Entrepreneurship and its development in BRICS, emerging markets and developed economies'), (b'6', b'Innovation in services, knowledge intensive services and creative industries'), (b'7', b'Modern technologies in logistics and services'), (b'8', b'Open Innovation in both large and small firms: cases of BRICS'), (b'9', b'Social innovation and innovation in social enterprises and other not-for- profit organizations'), (b'10', b'The impact of globalization on management research'), (b'11', b'Digital, IT-enabled and financial innovation: shaping the future'), (b'12', b'Cross Cultural Research - International issues in gender and management')], help_text='Select an item\u2026', max_length=255)),
                ('section_2', models.CharField(blank=True, choices=[('', ''), (b'1', b'Global challenges for innovation in management and business'), (b'2', b'Quantitative methods in management, economy and finance'), (b'3', b'National and regional innovation systems in BRICS and recently emerging economies'), (b'4', b'University-industry links and innovation in BRICS countries'), (b'5', b'Entrepreneurship and its development in BRICS, emerging markets and developed economies'), (b'6', b'Innovation in services, knowledge intensive services and creative industries'), (b'7', b'Modern technologies in logistics and services'), (b'8', b'Open Innovation in both large and small firms: cases of BRICS'), (b'9', b'Social innovation and innovation in social enterprises and other not-for- profit organizations'), (b'10', b'The impact of globalization on management research'), (b'11', b'Digital, IT-enabled and financial innovation: shaping the future'), (b'12', b'Cross Cultural Research - International issues in gender and management')], help_text='Select an item\u2026', max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('telephone', models.CharField(blank=True, max_length=255)),
                ('date_of_birth', models.CharField(help_text='dd/mm/yyyy', max_length=255)),
                ('citizenship', models.CharField(max_length=255)),
                ('visa', models.CharField(choices=[('', ''), ('yes', 'Yes'), ('no', 'No')], help_text='Select an item\u2026', max_length=255, verbose_name='Do you need a visa?')),
                ('passport', models.CharField(blank=True, max_length=255, verbose_name='Passport \u2116')),
                ('issued', models.CharField(blank=True, max_length=255, verbose_name='Issued on')),
                ('valid', models.CharField(blank=True, max_length=255, verbose_name='Valid by')),
                ('city', models.CharField(blank=True, max_length=255)),
                ('postal_address', models.CharField(max_length=255)),
                ('zip', models.CharField(blank=True, max_length=255, verbose_name='ZIP')),
                ('country', models.CharField(max_length=255)),
                ('hotel', models.CharField(choices=[('', ''), ('yes', 'Yes'), ('no', 'No')], help_text='Select an item\u2026', max_length=255, verbose_name='Do you need a hotel?')),
                ('created_at', models.DateField(blank=True, default=datetime.date.today, null=True)),
            ],
            options={
                'verbose_name': 'Submission',
                'verbose_name_plural': 'Submissions',
            },
        ),
        migrations.CreateModel(
            name='TopicAreas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Topic title')),
            ],
            options={
                'verbose_name': 'Topic Area',
                'verbose_name_plural': 'Topic Areas',
            },
        ),
    ]