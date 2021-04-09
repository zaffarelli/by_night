"""
           /       '_ /_/
          ()(/__/)/(//)/
            /     _/

"""


from django.db.models.signals import pre_save
from django.dispatch import receiver
from collector.models.creatures import Creature


@receiver(pre_save, sender=Creature, dispatch_uid='update_creature')
def update_creature(sender, instance, **kwargs):
    instance.fix()
    #pass
