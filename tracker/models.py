# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from six import python_2_unicode_compatible
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
exp_category=[('electronics', 'Electronics'),
    ('fashion', 'Fashion'),
    ('kitchen', 'Kitchen'),
    ('pets', 'Pets'),
    ('home utility','Home Utility'),
    ('vehicle utilities','Vehicle Utilities'),
    ('misc', 'Misc'),
    ('other', 'Other')]

class Expenses(models.Model):
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
    amount = models.IntegerField(default=0)
    exp_type = models.CharField(max_length=20, choices=exp_category, default='Other')

    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return u"{} | {} | {} |  {} | {}".format(self.usr, self.name,self.amount, self.exp_type, self.date)

    def get_absolute_url(self):
        return reverse('index')
