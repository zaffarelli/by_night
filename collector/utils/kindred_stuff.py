from collector.models.creatures import Creature
import json
import logging
from django.conf import settings
from collector.utils.wod_reference import get_current_chronicle

chronicle = get_current_chronicle()
logger = logging.Logger(__name__)


def cleanup_spare_unknown():
    action = 0
    logger.debug("=> Removing 'Unknown...' without infans")
    all = Creature.objects.filter(creature='kindred', name__contains='Unknown')
    for kindred in all:
        infans = Creature.objects.filter(sire=kindred.name)
        if infans is None:
            logger.debug(" --> Deleting [%s]: No infans." % (kindred.name))
            kindred.delete()
            action += 1
        if kindred.background3 >= 10:
            logger.debug(" --> Deleting [%s]: Generation is too low" % (kindred.name))
            kindred.delete()
            action += 1
    return action


def cleanup_false_unknown_reference():
    action = 0
    logger.info("=> Removing 'Unknown...' sire if they don't exist")
    all = Creature.objects.filter(creature='kindred', sire__contains='Unknown')
    for kindred in all:
        sire = Creature.objects.filter(name=kindred.sire).first()
        if sire is None:
            logger.info(" --> No sire [%s] found for [%s]: Updating kindred." % (kindred.sire, kindred.name))
            kindred.sire = ''
            kindred.save()
            action += 1
    return action


def create_named_sires():
    action = 0
    logger.info("=> Creating Sires")
    all = Creature.objects.filter(creature='kindred').exclude(sire='').exclude(background3__gte=8)
    for kindred in all:
        sire = Creature.objects.filter(creature='kindred', name=kindred.sire).first()
        if sire is None:
            embracer = Creature()
            embracer.background3 = kindred.background3 + 1
            embracer.family = kindred.family
            embracer.name = kindred.sire
            embracer.ghost = True
            embracer.save()
            logger.info(" --> Sire [%s] created for [%s]" % (embracer.name, kindred.name))
            action += 1
    return action


def create_sires():
    action = 0
    logger.info("=> Siring 'Unknown...'")
    all_sireless = Creature.objects.filter(creature='kindred', sire='', background3__lte=7)
    ghost_sires = {}
    for kindred in all_sireless:
        str = "Unknown %dth generation %s" % (13 - (kindred.background3 + 1), kindred.root_family())
        grandsire = "Unknown %dth generation %s" % (13 - (kindred.background3 + 2), kindred.root_family())
        if kindred.background3 + 2 == 10:
            if kindred.root_family() in ['Toreador', 'Daughter of Cacophony']:
                grandsire = 'Arikel'
            elif kindred.root_family() == 'Malkavian':
                grandsire = 'Malkav'
            elif kindred.root_family() == 'Salubri':
                grandsire = 'Saulot'
            elif kindred.root_family() == 'Gangrel':
                grandsire = 'Ennoia'
            elif kindred.root_family() == 'Ventrue':
                grandsire = 'Ventru'
            elif kindred.root_family() == 'Cappadocian':
                grandsire = 'Cappadocius'
            elif kindred.root_family() == 'Nosferatu':
                grandsire = 'Absimiliard'
            elif kindred.root_family() == 'Ravnos':
                grandsire = 'Dracian'
            elif kindred.root_family() == 'Setite':
                grandsire = 'Set'
            elif kindred.root_family() == 'Assamite':
                grandsire = 'Haqim'
            elif kindred.root_family() in ['Lasombra', 'Kiasyd']:
                grandsire = 'Lasombra'
            elif kindred.root_family() == 'Tzimisce':
                grandsire = 'The Eldest'
            elif kindred.root_family() == 'Brujah':
                grandsire = 'Brujah'
        elif kindred.background3 + 2 == 9:
            if kindred.root_family() == 'Giovanni':
                grandsire = 'Augustus Giovanni'
            elif kindred.root_family() == 'Tremere':
                grandsire = 'Tremere'
            elif kindred.root_family() == 'Brujah':
                grandsire = 'Troile'
        j = {"ghost": True, "family": kindred.root_family(), "background3": kindred.background3 + 1, "name": str,
             "sire": grandsire}
        ghost_sires[str] = j
        kindred.sire = str
        kindred.save()
        action += 1
    logger.info("=> Kindred sires to be created")
    logger.info(json.dumps(ghost_sires, indent=2))
    logger.info("=> Creating Linked Ghosts")
    for key in ghost_sires:
        gs = ghost_sires[key]
        logger.info(" ----> Dealing with ghost %s" % (gs['name']))
        f = Creature.objects.filter(name=gs['name']).first()
        if f is None:
            t = Creature()
            t.name = gs['name']
            t.background3 = gs['background3']
            t.family = gs['family']
            t.ghost = gs['ghost']
            t.sire = gs['sire']
            t.save()
            logger.info(" --> Adding ghost %s" % (t.name))
            action += 1
    return action


def check_caine_roots():
    action = 1
    while action > 0:
        action = cleanup_spare_unknown()
        action = cleanup_false_unknown_reference()
        action = create_named_sires()
        action = create_sires()
        logger.info("Number of actions executed: %d" % (action))
    x = Creature.objects.filter(creature='kindred', name="Caine").first()
    data = x.find_lineage()
    with open(f'{settings.STATICFILES_DIRS}/js/kindred.json', 'w') as fp:
        json.dump(data, fp)
    logger.info("--> Lineage Done")
    return {'responseText': 'Ok'}


def blank_str(name, gen, sire, clan=''):
    root_family = clan.replace(' Antitribu', '')
    return {'name': name, 'clan': clan, 'family': root_family, 'sire': sire, 'condition': 'OK', 'status': 'OK', 'generation': gen,
            'ghost': True, 'mythic': False, 'faction': '', 'children': []}


def create_mythics():
    generations = {
        '1': [],
        '2': [],
        '3': [],
        '4': [],
        '5': [],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
        '10': [],
        '11': [],
        '12': [],
        '13': [],
    }
    kindred_stack = []
    kindred_stack.append(blank_str('Caine', 1, ""))
    kindred_stack.append(blank_str('Enoch', 2, "Caine"))
    kindred_stack.append(blank_str('Irad', 2, "Caine"))
    kindred_stack.append(blank_str('Zillah', 2, "Caine"))
    kindred_stack.append(blank_str('The Crone', 2, "Caine"))
    kindred_stack.append(blank_str('Lilith', 2, "Caine"))
    kindred_stack.append(blank_str('Arikel', 3, "Enoch", 'Toreador'))
    kindred_stack.append(blank_str('Malkav', 3, "Enoch", 'Malkavian'))
    kindred_stack.append(blank_str('Saulot', 3, "Enoch", 'Salubri'))
    kindred_stack.append(blank_str('Ventru', 3, "Irad", 'Ventrue'))
    kindred_stack.append(blank_str('Brujah', 3, "Irad", 'True Brujah'))
    kindred_stack.append(blank_str('Cappadocius', 3, "Irad", 'Cappadocian'))
    kindred_stack.append(blank_str('Lasombra', 3, "Irad", 'Lasombra'))
    kindred_stack.append(blank_str('Ennoia', 3, "Lilith", 'Gangrel'))
    kindred_stack.append(blank_str('Ravnos', 3, "The Crone", 'Ravnos'))
    kindred_stack.append(blank_str('The Elder One', 3, "The Crone", 'Tzimisce'))
    kindred_stack.append(blank_str('Absimilard', 3, "Zillah", 'Nosferatu'))
    kindred_stack.append(blank_str('Set', 3, "Zillah", 'Setite'))
    kindred_stack.append(blank_str('Haqim', 3, "Zillah", 'Assamite'))
    kindred_stack.append(blank_str('Troile', 4, "Brujah", 'Brujah'))
    kindred_stack.append(blank_str('Augustus Giovanni', 4, "Cappadocius", 'Giovanni'))
    kindred_stack.append(blank_str('Tremere', 4, "Saulot", 'Tremere'))
    for k in kindred_stack:
        k['mythic'] = True
        generations[f'{k["generation"]}'].append(k)
    return generations


def improvise_id():
    import random
    sequence = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for _ in range(6):
        s += random.choice(sequence)
    return s


def build_per_primogen(param=None):
    chronicle = get_current_chronicle()
    cainites = create_mythics()
    if param is None:
        kindreds = Creature.objects.filter(creature='kindred', ghost=False, mythic=False, chronicle=chronicle.acronym).order_by('family')
    else:
        kindreds = Creature.objects.filter(creature='kindred', faction=param, ghost=False, mythic=False, chronicle=chronicle.acronym).order_by('family')
    # Improvise empty sires
    for kindred in kindreds:
        gen = 13 - kindred.background3
        k = kindred.json_str()
        if kindred.sire == '':
            k['sire'] = f'temporary_{improvise_id()}_{gen-1}_{k["name"]}_{k["clan"]}'
        else:
            k['sire'] = kindred.sire
        cainites[f'{gen}'].append(k)

    # Try to fill empty lineages
    for gen in range(13, 0, -1):
        for k in cainites[f'{gen}']:
            if gen > 1:
                if k['sire'].startswith('temporary_'):
                    sire = None
                    for item in cainites[f'{gen-1}']:
                        if item.get('sire') == k['sire']:
                            sire = item
                    if sire is None:
                        words = k["sire"].split('_')
                        sire = blank_str(words[1], words[2], "TBD", words[4])
                        sire['children'].append(k)
                        k['sire'] = sire['name']
                        cainites[f'{gen-1}'].append(sire)
                else:
                    if k["sire"] == "TBD":
                        # We need here to find a matchingsire according to clan
                        found = None
                        for s in cainites[f'{gen-1}']:
                            if s["family"] == k["family"]:
                                k["sire"] = s["name"]
                                s["children"].append(k)
                                found = s
                                break
                        if found is None:
                            sire = blank_str(improvise_id(), gen-1, "TBD", k['clan'])
                            sire['children'].append(k)
                            k['sire'] = sire['name']
                            cainites[f'{gen - 1}'].append(sire)
                    else:
                        sire = None
                        for item in cainites[f'{gen-1}']:
                            if item['name'] == k["sire"]:
                                sire = item
                                sire['children'].append(k)
                        if sire is None:
                            sire = blank_str(k['sire'], gen-1, "TBD", k['clan'])
                            sire['children'].append(k)
                            k['sire'] = sire['name']
                            cainites[f'{gen - 1}'].append(sire)
    str = json.dumps(cainites['1'], indent=4, sort_keys=False)
    print(str)
    return str


def domitor_from_sire():
    kindreds = Creature.objects.filter(chronicle=chronicle.acronym)
    for k in kindreds:
        if k.sire != '':
            sires = Creature.objects.filter(name=k.sire)
            if len(sires) == 1:
                s = sires.first()
            else:
                s = None
            if s is not None:
                k.domitor = s
                k.save()


def build_gaia_wheel():
    chronicle = get_current_chronicle()
    creatures = Creature.objects.filter(chronicle=chronicle.acronym).exclude(mythic=True).exclude(ghost=True).order_by(
        '-faction', 'display_pole')
    for creature in creatures:
        creature.need_fix = True
        creature.save()
    wyrm_list = []
    weaver_list = []
    wyld_list = []
    for c in creatures:
        creature_dict = {
            'name': c.name,
            'player': c.player,
            'creature': c.creature,
            'family': c.family,
            'group': c.group,
            'groupspec': c.groupspec,
            'display_gauge': c.display_gauge,
            'display_pole': c.display_pole,
            'freebies': c.freebies,
            'auspice': c.auspice,
            'breed': c.breed,
            'rank': c.rank,
            'rid': c.rid,
            'position': c.position,
            'status': c.status
        }
        if (c.faction == 'Camarilla') or (c.faction == 'Sabbat') or (c.faction == 'Independant') or (c.faction == 'Anarchs') or (
                c.faction == 'Inconnu') or (c.faction == 'Pentex'):
            wyrm_list.append(creature_dict)
        elif (c.faction == 'Gaia'):
            wyld_list.append(creature_dict)
        else:
            weaver_list.append(creature_dict)
    d3js_data = {'weaver': weaver_list, 'wyrm': wyrm_list, 'wyld': wyld_list}
    all = json.dumps(d3js_data, indent=4, sort_keys=False)
    return all
