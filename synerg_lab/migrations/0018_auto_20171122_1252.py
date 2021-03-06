# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('synerg_lab', '0017_auto_20171120_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('answer_text', models.CharField(help_text='This will be shown as a answer of related question', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(help_text='This field is the question that will be shown', max_length=500)),
                ('answer_type', models.CharField(choices=[(None, 'Choose a type for answers!'), ('Answer Type', [('single', 'Single choice'), ('multi', 'Multi choice')])], max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='This will be displayed to users while giving feedback.', max_length=50)),
                ('description', models.CharField(blank=True, help_text='Describe the region if required', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='What is the room generally called? ex:- seil lab,circular hall etc', max_length=100)),
                ('short_name', models.CharField(help_text='Short name of the room. ex:- SIC 201,SIA 310 etc', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('sensor_type', models.CharField(choices=[(None, 'Choose sensor type!'), ('H', 'Humidity'), ('T', 'Temperature'), ('H_T', 'Humidity and Temperature')], max_length=50)),
                ('region', models.ManyToManyField(to='synerg_lab.Region')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(help_text='Full name of user', max_length=100)),
                ('username', models.CharField(help_text='username for login', max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(help_text='password for login', max_length=50)),
                ('email', models.EmailField(help_text='Email for contacting the user', max_length=100)),
                ('height', models.FloatField(blank=True, help_text='Meta data for future study(if available)', null=True)),
                ('weight', models.FloatField(blank=True, help_text='Meta data for future study(if available)', null=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerg_lab.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('answer_time', models.DateTimeField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerg_lab.Answer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerg_lab.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='question',
            name='text',
        ),
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(blank=True, help_text='This will be shown as question for feedback', max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_type',
            field=models.CharField(choices=[(None, 'Choose answer type!'), ('S', 'Single Choice Answer'), ('M', 'Multiple Choice Answer')], help_text='Single Choice Answer will render radio button for answers while Multiple Choice Answer will render check box for answers', max_length=50),
        ),
        migrations.AddField(
            model_name='region',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerg_lab.Room'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synerg_lab.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ManyToManyField(through='synerg_lab.UserAnswer', to='synerg_lab.User'),
        ),
        migrations.AddField(
            model_name='question',
            name='region',
            field=models.ManyToManyField(to='synerg_lab.Region'),
        ),
    ]
