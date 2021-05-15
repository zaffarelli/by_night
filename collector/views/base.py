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
        chronicles.append({'name':c.name, 'acronym':c.acronym, 'active':c == chronicle})
    context = { 'chronicles': chronicles }
    return render(request, 'collector/index.html', context=context)


def change_chronicle(request,slug=''):
    from collector.utils.wod_reference import set_chronicle
    set_chronicle(slug)
    chronicles = []
    for c in Chronicle.objects.all():
        chronicles.append({'name':c.name, 'acronym':c.acronym, 'active':c == chronicle})
    context_ch = {'c': chronicles}
    template_ch = get_template("collector/page/chronicles.html")
    html_ch = template_ch.render(context_ch)
    answer = {'chronicles': html_ch}
    return JsonResponse(answer)


def extract_raw(request,slug):
    found = Creature.objects.all().filter(rid=slug)
    if len(found) == 1:
        lines = found.first().extract_raw()
        return HttpResponse(lines, content_type='text/plain', charset="utf-16")
    return HttpResponse(status=204)


def extract_roster(request,slug):
    found = Creature.objects.all().filter(rid=slug)
    if len(found) == 1:
        lines = found.first().extract_roster()
        return HttpResponse(lines, content_type='text/html', charset="utf-16")
    return HttpResponse(status=204)


def extract_per_group(request,slug):
    grp_name = slug.replace('_', ' ')
    lines = []
    creatures = Creature.objects.all().filter(group=grp_name).order_by('groupspec')
    for creature in creatures:
        lines.append(creature.extract_roster())
    return HttpResponse(lines, content_type='text/html', charset="utf-16")


def extract_mechanics(request):
    all = Creature.objects.all().filter(creature="garou")
    stats_by_auspice = {
        '0': {'power1': 0, 'power2': 0, 'willpower': 0, 'cnt': 0},
        '1': {'power1': 0, 'power2': 0, 'willpower': 0, 'cnt': 0},
        '2': {'power1': 0, 'power2': 0, 'willpower': 0, 'cnt': 0},
        '3': {'power1': 0, 'power2': 0, 'willpower': 0, 'cnt': 0},
        '4': {'power1': 0, 'power2': 0, 'willpower': 0, 'cnt': 0},
    }

    all_known_gifts = []
    for c in all:
        x = f'{c.auspice}'
        stats_by_auspice[x]['power1'] += c.power1
        stats_by_auspice[x]['power2'] += c.power2
        stats_by_auspice[x]['willpower'] += c.willpower
        stats_by_auspice[x]['cnt'] += 1
        for n in range(10):
            gift = getattr(c, f'gift{n}')
            if gift:
                from collector.models.gifts import Gift
                gs = Gift.objects.filter(declaration=gift)
                if not len(gs):
                    go = Gift()
                    go.name = gift.split(' (')[0]
                    go.level = int(gift.split(' (')[1].split(')')[0])
                    go.fix()
                    go.save()

                if not gift.title() in all_known_gifts:
                    all_known_gifts.append(f'- {gift}')
    lines = "All known gifts:\n"
    all_known_gifts.sort()
    lines += "\n".join(all_known_gifts)
    all_kinfolks = []
    for c in all:
        num = 0
        kinfolk = c.value_of('kinfolk')
        if kinfolk == 1:
            num = 2
        elif kinfolk == 2:
            num = 5
        elif kinfolk == 3:
            num = 10
        elif kinfolk == 4:
            num = 20
        elif kinfolk == 5:
            num = 50
        my_kinfolk = []
        for n in range(num):
            my_kinfolk.append(f'- unknown #{n+1} ({c.name})')
        x = 0
        found_folks = Creature.objects.filter(creature='kinfolk',patron=c.name)
        for k in found_folks:
            my_kinfolk[x] = f'- {k.name} ({c.name})'
            x += 1
        for n in range(num):
            if my_kinfolk[n].startswith(f'- unknown #{n+1}'):
                nk = Creature()
                nk.faction = 'Gaia'
                nk.patron = c.name
                nk.creature = 'kinfolk'
                nk.name = f'NewKinfolk for {c.name} #{n+1}'
                nk.age = random.randrange(18,58)
                nk.need_fix = True
                nk.save()
        x = 0

        if len(my_kinfolk):
            all_kinfolks.append("\n".join(my_kinfolk))
    lines += "\nAll kinfolks:\n"
    lines += "\n".join(all_kinfolks)
    kinfolks = Creature.objects.filter(creature='kinfolk')
    for k in kinfolks:
        if k.condition == 'recalculate':
            k.randomize_kinfolk()
    lines += "\nPowers:\n"
    for a in range(5):
        x = f'{a}'
        stats_by_auspice[x]['power1'] /= stats_by_auspice[x]['cnt']
        stats_by_auspice[x]['power2'] /= stats_by_auspice[x]['cnt']
        stats_by_auspice[x]['willpower'] /= stats_by_auspice[x]['cnt']
        str = f'R:{round(stats_by_auspice[x]["power1"])} '
        str += f'G:{round(stats_by_auspice[x]["power2"])} '
        str += f'W:{round(stats_by_auspice[x]["willpower"])} '
        str += f'C:{stats_by_auspice[x]["cnt"]}\n'
        lines += str
    from collector.models.rites import Rite
    rites = Rite.objects.all()
    all_garous = Creature.objects.filter(creature='garou')
    for garou in all_garous:
        if garou.value_of("rites")>0:
            pass
    # all = Creature.objects.all()
    # for c in all:
    #     if c.domitor:
    #         c.new_domitor = c.domitor.name
    #         c.need_fix = True
    #         c.save()
    return HttpResponse(lines, content_type='text/plain', charset="utf-16")


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
        HttpResponse(status=204)


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


@csrf_exempt
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
    if slug is None:
        slug = 'adel_the_swift'
    c = Creature.objects.get(rid=slug)
    settings = {'version': 1.0, 'labels': STATS_NAMES[c.creature]  }
    crossover_sheet_context = {'settings': json.dumps(settings, sort_keys=True, indent=4), 'data': c.toJSON()}
    return JsonResponse(crossover_sheet_context)


def display_gaia_wheel(request):
    gaia_wheel_context = {'data': build_gaia_wheel()}
    return JsonResponse(gaia_wheel_context)


def display_lineage(request):
    lineage_context = {'data': build_per_primogen()}
    return JsonResponse(lineage_context)
