import factory
import datetime
from django.utils import timezone
from collector.models.creatures import Creature


class CharacterFactory(factory.django.DjangoModelFactory):
  class Meta:
    model = Creature
  name = 'Vlad Tepes'
  creature = 'kindred'
  sex = True
  pub_date = timezone.now()

