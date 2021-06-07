import factory
from django.utils import timezone
from collector.models.creatures import Creature


class BlankCreatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Creature
    pub_date = timezone.now()

class CreatureFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Creature
    name = 'Vlad Tepes'
    creature = 'kindred'
    sex = False
    pub_date = timezone.now()
