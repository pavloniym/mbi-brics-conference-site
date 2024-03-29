# coding: utf-8
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django_markdown.models import MarkdownField
from multiselectfield import MultiSelectField

from .helpers import *

ORGANIZERS_CHOICES = (
    ('org', 'Organising Committee'),
    ('prog', 'Programme Committee'),
)


@python_2_unicode_compatible
class Menu(models.Model):
    title = models.CharField(max_length=255)
    section = models.CharField(max_length=255, default='', blank=True)
    anchor = models.CharField(max_length=255, default='', blank=True)
    externalLink = models.BooleanField('External link', default=False, blank=True)
    externalURL = models.URLField('External URL', blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Main Menu'
        verbose_name_plural = 'Main Menu'
        ordering = ('order',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class VisaSteps(models.Model):
    step_num = models.IntegerField('Step number')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Visa Step'
        verbose_name_plural = 'Visa Steps'
        ordering = ('order',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class VisaStepsBlock(models.Model):
    title = models.CharField(max_length=255, blank=True)
    text = MarkdownField(blank=True)
    important = MarkdownField(blank=True)
    visa_step = models.ForeignKey(VisaSteps, on_delete=models.CASCADE, related_name='visa_step_block')

    class Meta:
        verbose_name = 'Visa Step Block'
        verbose_name_plural = 'Visa Step Block'
        ordering = ('pk',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class BaseInfo(models.Model):
    event_type = models.CharField('Type', max_length=255)
    event_title = models.CharField('Title', max_length=255)
    event_date = models.CharField('Date', max_length=255)
    event_place = models.CharField('Place', max_length=255)
    background_image = models.ImageField('Photo', upload_to=RandomFileName('main'), default='')
    language = models.CharField('Working language', max_length=255)
    submission_open = models.BooleanField('Open submission', default=True, blank=True)
    submission_start = MarkdownField('Submission above button text', default='')
    submission_details = MarkdownField('Submission details text', default='')
    submission_help = MarkdownField('Submission help text', default='')
    works_invitation = MarkdownField('Works invitation text', default='')
    visa_header = models.CharField('Visa Header', max_length=255, default='Visa Requirements')
    visa_main_text = MarkdownField('Visa Main Text', default='')
    visa_find_nearest_link = models.URLField(blank=True)
    no_visa_requirement_link = models.URLField(blank=True)
    practical_header = models.CharField('Practical Info Header', max_length=255, default='BRICS Practical Information')
    practical_main_text = MarkdownField('Practical Info Main Text', default='')
    fees_header = models.CharField(max_length=255, default='', blank=False)
    fees_text = MarkdownField(default='', blank=True)

    class Meta:
        verbose_name = 'Base information'
        verbose_name_plural = 'Base information'

    def __str__(self):
        return self.event_type + " - " + self.event_title


@python_2_unicode_compatible
class Areas(models.Model):
    area_title = models.CharField('Area title', max_length=255)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Areas'
        ordering = ('order',)

    def __str__(self):
        return self.area_title


@python_2_unicode_compatible
class Speakers(models.Model):
    name = models.CharField('Name', max_length=255)
    university = models.CharField('University', max_length=255)
    description = models.TextField('Description')
    url = models.URLField('Link')
    photo = models.ImageField('Photo', upload_to=RandomFileName('speakers'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name_plural = 'Speakers'
        ordering = ('order',)

    def __str__(self):
        return self.name + " - " + self.university


@python_2_unicode_compatible
class Publications(models.Model):
    title = models.CharField('Title', max_length=255)
    description = MarkdownField('Description')

    class Meta:
        verbose_name_plural = 'Publications'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TopicAreas(models.Model):
    title = models.CharField('Topic title', max_length=255)

    class Meta:
        verbose_name = 'Topic Area'
        verbose_name_plural = 'Topic Areas'
        ordering = ('pk',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ImportantDates(models.Model):
    title = models.CharField('Title', max_length=255)
    since = models.CharField('Since', max_length=255, blank=True)
    till = models.CharField('Till', max_length=255, blank=True)
    description = models.TextField('Description', blank=True)
    svg = models.TextField('Icon')

    class Meta:
        verbose_name = 'Important Date'
        verbose_name_plural = 'Important Dates'
        ordering = ('pk',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Footer(models.Model):
    left_text = models.TextField('Left Text')
    phone = models.CharField('Phone', max_length=255)
    email = models.CharField('Email', max_length=255)
    site = models.URLField('Site')
    address_text = models.CharField('Address Text', max_length=255)
    address_link = models.CharField('Address Link', max_length=255)

    class Meta:
        verbose_name_plural = 'Footer'

    def __str__(self):
        return 'Footer'


@python_2_unicode_compatible
class Organizers(models.Model):
    name = models.CharField('Name', max_length=255)
    university = models.CharField(max_length=255)
    url = models.URLField()
    photo = models.ImageField(upload_to=RandomFileName('ogranizers'))
    committee = MultiSelectField(choices=ORGANIZERS_CHOICES, blank=True)

    class Meta:
        verbose_name_plural = 'Organizers'
        verbose_name = 'Organizers'
        ordering = ('pk',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Submission(models.Model):
    Title = (('', ''), ('Prof', 'Prof'), ('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms'))
    Attendance = (('', ''), ('reporter', 'Reporter'), ('participant', 'Participant, without a report'))
    YesNo = (('', ''), ('yes', 'Yes'), ('no', 'No'))
    Areas = [('', '')] + [(str(c.id), str(c.title)) for c in TopicAreas.objects.all()]

    title = models.CharField(choices=Title, blank=False, max_length=255, help_text='Select an item…')
    first_name = models.CharField(max_length=255, blank=False)
    middle_name = models.CharField(max_length=255, blank=True)
    second_name = models.CharField(max_length=255, blank=False)
    company = models.CharField(max_length=255, blank=False)
    job_position = models.CharField(max_length=255, blank=False)
    attendance_status = models.CharField(choices=Attendance, max_length=255, blank=False, help_text='Select an item…')
    abstract_title = models.CharField(max_length=255, blank=True)
    abstract_text = models.TextField(blank=True, help_text="Not more than 500 words")
    section_1 = models.CharField(max_length=255, choices=Areas,
                                 help_text='Sections your report corresponds to (by priority of compliance)')
    section_2 = models.CharField(max_length=255, blank=True, choices=Areas,
                                 help_text='Sections your report corresponds to (by priority of compliance)')
    get_review = models.CharField('Would you like to review the Conference papers?', max_length=255, choices=YesNo,
                                  blank=True, help_text='Select an item…')
    email = models.EmailField(max_length=255, blank=False)
    telephone = models.CharField(max_length=255, blank=True)
    date_of_birth = models.CharField(max_length=255, blank=False, help_text="dd/mm/yyyy")
    citizenship = models.CharField(max_length=255, blank=False)
    visa = models.CharField('Do you need a visa?', choices=YesNo, max_length=255, blank=False,
                            help_text='Select an item…')
    passport = models.CharField('Passport №', max_length=255, blank=True)
    issued = models.CharField('Issued on', max_length=255, blank=True)
    valid = models.CharField('Valid by', max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    postal_address = models.CharField(max_length=255, blank=False)
    zip = models.CharField('ZIP', max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=False)
    hotel = models.CharField('Do you need a hotel?', max_length=255, blank=False, choices=YesNo,
                             help_text='Select an item…')
    accompanying = models.CharField('Will you be accompanying by a person?', max_length=255, blank=False, choices=YesNo,
                                    help_text='Select an item…')
    created_at = models.DateField(blank=True, null=True, default=datetime.date.today)

    class Meta:
        verbose_name = 'Submission'
        verbose_name_plural = 'Submissions'

    def __str__(self):
        return "Submission form"


@python_2_unicode_compatible
class SubmissionGuidelines(models.Model):
    title = models.CharField('Name', max_length=255, blank=True)
    description = models.TextField('Description')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Submission Guidelines'
        verbose_name_plural = 'Submission Guidelines'
        ordering = ('order',)

    def __str__(self):
        return self.title



@python_2_unicode_compatible
class News(models.Model):
    title = models.CharField(max_length=255, blank=False, default='')
    text = MarkdownField(blank=False)
    date = models.DateField(blank=False, default=datetime.date.today)
    published = models.BooleanField(blank=False, default=True)

    class Meta:
        verbose_name = 'News List'
        verbose_name_plural = 'News List'

    def __str__(self):
        return self.title



@python_2_unicode_compatible
class Practical(models.Model):
    title = models.CharField(max_length=255)
    description = MarkdownField(blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Practical Info'
        verbose_name_plural = 'Practical Info'
        ordering = ('order',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class PracticalBlock(models.Model):
    title = models.CharField(max_length=255, blank=True)
    text = MarkdownField()
    photo = models.ImageField(upload_to=RandomFileName('practical'), blank=True)
    link = models.URLField(blank=True)
    link_placeholder = models.CharField(max_length=255, blank=True, default='')
    practical = models.ForeignKey(Practical, on_delete=models.CASCADE, related_name='practical_block')

    class Meta:
        verbose_name = 'Practical Info Block'
        verbose_name_plural = 'Practical Info Block'
        ordering = ('pk',)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Fees(models.Model):
    num = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta:
        verbose_name = 'Fees'
        verbose_name_plural = 'Fees'
        ordering = ('order',)

    def __str__(self):
        return self.num + ' - ' + self.type + ' - ' + self.category

