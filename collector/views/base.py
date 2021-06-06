from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from collector.models.creatures import Creature
from django.core.paginator import Paginator
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from collector.templatetags.wod_filters import as_bullets
from collector.utils.kindred_stuff import build_per_primogen, build_gaia_wheel
from collector.utils.wod_reference import get_current_chronicle
from collector.models.chronicles import Chronicle
from collector.utils.wod_reference import STATS_NAMES
import json
from collector.utils.wod_reference import FONTSET


chronicle = get_current_chronicle()


def prepare_index(request):
    chronicles = []
    players = []
    plist = Creature.objects.filter(chronicle=chronicle.acronym).exclude(player='')
    for p in plist:
        players.append({'name': p.name, 'rid': p.rid, 'player': p.player})
    print(players)
    for c in Chronicle.objects.all():
        chronicles.append({'name': c.name, 'acronym': c.acronym, 'active': c == chronicle})
    context = {'chronicles': chronicles, 'fontset': FONTSET, 'players': players}
    return context


def index(request):
    context = prepare_index(request)
    return render(request, 'collector/index.html', context=context)


def change_chronicle(request, slug=None):
    if request.is_ajax:
        from collector.utils.wod_reference import set_chronicle
        set_chronicle(slug)
        context = prepare_index(request)
        return render(request, 'collector/index.html', context=context)

def get_list(request, pid, slug):
    if request.is_ajax:
        if slug == 'sabbat':
            creature_items = Creature.objects.all().filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(faction='Sabbat', creature='kindred')
        elif slug == 'players':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(player='')
        elif slug == 'camarilla':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(faction='Camarilla',creature='kindred')
        elif slug == 'vtm':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(creature__in=['ghoul'])
        elif slug == 'wta':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(creature__in=['garou','kinfolk'])
        elif slug == 'mortals':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(creature__in=['mortal','ghoul','kinfolk','fomori'])
        elif slug == 'garou':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(creature__in=['garou'])
        elif slug == 'pentex':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(faction='Pentex',creature__in=['garou','kinfolk','fomori'])
        else:
            creature_items = Creature.objects.all().filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)
        paginator = Paginator(creature_items, 20)
        creature_items = paginator.get_page(pid)
        list_context = {'creature_items': creature_items}
        list_template = get_template('collector/list.html')
        list_html = list_template.render(list_context)
        answer = {
            'list': list_html,
        }
        return JsonResponse(answer)
    else:
        return HttpResponse(status=204)


@csrf_exempt
def updown(request):
    if request.is_ajax():
        answer = 'error'
        if request.method == 'POST':
            answer = {}
            rid = request.POST.get('id')
            field = request.POST.get('field')
            offset = int(request.POST.get('offset'))
            item = Creature.objects.get(rid=rid)
            if hasattr(item, field):
                current_val = getattr(item, field, 'Oops, nothing found')
                new_val = int(current_val) + int(offset)
                setattr(item, field, new_val)
                item.need_fix = True
                item.save()
                answer['new_value'] = as_bullets(getattr(item, field))
                answer['freebies'] = item.freebies
            else:
                answer['new_value'] = '<b>ERROR!</b>'
        return JsonResponse(answer)
    return Http404


@csrf_exempt
def userinput(request):
    if request.is_ajax():
        answer = 'error'
        if request.method == 'POST':
            answer = {}
            rid = request.POST.get('id')
            field = request.POST.get('field')
            value = request.POST.get('value')
            item = Creature.objects.get(rid=rid)
            if hasattr(item, field):
                setattr(item, field, value)
                item.need_fix = True
                item.save()
                answer['new_value'] = value
                answer['freebies'] = item.freebies
            else:
                answer['new_value'] = '<b>ERROR!</b>'
        return JsonResponse(answer)
    return HttpResponse(status=204)


def add_creature(request):
    if request.is_ajax:
        slug = request.POST['creature']
        chronicle = get_current_chronicle()
        item = Creature()
        item.name = " ".join(slug.split("-"))
        item.chronicle = chronicle.acronym
        item.creature = chronicle.main_creature
        item.source = 'zaffarelli'
        item.ghost = False
        item.need_fix = True
        item.save()
        context = {'answer': 'creature added'}
        return JsonResponse(context)
    else:
        return HttpResponse(status=204)

def display_crossover_sheet(request, slug=None):
    if request.is_ajax:
        chronicle = get_current_chronicle()
        if slug is None:
            slug = 'julius_von_blow'
        c = Creature.objects.get(rid=slug)

        if chronicle.acronym == 'BAV':
            scenario = "Bayerische Nächte"
            pre_title = 'Munich'
            post_title = "Oktoberfest, 2019"
        else:
            pre_title = 'World of Darkness'
            scenario = "NEW YORK CITY"
            post_title = "feat. Julius Von Blow"
        spe = c.get_specialities()
        shc = c.get_shortcuts()
        settings = {'version': 1.0, 'labels': STATS_NAMES[c.creature], 'pre_title': pre_title, 'scenario': scenario, 'post_title': post_title, 'fontset': FONTSET, 'specialities': spe, 'shortcuts': shc}
        crossover_sheet_context = {'settings': json.dumps(settings, sort_keys=True, indent=4), 'data': c.toJSON()}
        return JsonResponse(crossover_sheet_context)


def display_gaia_wheel(request):
    if request.is_ajax:
        gaia_wheel_context = {'data': build_gaia_wheel()}
        return JsonResponse(gaia_wheel_context)


def display_lineage(request, slug=None):
    if request.is_ajax:
        if slug is None:
            data = build_per_primogen()
        else:
            print(slug)
            data = build_per_primogen(slug)
        lineage_context = {'data': data}
        return JsonResponse(lineage_context)

