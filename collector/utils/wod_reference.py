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
    current_chronicle = Chronicle.objects.filter(is_current=True).first()
    logger.debug(f'Current Chronicle found is {current_chronicle.acronym}.')
    return current_chronicle
