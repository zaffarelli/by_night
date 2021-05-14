from django.urls import path, re_path
from collector.views.base import index, get_list, updown, userinput, display_lineage, add_creature, change_chronicle, \
    extract_raw, extract_roster, display_gaia_wheel, extract_mechanics, extract_per_group, display_crossover_sheet
from collector.views.creature_views import CreatureDetailView

urlpatterns = [
    path('', index, name='index'),
    re_path('^ajax/list/creatures/(?P<pid>\d+)/(?P<slug>\w+)/$', get_list, name='get_list'),
    re_path('^ajax/display/gaia_wheel/$', display_gaia_wheel, name='display_gaia_wheel'),
    re_path('^ajax/display/lineage$', display_lineage, name='display_lineage'),

    re_path('^ajax/switch/chronicle/(?P<rid>\w+)/$', change_chronicle, name='change_chronicle'),
    re_path('^ajax/view/creature/(?P<slug>\w+)/$', CreatureDetailView.as_view(), name='view_creature'),
    # re_path('^ajax/edit/creature/(?P<slug>\w+)/$', CreatureUpdateView.as_view(), name='edit_creature'),
    # re_path('^ajax/update/creature/(?P<slug>\w+)/$', CreatureUpdateView.as_view(), name='update_creature'),
    re_path('^ajax/display/crossover_sheet/$', display_crossover_sheet, name='display_crossover_sheet'),
    re_path('^ajax/display/crossover_sheet/(?P<slug>\w+)/$', display_crossover_sheet, name='display_crossover_sheet'),
    re_path('^ajax/add/creature/$', add_creature, name='add_creature'),
    re_path('^ajax/editable/updown$', updown, name='updown'),
    re_path('^ajax/editable/userinput$', userinput, name='userinput'),

    re_path('^api/text/(?P<slug>\w+)/$', extract_raw, name='extract_raw'),
    re_path('^api/roster/(?P<slug>\w+)/$', extract_roster, name='extract_roster'),
    re_path('^api/mechanics/$', extract_mechanics, name='extract_mechanics'),
    re_path('^api/group/(?P<slug>\w+)/$', extract_per_group, name='extract_per_group'),
]
