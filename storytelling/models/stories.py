from django.db import models
from django.contrib import admin
from collector.models.chronicles import Chronicle
from collector.utils.helper import json_default
from datetime import datetime
import json

import logging

logger = logging.Logger(__name__)


class Story(models.Model):
    name = models.CharField(max_length=128, default='')
    chronicle = models.ForeignKey(Chronicle, on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1024, blank=True, default='')
    dday = models.DateTimeField(default=datetime.now,blank=True,null=True)
    is_current = models.BooleanField(default=False)

    @property
    def story_end_time(self):
        from storytelling.models.scenes import Scene
        all = Scene.objects.filter(story=self)
        end_time = 0
        for s in all:
            if s.time_offset_hours > end_time:
                end_time = s.time_offset_hours
        return end_time

    @property
    def all_places(self):
        from storytelling.models.places import Place
        list = []
        all = Place.objects.filter(story=self)
        for p in all:
            list.append({'name': p.name, 'id': p.id, 'acronym': p.acronym})
        return list

    @property
    def all_scenes(self):
        from storytelling.models.scenes import Scene
        list = []
        all = Scene.objects.filter(story=self)
        for s in all:
            list.append({'name': s.name, 'id': s.id, 'time': s.time_offset_hours, 'place': s.place.id})
        return list

    def toJSON(self):
        jstr = json.dumps(self, default=json_default, sort_keys=True, indent=4)
        return jstr

    def __str__(self):
        ch = ''
        if self.chronicle is not None:
            ch = self.chronicle.name
        return f'{self.name} ({ch})'


class StoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'chronicle', 'dday', 'description', 'is_current']
    ordering = ['dday', 'name']
    list_filter = ['dday', 'chronicle']
    search_fields = ['name', 'description']
