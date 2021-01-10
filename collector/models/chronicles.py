"""
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import json

import logging

logger = logging.Logger(__name__)


class Chronicle(models.Model):
    name = models.CharField(max_length=128, default='')
    acronym = models.CharField(max_length=16, blank=True, default='')
    era = models.IntegerField(default=2019)
    main_creature = models.CharField(max_length=128, blank=True, default='')
    image_logo = models.CharField(max_length=128, blank=True, default='')
    description = models.TextField(max_length=1024, blank=True, default='')
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.acronym


class ChronicleAdmin(admin.ModelAdmin):
    list_display = ['acronym', 'name', 'description', 'main_creature', 'is_current']
    ordering = ['acronym']