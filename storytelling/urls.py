from django.urls import  re_path
from storytelling.views.base import display_storytelling


urlpatterns = [
    re_path(r'^ajax/display/storytelling/$', display_storytelling, name='display_storytelling'),
]
