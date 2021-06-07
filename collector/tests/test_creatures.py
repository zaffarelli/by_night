from django.test import TestCase
from collector.tests.factories import BlankCreatureFactory
from collector.utils.wod_reference import get_current_chronicle


class CreatureTest(TestCase):
  def test_creature_default_chronicle(self):
    chronicle = get_current_chronicle()
    c = BlankCreatureFactory.build()
    self.assertTrue(c.chronicle == chronicle.acronym)


