from collector.models.chronicles import Chronicle
import logging

logger = logging.Logger(__name__)


def get_current_chronicle():
    ch = None
    try:
        current_chronicle = Chronicle.objects.filter(is_current=True).first()
        ch = current_chronicle
    except:
        first_chronicle = Chronicle.objects.first()
        first_chronicle.is_current = True
        first_chronicle.save()
        ch = first_chronicle
    return ch

def set_chronicle(acro):
    for c in Chronicle.objects.all():
        if c.acronym == acro:
            c.is_current = True
            logger.debug(f'Current Chronicle set to is {c.acronym}.')
        else:
            c.is_current = False
        c.save()


def find_stat_property(creature, statistic):
    # You give 'kindred' / 'generation', it returns 'background3'
    lists = ['attributes', 'talents', 'skills', 'knowledges', 'backgrounds']
    property = 'n/a'
    for list in lists:
        if statistic in STATS_NAMES[creature][list]:
            property = f'{list[:-1]}{STATS_NAMES[creature][list].index(statistic)}'
            logger.debug(f'Parsing --> {property}')
            break
    return property


STATS_NAMES = {
    'fomori': {
        'attributes': ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'appearance', 'perception',
                       'intelligence', 'wits'],
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
        'attributes': ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'appearance', 'perception',
                       'intelligence', 'wits'],
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
        'attributes': ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'appearance', 'perception',
                       'intelligence', 'wits'],
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
        'attributes': ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'appearance', 'perception',
                       'intelligence', 'wits'],
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
        'attributes': ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'appearance', 'perception',
                       'intelligence', 'wits'],
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
        'attributes': ['strength', 'dexterity', 'stamina', 'charisma', 'manipulation', 'appearance', 'perception',
                       'intelligence', 'wits'],
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

STATS_TEMPLATES = {
    'changeling': {
        'attributes': '7/5/3',
        'abilities': '13/9/5',
        'arts': '3',
        'realms': '5',
        'backgrounds': '5',
        'freebies': '15'
    },
    'fomori': {
        'attributes': '6/4/3',
        'abilities': '11/7/5',
        'disciplines': '1',
        'backgrounds': '7',
        'willpower': '3',
        'freebies': '21'
    },
    'garou': {
        'attributes': '7/5/3',
        'abilities': '13/9/5',
        'gifts': '5',
        'backgrounds': '5',
        'freebies': '15'
    },
    'ghoul': {
        'attributes': '6/4/3',
        'abilities': '11/7/5',
        'disciplines': '1',
        'backgrounds': '7',
        'willpower': '3',
        'freebies': '21'
    },
    'kindred': {
        'attributes': '7/5/3',
        'abilities': '13/9/5',
        'disciplines': '3',
        'backgrounds': '5',
        'virtues': '10',
        'freebies': '15'
    },
    'kinfolk': {
        'attributes': '6/4/3',
        'abilities': '11/7/5',
        'disciplines': '1',
        'backgrounds': '7',
        'willpower': '3',
        'freebies': '21'
    },
    'mage': {
        'attributes': '7/5/3',
        'abilities': '13/9/5',
        'arete': '1',
        'spheres': '5',
        'backgrounds': '7',
        'willpower': '5',
        'freebies': '15'
    },
    'mortal': {
        'attributes': '6/4/3',
        'abilities': '11/7/5',
        'disciplines': '1',
        'backgrounds': '7',
        'willpower': '3',
        'freebies': '21'
    },
    'wraith': {
        'attributes': '7/5/3',
        'abilities': '13/9/5',
        'arcanos': '5',
        'passions': '10',
        'fetters': '10',
        'backgrounds': '7',
        'willpower': '5',
        'pathos': '5',
        'freebies': '15'
    },

}

ARCHETYPES = [
    'Alpha',
    'Architect',
    'Autocrat',
    'Avant-garde',
    'Bon Vivant',
    'Bravo',
    'Builder',
    'Bureaucrat',
    'Caregiver',
    'Celebrant',
    'Child',
    'Competitor',
    'Confident',
    'Conformist',
    'Conniver',
    'Critic',
    'Curmudgeon',
    'Deviant',
    'Director',
    'Explorer',
    'Fanatic',
    'Follower',
    'Gallant',
    'Hedonist',
    'Jester',
    'Judge',
    'Loner',
    'Martyr',
    'Masochist',
    'Monster',
    'Pedagogue',
    'Penitent',
    'Perfectionist',
    'Predator',
    'Rebel',
    'Reluctant',
    'Rogue',
    'Show off',
    'Survivor',
    'Thrill-seeker',
    'Traditionalist',
    'Trickster',
    'Visionary'
]

BREEDS = ['Homid', 'Metis', 'Lupus']

AUSPICES = ['Ragabasch', 'Theurge', 'Philodox', 'Galliard', 'Ahroun']

RANKS = ['Cliath', 'Fostern', 'Adren', 'Athro', 'Elder']

FONTSET = ['Cinzel', 'Trade+Winds', 'Imprima', 'Roboto', 'Philosopher', 'Ruda', 'Khand', 'Allura', 'Gochi+Hand', 'Reggae+One', 'Syne+Mono', 'Zilla+Slab', 'Spartan']


GM_SHORTCUTS = {
    'garou': [
        ['perception', 'alertness'],
        ['perception', 'primal-urge'],
        ['dexterity', 'brawl'],
        ['stamina', 'primal-urge'],
        ['wits', 'enigmas'],
        ['appearance', 'subterfuge']
    ],
    'kindred': [],
    'mortal': [],
    'kinfolk': [],
    'ghoul': [],
    'fomori': [],
}