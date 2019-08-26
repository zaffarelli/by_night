from collector.models.creatures import Creature
import json


print("=> Removing Ghosts with no infans")      
all = Creature.objects.filter(name__contains='Unknown')
for x in all:
  x.ghost = True
  x.save()
  infans = Creature.objects.filter(sire=x.name)
  if infans is None:
    print(" ooo-> Deleting %s"%(x.name))      
    x.delete()
  if x.background3 >= 10:
    print(" oxo-> Deleting %s"%(x.name))      
    x.delete()

print("Checking orphans")
all = Creature.objects.filter(sire__contains='Unknown')
for x in all:
  sire = Creature.objects.filter(name=x.sire).first()
  if sire is None:
    print(" oxr-> No sire found for %s (%s)"%(x.name,x.sire))      
    x.sire = ''
    x.save()

print("=> Creating Unknown Sires")      
all = Creature.objects.exclude(sire='').exclude(background3__gte=8)
for x in all:
  sire = Creature.objects.filter(creature='kindred',name=x.sire).first()
  if sire is None:
    y = Creature()
    y.background3 = x.background3+1
    y.family = x.family
    y.name = x.sire
    y.ghost = True
    y.save()
    print(" x--> %s [%s]"%(y.name,y.sire))    

print("=> Siring Ghosts")      
all_no_sire = Creature.objects.filter(creature='kindred',sire='',background3__lte=7)
ghost_sires = {}
for n in all_no_sire:
  str = "Unknown %dth generation %s"%(13-(n.background3+1),n.root_family())
  grandsire= "Unknown %dth generation %s"%(13-(n.background3+2),n.root_family())
  if (n.background3+2 == 10):
    if n.root_family() in ['Toreador','Daughter of Cacophony'] :
      grandsire = 'Arikel'
    elif n.root_family() == 'Malkavian':
      grandsire = 'Malkav'
    elif n.root_family() == 'Salubri':
      grandsire = 'Saulot'
    elif n.root_family() == 'Gangrel':
      grandsire = 'Ennoia'
    elif n.root_family() == 'Ventrue':
      grandsire = 'Ventru'
    elif n.root_family() == 'Cappadocian':
      grandsire = 'Cappadocius'
    elif n.root_family() == 'Nosferatu':
      grandsire = 'Absimiliard'
    elif n.root_family() == 'Ravnos':
      grandsire = 'Dracian'
    elif n.root_family() == 'Setite':
      grandsire = 'Set'
    elif n.root_family() == 'Assamite':
      grandsire = 'Haqim'
    elif n.root_family() in ['Lasombra','Kiasyd']:
      grandsire = 'Lasombra'
    elif n.root_family() == 'Tzimisce':
      grandsire = 'The Eldest'
    elif n.root_family() == 'Brujah':
      grandsire = 'Brujah'      
  elif (n.background3+2 == 9):
    if n.root_family() == 'Giovanni':
      grandsire = 'Augustus Giovanni'
    elif n.root_family() == 'Tremere':
      grandsire = 'Tremere'
    if n.root_family() == 'Brujah':
      grandsire = 'Troile'      
  j = {"ghost":True,"family":n.root_family(),"background3":n.background3+1,"name":str,"sire":grandsire}    
  ghost_sires[str] = j
  n.sire = str
  n.save()  
  print(json.dumps(ghost_sires,indent=2))

print("=> Creating Linked Ghosts")  
for key in ghost_sires:
  gs = ghost_sires[key]
  print(" ----> Dealing with ghost %s"%(gs['name']))
  f = Creature.objects.filter(name=gs['name']).first()
  if f is None:
    t = Creature()
    t.name = gs['name']
    t.background3 = gs['background3']
    t.family = gs['family']
    t.ghost = gs['ghost']
    t.sire = gs['sire']
    t.save()
    print(" --> Adding ghost %s"%(t.name))

