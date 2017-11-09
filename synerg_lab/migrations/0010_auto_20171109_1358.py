# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('synerg_lab', '0009_auto_20171109_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[(None, 'Choose a type for answers!'), ('Answer Type', [('text', 'Text'), ('single', 'Single choice'), ('multi', 'Multi choice')])], max_length=10),
        ),
    ]