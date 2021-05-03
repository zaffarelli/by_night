"""
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

"""
from collector.models.chronicles import Chronicle
import logging

logger = logging.Logger(__name__)


def get_current_chronicle():
    try:
        current_chronicle = Chronicle.objects.filter(is_current=True).first()
        return current_chronicle
    except:
        first_chronicle = Chronicle.objects.first()
        first_chronicle.is_current = True
        first_chronicle.save()
        return first_chronicle


def set_chronicle(acro):
    for c in Chronicle.objects.all():
        c.is_current = c.acronym == acro
        if c.is_current:
            logger.debug(f'Current Chronicle set to is {c.acronym}.')
        c.save()

def find_stat_property(creature,statistic):
    # You give 'kindred' / 'generation', it returns 'background3'
    lists = ['talents','skills','knowledges','backgrounds']
    property = 'n/a'
    for list in lists:
        if statistic in STATS_NAMES[creature][list]:
            property = f'{list[:-1]}{STATS_NAMES[creature][list].index(statistic)}'
            logger.debug(f'Parsing --> {property}')
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
        'knowledges': ['academics', 'computer', 'finance', 'investigation', 'law', 'linguistics', 'medicine',
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
        'knowledges': ['academics', 'computer', 'enigmas', 'investigation', 'law', 'linguistics', 'medicine',
                       'occult', 'politics', 'science'],
        'backgrounds': ['allies', 'ancestors', 'contacts', 'equipment', 'favors', 'pure-breed', 'renown', 'resources',
                        'status', 'true faith']
    },
    'mortal': {
        'talents': ['alertness', 'athletics', 'brawl', 'dodge', 'empathy', 'expression', 'intimidation', 'intuition',
                    'streetwise', 'subterfuge'],
        'skills': ['animal ken', 'craft', 'drive', 'etiquette', 'firearms', 'leadership', 'melee', 'performance',
                   'stealth', 'survival'],
        'knowledges': ['academics', 'computer', 'enigmas', 'investigation', 'law', 'linguistics', 'medicine',
                       'occult', 'politics', 'science'],
        'backgrounds': ['allies', 'career', 'contacts', 'fame', 'family', 'equipment', 'influence',
                        'resources', 'status', 'true faith']
    }

}
