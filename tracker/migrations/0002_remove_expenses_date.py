# -*- coding: utf-8 -*-
#Generated by Django 3.1.2 on 2020-10-21 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='date',
        ),
    ]
