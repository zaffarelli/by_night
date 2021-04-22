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

def find_stat_property(creature,statistic):
    # You give 'kindred' / 'generation', it returns 'background3'
    lists = ['talents','skills','knowledges','backgrounds']
    property = 'n/a'
    for list in lists:
        if statistic in STATS_NAMES[creature][list]:
            property = f'{list[:-1]}{STATS_NAMES[creature][list].index(statistic)}'
            break
    return property


STATS_NAMES = {
    'fomori': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'intuition',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'leadership', 'melee', 'performance',
                   'stealth', 'survival'],
        'knowledges': ['bureaucracy', 'computer', 'enigmas', 'investigation', 'law', 'linguistics', 'medicine',
                       'occult', 'politics', 'science'],
        'backgrounds': ['allies', 'career', 'contacts', 'fame', 'family', 'equipment', 'influence',
                        'resources', 'status', 'true faith']
    },

    'garou': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'primal-urge',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'leadership', 'melee', 'performance',
                   'stealth', 'survival'],
        'knowledges': ['computer', 'enigmas', 'investigation', 'law', 'linguistics', 'medicine', 'occult', 'politics',
                       'rituals', 'science'],
        'backgrounds': ['allies', 'ancestors', 'contacts', 'fetish', 'kinfolk', 'mentor', 'pure-breed', 'resources',
                        'rites', 'totem']
    },
    'ghoul': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'intuition',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'leadership', 'melee', 'performance',
                   'stealth', 'survival'],
        'knowledges': ['bureaucracy', 'computer', 'finance', 'investigation', 'law', 'linguistics', 'medicine',
                       'occult', 'politics', 'science'],
        'backgrounds': ['allies', 'bond', 'contacts', 'fame', 'equipment', 'influence', 'mentor',
                        'resources', 'status', 'trust']
    },
    'kindred': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'leadership',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'melee', 'performance', 'security',
                   'stealth', 'survival'],
        'knowledges': ['academics', 'computer', 'finance', 'investigation', 'law', 'linguistics', 'medicine', 'occult',
                       'politics',
                       'science'],
        'backgrounds': ['allies', 'contacts', 'fame', 'generation', 'herd', 'influence', 'mentor',
                        'resources', 'retainers', 'status']
    },
    'kinfolk': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'intuition',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'leadership', 'melee', 'performance',
                   'stealth', 'survival'],
        'knowledges': ['bureaucracy', 'computer', 'enigmas', 'investigation', 'law', 'linguistics', 'medicine',
                       'occult', 'politics', 'science'],
        'backgrounds': ['allies', 'ancestors', 'contacts', 'equipment', 'favors', 'pure-breed', 'renown', 'resources',
                        'status', 'true faith']
    },
    'mortal': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'intuition',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'leadership', 'melee', 'performance',
                   'stealth', 'survival'],
        'knowledges': ['bureaucracy', 'computer', 'enigmas', 'investigation', 'law', 'linguistics', 'medicine',
                       'occult', 'politics', 'science'],
        'backgrounds': ['allies', 'career', 'contacts', 'fame', 'family', 'equipment', 'influence',
                        'resources', 'status', 'true faith']
    }

}
