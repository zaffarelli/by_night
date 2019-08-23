'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django.contrib import admin

from collector.models.creatures import Creature, CreatureAdmin

admin.site.register(Creature, CreatureAdmin)
