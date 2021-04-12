"""
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

"""

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from collector.models.creatures import Creature
from django.core.paginator import Paginator
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from collector.templatetags.wod_filters import as_bullets
from collector.utils.kindred_stuff import build_per_primogen
from collector.utils.wod_reference import get_current_chronicle
chronicle = get_current_chronicle()


def index(request):
    context = {'data': build_per_primogen() }
    return render(request, 'collector/index.html', context=context)


def get_list(request, pid):
    """ Update the list of characters on the page
    """
    if request.is_ajax:
        creature_items = Creature.objects.all().filter(chronicle=chronicle.acronym).order_by('groupspec','auspice','name').exclude(ghost=True)
        paginator = Paginator(creature_items, 25)
        creature_items = paginator.get_page(pid)
        context = {'creature_items': creature_items}
        template = get_template('collector/list.html')
        html = template.render(context)
        return HttpResponse(html, content_type='text/html')
    else:
        Http404


@csrf_exempt
def updown(request):
    """ Touching skills to edit them in the view
    """
    if request.is_ajax():
        answer = 'error'
        if request.method == 'POST':
            answer = {}
            aid = int(request.POST.get('id'))
            afield = request.POST.get('field')
            aoffset = int(request.POST.get('offset'))
            # print("%d %s %d"%(aid,afield,aoffset))
            item = get_object_or_404(Creature, id=aid)
            if hasattr(item, afield):
                current_val = getattr(item, afield, 'Oops, nothing found')
                # print("item.field=%s"%(getattr(item,afield,'Oops, nothing found')))
                new_val = int(current_val) + int(aoffset)
                setattr(item, afield, new_val)
                item.need_fix = True
                item.save()
                x = as_bullets(getattr(item, afield))
                answer['freebiedif'] = item.freebiedif
            else:
                x = '<b>ERROR!</b>'
            answer['new_value'] = x
        return JsonResponse(answer)
    return Http404


@csrf_exempt
def userinput(request):
    """ Setting value from userinput
    """
    if request.is_ajax():
        answer = 'error'
        if request.method == 'POST':
            answer = {}
            aid = int(request.POST.get('id'))
            afield = request.POST.get('field')
            avalue = request.POST.get('value')
            item = get_object_or_404(Creature, id=aid)
            if hasattr(item, afield):
                # current_val = getattr(item,afield,'Oops, nothing found')
                # print("item.field=%s"%(getattr(item,afield,'Oops, nothing found')))
                # new_val = int(current_val)+int(aoffset)
                setattr(item, afield, avalue)
                item.need_fix = True
                item.save()
                x = avalue
                answer['freebiedif'] = item.freebiedif
            else:
                x = '<b>ERROR!</b>'
            answer['new_value'] = x
        return JsonResponse(answer)
    return Http404


def update_lineage(request):
    """ Check Caine Lineage
    """
    answer = {}#build_per_primogen()
    return JsonResponse(answer)

@csrf_exempt
def add_creature(request):
    """ Add creature to the current chronicle
    """
    if request.is_ajax:
        slug = request.POST['creature']
    chronicle = get_current_chronicle()
    item = Creature()
    item.name = " ".join(slug.split("-"))
    item.chronicle = chronicle.acronym
    item.creature = chronicle.main_creature
    item.source = 'zaffarelli'
    item.ghost = False
    item.save()
    context = {'answer':'creature added'}
    return JsonResponse(context)


def change_chronicle(request,slug=''):
    from wod_reference import set_chronicle
    if not slug:
        set_chronicle('none')
    else:
        set_chronicle(slug)
    return HttpResponse(status=204)
