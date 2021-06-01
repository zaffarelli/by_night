from django.db import models
from django.contrib import admin
from storytelling.models.stories import Story
from storytelling.models.places import Place
from datetime import datetime
from collector.utils.helper import json_default
import json
import logging

logger = logging.Logger(__name__)


class Scene(models.Model):
    name = models.CharField(max_length=128, default='')
    story = models.ForeignKey(Story, on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    time_offset_hours = models.IntegerField(default=-1, blank=True)
    time_offset_custom = models.CharField(default='', max_length=32, blank=True)
    day = models.DateTimeField(default=datetime.now,blank=True,null=True)

    description = models.TextField(max_length=1024, blank=True, default='')
    era = models.CharField(max_length=16, blank=True, default='2019')
    is_current = models.BooleanField(default=False)

    def fix(self):
        if self.time_offset_hours >= 0:
            self.time_offset_custom = f'{int(self.time_offset_hours/24)} {self.time_offset_hours%24}'
        else:
            words = self.time_offset_custom.split(' ')
            if len(words) == 2:
                self.time_offset_hours = int(words[0])*24+int(words[1])
            else:
                self.time_offset_hours = -1

    def toJSON(self):
        jstr = json.dumps(self, default=json_default, sort_keys=True, indent=4)
        return jstr


    def __str__(self):
        st = ''
        if self.story is not None:
            st = self.story.name
        return f'{self.name} {st}'


def refix(modeladmin, request, queryset):
    for scene in queryset:
        scene.fix()
        scene.save()
    short_description = 'Fix scenes'


class SceneAdmin(admin.ModelAdmin):
    list_display = ['name', 'story', 'place', 'time_offset_custom', 'time_offset_hours', 'description']
    ordering = ['place', 'time_offset_hours', 'name']
    list_filter = ['name', 'description', 'story']
    search_fields = ['name', 'description']
    actions = [refix]
