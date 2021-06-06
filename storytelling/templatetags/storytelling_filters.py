from django import template
import re
import string


register = template.Library()






@register.filter(name='as_bullets')
def as_bullets(value, options=''):
    """ Change int value to list of bullet (Mark Rein*Hagen like)
    """
    if options == '':
        max = 10
    else:
        tokens = options.split(',')
        max = int(tokens[0])
    one = '<i class="fas fa-circle fa-xs" title="%d"></i>'%(value)
    blank = '<i class="fas fa-circle fa-xs blank" title="%d"></i>'%(value)
    x = 0
    res = ''
    while x < max:
        if x < int(value):
            res += one
        else:
            res += blank
        if (x+1) % 10 == 0:
            res += '<br/>'
        elif (x+1) % 5 == 0:
            res += '&nbsp;'
        x += 1
    return res


@register.filter(name='param_stack')
def param_stack(x_trait, x_id=''):
    return x_trait, x_id


@register.filter(name='as_entry')
def as_entry(stack, x_field=''):
    """ Display table lines as editable disciplines """
    x_trait, x_id = stack
    text = ""
    val = 0
    # tokens = x_trait.split('(')
    # if len(tokens) > 0:
    #     text = tokens[0]
    #     if len(tokens) > 1:
    #         val = int(tokens[1].replace('(','').replace(')',''))
    # if x_field != "":
    res = "<tr><th>%s</th><td class='editable userinput' id='%s__%s'>%s</td></tr>" % (x_field, x_id, x_field,x_trait)
    # else:
    # res = "<th>%s</th><td>%s</td>"%(text,as_bullets(val))
    return res


@register.filter(name='as_stat_name')
def as_stat_name(stack, x_field=''):
    x_creature, x_id = stack
    value = STATS_NAMES[str(x_creature)][x_field + 's'][int(x_id)]
    return value.title()


@register.filter(name='as_editable_updown')
def as_editable_updown(value, options=''):
    keys = options.split(',')
    aid = int(keys[0])
    afield = keys[1]
    res = "<td class='editable updown' id='%d_%s'>"%(aid,afield)
    return res

