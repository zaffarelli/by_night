'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django import template
import re
import string
from collector.utils.wod_reference import STATS_NAMES

register = template.Library()


@register.filter(name='as_generation')
def as_generation(value):
  return "%dth"%(13-value)

@register.filter(name='prev')
def prev(value):
  return value-1

@register.filter(name='next')
def next(value):
  return value+1


@register.filter(name='modulo')
def modulo(num, val):
  return num % val

@register.filter(name='to_logo')
def modulo(val):
  logo_str = '_'.join(val.lower().split(' '))
  res = '<img src="/static/collector/clans/%s.webp"> '%(logo_str)
  return res

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
  while x<max:
    if x<int(value):
      res += one
    else:
      res += blank
    if (x+1) % 10 == 0:
      res += '<br/>'
    elif (x+1) % 5 == 0:
      res += '&nbsp;'
    x += 1
  return res

@register.filter(name='as_discipline')
def as_discipline(x_trait,x_id=0,x_field=''):
  """ Display table lines as editable disciplines """  
  text = ""
  val = 0
  tokens = x_trait.split('(')
  if len(tokens)>0:
    text = tokens[0]
    if len(tokens)>1:
      val = int(tokens[1].replace('(','').replace(')',''))
  #if x_field != "":
  #  res = "<th>%s</th><td class='editable userinput' id='%s_%s'>%s</td>" % (text,x_id,x_field,as_bullets(val))
  #else:
    res = "<th>%s</th><td>%s</td>"%(text,as_bullets(val))
  return res

@register.filter(name='param_stack')
def param_stack(x_trait, x_id=0):
  """ Parameters stacking """
  return x_trait, x_id

@register.filter(name='as_discipline2')
def as_discipline2(stack, x_field=''):
  """ Display table lines as editable disciplines """
  x_trait, x_id = stack
  text = ""
  val = 0
  tokens = x_trait.split('(')
  if len(tokens)>0:
    text = tokens[0]
    if len(tokens)>1:
      val = int(tokens[1].replace('(','').replace(')',''))
  if x_field != "":
    res = "<th>%s</th><td class='editable userinput' id='%s_%s'>%s</td>" % (text,x_id,x_field,as_bullets(val))
  else:
    res = "<th>%s</th><td>%s</td>"%(text,as_bullets(val))
  return res

""" <th>{{ c.creature|param_stack:9|as_stat_name:"talent"|safe }}</th> """
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


@register.filter(name='as_rank')
def as_rank(value):
  try:
    ranks = ['Cliath','Fostern','Adren','Athro','Elder']
    rank = ranks[int(value)-1]
  except:
    rank = 'none'
  return rank

@register.filter(name='as_breed')
def as_breed(value):
  try:
    breeds = ['Homid','Metis','Lupus']
    breed = breeds[int(value)]
  except:
    breed = 'none'
  return breed

@register.filter(name='as_auspice')
def as_auspice(value):
  try:
    auspices = ['Ragabash','Theurge','Philodox','Galliard','Ahroun']
    auspice = auspices[int(value)]
  except:
    auspice = 'none'
  return auspice

@register.filter(name='as_sex')
def as_sex(value):
  sex = 'Male'
  if value:
    sex = 'Female'
  return sex

@register.filter(name='as_tribe_plural')
def as_tribe_plural(value):
  plural = f'{value}s'
  if value == 'Get of Fenris':
    plural = 'Gets of Fenris'
  elif value == 'Child of Gaia':
    plural = 'Children of Gaia'
  elif value == 'Black Fury':
    plural = 'Black Furies'
  return plural

@register.filter(name='to_tribe_logo')
def to_tribe_logo(val):
  logo_str = '_'.join(val.lower().split(' '))
  res = '<img src="/static/collector/tribes/%s.webp"> '%(logo_str)
  return res


