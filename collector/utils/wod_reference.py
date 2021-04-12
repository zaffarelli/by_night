"""
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

"""
from collector.models.chronicles import Chronicle
import logging

logger = logging.Logger(__name__)


def get_current_chronicle():
    # current_chronicle = Chronicle.objects.get(is_current=True)
    try:
        current_chronicle = Chronicle.objects.filter(is_current=True).first()
        logger.debug(f'Current Chronicle found is {current_chronicle.acronym}.')
        return current_chronicle
    except:
        c = Chronicle.objects.first()
        c.is_current = True
        c.save()
        # dummy = Chronicle()
        # dummy.name='dummy'
        # dummy.acronym='dummy'
        # dummy.era = 2021
        # dummy.is_current = True

        return dummy

def set_chronicle(acro):
    for c in Chronicle.objects.all():
        c.is_current = c.acronym == acro
        if c.is_current:
            logger.debug(f'Current Chronicle set to is {current_chronicle.acronym}.')
        c.save()
