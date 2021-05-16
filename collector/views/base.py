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
import random

chronicle = get_current_chronicle()

def index(request):
    chronicles = []
    for c in Chronicle.objects.all():
        chronicles.append({'name': c.name, 'acronym': c.acronym, 'active': c == chronicle})
    context = {'chronicles': chronicles}
    return render(request, 'collector/index.html', context=context)


def change_chronicle(request, slug=''):
    if request.is_ajax:
        from collector.utils.wod_reference import set_chronicle
        set_chronicle(slug)
        chronicles = []
        for c in Chronicle.objects.all():
            chronicles.append({'name':c.name, 'acronym':c.acronym, 'active': c == chronicle})
        context_ch = {'c': chronicles}
        template_ch = get_template("collector/page/chronicles.html")
        html_ch = template_ch.render(context_ch)
        answer = {'chronicles': html_ch}
        return JsonResponse(answer)


def get_list(request, pid, slug):
    if request.is_ajax:
        if slug == 'sabbat':
            creature_items = Creature.objects.all().filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(faction='Sabbat', creature='kindred')
        elif slug == 'camarilla':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(faction='Camarilla',creature='kindred')
        elif slug == 'vtm':
            creature_items = Creature.objects.filter(chronicle=chronicle.acronym)\
                .order_by('name')\
                .exclude(ghost=True)\
                .filter(creature__in=['kindred','ghoul'])
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
        if slug is None:
            slug = 'adel_the_swift'
        c = Creature.objects.get(rid=slug)
        settings = {'version': 1.0, 'labels': STATS_NAMES[c.creature]  }
        crossover_sheet_context = {'settings': json.dumps(settings, sort_keys=True, indent=4), 'data': c.toJSON()}
        return JsonResponse(crossover_sheet_context)


def display_gaia_wheel(request):
    if request.is_ajax:
        gaia_wheel_context = {'data': build_gaia_wheel()}
        return JsonResponse(gaia_wheel_context)


def display_lineage(request, slug=None):
    if request.is_ajax:
        print(slug)
        if slug is None:
            data = build_per_primogen()
        else:
            print(slug)
            data = build_per_primogen(slug)
        lineage_context = {'data': data}
        return JsonResponse(lineage_context)

