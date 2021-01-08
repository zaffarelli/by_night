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
from collector.utils.kindred_stuff import check_caine_roots
from collector.utils.wod_reference import get_current_chronicle
chronicle = get_current_chronicle()

def index(request):
    """ The basic page for the application
    """
    return render(request, 'collector/index.html')


def get_list(request, pid):
    """ Update the list of characters on the page
    """
    if request.is_ajax:
        creature_items = Creature.objects.all().filter(chronicle=chronicle.acronym).order_by('name').exclude(ghost=True)
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
    answer = check_caine_roots()
    return JsonResponse(answer)
