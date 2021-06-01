from django.db import models
from django.contrib import admin
from storytelling.models.stories import Story
from collector.utils.helper import json_default
import json
import logging

logger = logging.Logger(__name__)


class Place(models.Model):
    name = models.CharField(max_length=128, default='')
    acronym = models.CharField(max_length=24, default='')
    story = models.ForeignKey(Story, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1024, blank=True, default='')
    is_current = models.BooleanField(default=False)

    def __str__(self):
        st = ''
        if self.story is not None:
            st = self.story.name
        return f'{self.name} {st}'

    def toJSON(self):
        jstr = json.dumps(self, default=json_default, sort_keys=True, indent=4)
        return jstr


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'acronym', 'story']
    ordering = ['story']
    list_filter = ['story']
    search_fields = ['name', 'description']
