# -*- coding: utf-8 -*-
# Generated by Django 3.1.2 on 2020-10-21 20:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tracker', '0002_remove_expenses_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='usr',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
