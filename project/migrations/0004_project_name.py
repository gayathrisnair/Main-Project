# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-27 05:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
