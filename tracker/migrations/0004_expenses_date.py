# -*- coding: utf-8 -*-
# Generated by Django 3.1.2 on 2020-10-21 20:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_expenses_usr'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
