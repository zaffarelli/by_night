'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django import template
import re
import string

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
  res = '<img class="clan_logo" src="http://localhost:8000/static/collector/clans/%s.webp"> '%(logo_str)
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

@register.filter(name='as_editable_updown')
def as_editable_updown(value, options=''):
  keys = options.split(',')
  aid = int(keys[0])
  afield = keys[1]
  res = "<td class='editable updown' id='%d_%s'>"%(aid,afield)
  return res
