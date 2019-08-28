'''
#           /       '_ /_/ 
#          ()(/__/)/(//)/  
#            /     _/      

'''
from django.test import TestCase
from collector.models.creaturess import Creature
from collector.tests.factories import CreatureFactory

class CreatureTest(TestCase):
  def test_creature_creation(self):
    c = CreatureFactory.build()
    self.assertTrue(isinstance(c,Character))

  def test_rid_after_save(self):
    c = CharacterFactory.create()    
    self.assertEquals(c.rid,'tastus_fabulus')
