"""
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

"""
from django.urls import path, re_path
from collector.views.base import index, get_list, updown, userinput, update_lineage, add_creature, change_chronicle
from collector.views.creature_views import CreatureUpdateView, CreatureDetailView

urlpatterns = [
    path('', index, name='index'),
    re_path('^ajax/list/(?P<pid>\d+)/$', get_list, name='get_list'),
    re_path('^ajax/chronicle/(?P<slug>\w+)/$', change_chronicle, name='change_chronicle'),
    re_path('^ajax/view/creature/(?P<pk>\d+)/$', CreatureDetailView.as_view(), name='view_creature'),
    re_path('^ajax/edit/creature/(?P<pk>\d+)/$', CreatureUpdateView.as_view(), name='edit_creature'),
    re_path('^ajax/update/creature/(?P<id>\d+)/$', CreatureUpdateView.as_view(), name='update_creature'),
    re_path('^ajax/add/creature/$', add_creature, name='add_creature'),
    re_path('^ajax/editable/updown$', updown, name='updown'),
    re_path('^ajax/editable/userinput$', userinput, name='userinput'),
    re_path('^ajax/update/lineage$', update_lineage, name='update_lineage'),
]
