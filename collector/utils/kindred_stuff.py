from collector.models.creatures import Creature
import json
import logging
import os
from django.conf import settings
from collector.utils.wod_reference import get_current_chronicle

chronicle = get_current_chronicle()
logger = logging.Logger(__name__)



def cleanup_spare_unknown():
    action = 0
    print("CLEANING UP SPARE UNKNOWNS!!!")
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
        if (kindred.background3 + 2 == 10):
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
        elif (kindred.background3 + 2 == 9):
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


def blank_str(str,gen,id,sire):
    return {'name': str, 'clan': '', 'sire': sire, 'condition': 'OK', 'status':'OK', 'generation': gen,
            'ghost': True, 'faction': '', 'id': id, 'children': []}


def build_per_primogen():
    # kindreds = Creature.objects.filter(creature='kindred', chronicle=chronicle.acronym)
    # for kindred in kindreds:
    #     if kindred.ghost:
    #         kindred.delete()
        # else:
        #
        #     kindred.sire = ''
        #     kindred.save()
    cainites = {
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
    for gen in range(1, 14):
        sire = ''
        if gen > 1:
            sire = f'cainite_{gen-1}'
        cainites[f'{gen}'] = [blank_str(f'cainite_{gen}', gen, gen+1000000, sire)]
    # STARTING_GENERATION = 6
    kindreds = Creature.objects.filter(creature='kindred', ghost=False, mythic=False, chronicle=chronicle.acronym).order_by('family')

    for kindred in kindreds:
        gen = 13 - kindred.background3
        print(cainites[f'{gen}'])
        k = kindred.json_str()
        if kindred.sire == '':
            k['sire'] = f'cainite_{gen -1}'
        else:
            if not kindred.ghost:
                k['sire'] = kindred.sire
            else:
                k['sire'] = f'cainite_{gen - 1}'

        sk = json.dumps(k, indent=4, sort_keys=False)
        print(f'---> {sk}')
        cainites[f'{gen}'].append(k)

    #str = json.dumps(cainites,indent=4, sort_keys=False)
    #print(str)

    for gen in range(13, 0, -1):
        print("")
        print(f'--- Handling {gen} generation: ')
        for k in cainites[f'{gen}']:
            if not k['ghost']:
                print("")
                print(f' -- Handling {k["name"]}: ')
            if gen > 1:
                if k['sire'] == '':
                    if not k['ghost']:
                        print("No sire")
                    sire_name = f'cainite_{gen}'
                    if not k['ghost']:
                        print(f"Sire name for {k['name']} is {sire_name}")
                    sire = None
                    for item in cainites[f'{gen-1}']:
                        if item.get('sire') == sire_name:
                            sire = item
                    if sire:
                        if not k['ghost']:
                            print(sire)
                        sire['children'].append(k)
                        if not k['ghost']:
                            print(k)
                else:
                    if not k['ghost']:
                        print("Sire is not blank")
                    sire_name = k['sire']
                    if not k['ghost']:
                        print(f"  - Sire name for {k['name']} is {sire_name}")
                    sire = None
                    for item in cainites[f'{gen-1}']:
                        # if not k['ghost']:
                        #     print(f'    :checking: {item}')
                        if item['name'] == sire_name:
                            sire = item
                    if sire:
                        if not k['ghost']:
                            print(f'    --> Adding {k["name"]} to {sire["name"]} children.')
                        sire['children'].append(k)
                if not k['ghost']:
                    print(sire)

    str = json.dumps(cainites['1'], indent=4, sort_keys=False)
    #print(str)

    # print(settings.STATICFILES_DIRS)
    # with open(f'{settings.STATICFILES_DIRS}/js/kindred.json', 'w') as fp:
    #     json.dump(cainites['1'], fp)
    return str #cainites['1']


def domitor_from_sire():
    kindreds = Creature.objects.filter(chronicle=chronicle.acronym)
    for k in kindreds:
        if k.sire != '':
            print(f'Searching sire [{k.sire}]...')
            sires = Creature.objects.filter(name=k.sire)
            if len(sires)==1:
                s = sires.first()
            else:
                s = None
            if s is not None:
                k.domitor = s
                print(f'--> {k.name} has sire {k.sire} so domitor must be {s.name}')
                k.save()
            else:
                print(f'XX> {k.name} has sire {k.sire} was not found...')
                #k.domitor = None
                #k.save()
        else:
            print(f'X-> {k.name} has no sire {k.sire}.')

def build_gaia_wheel():
    creatures = Creature.objects.filter(chronicle=chronicle.acronym).exclude(mythic=True).exclude(ghost=True).order_by('-faction','display_pole')
    for creature in creatures:
        creature.need_fix = True
        creature.save()
    wyrm_list = []
    weaver_list = []
    wyld_list = []
    for c in creatures:
        creature_dict = {
            'id':c.id,
            'name':c.name,
            'player': c.player,
            'creature':c.creature,
            'family':c.family,
            'group':c.group,
            'groupspec':c.groupspec,
            'display_gauge':c.display_gauge,
            'display_pole':c.display_pole,
            'freebies': c.freebies,
            'auspice':c.auspice,
            'breed': c.breed,
            'rank': c.rank,
            'rid': c.rid,
            'position': c.position,
            'status': c.status
        }
        if (c.faction == 'Camarilla') or (c.faction=='Sabbat') or (c.faction=='Independant') or (c.faction=='Inconnu') or (c.faction=='Pentex'):
            wyrm_list.append(creature_dict)
        elif (c.faction=='Gaia'):
            wyld_list.append(creature_dict)
        else:
            weaver_list.append(creature_dict)
    d3js_data = {'weaver':weaver_list,'wyrm':wyrm_list,'wyld':wyld_list}
    all = json.dumps(d3js_data, indent=4, sort_keys=False)
    return all