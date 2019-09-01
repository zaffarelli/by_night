'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django.contrib import admin

from collector.models.creatures import Creature, CreatureAdmin
from collector.models.chronicles import Chronicle, ChronicleAdmin

admin.site.register(Creature, CreatureAdmin)
admin.site.register(Chronicle, ChronicleAdmin)
