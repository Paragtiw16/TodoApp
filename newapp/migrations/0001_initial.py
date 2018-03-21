# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-21 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=550, null=True)),
                ('password', models.CharField(blank=True, max_length=550, null=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contactno', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(default=0)),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Logins')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=550, null=True)),
                ('description', models.CharField(blank=True, max_length=550, null=True)),
                ('duedate', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('status', models.BooleanField(default=False)),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.Logins')),
            ],
        ),
    ]
