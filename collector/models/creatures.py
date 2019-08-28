'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import json

bloodpool ={
  13: 10,
  12: 11,
  11: 12,
  10: 13,
  9: 14,
  8: 15,
  7: 20,
  6: 30,
  5: 50,
  4: 70,
  3: 100,
  2: 100,
  1: 100,
}

class Creature(models.Model):
  player = models.CharField(max_length=32, blank=True, default='')
  name  = models.CharField(max_length=128, default='')
  nickname  = models.CharField(max_length=128, blank=True, default='')
  family = models.CharField(max_length=32, blank=True, default='')
  auspice = models.PositiveIntegerField(default=0)
  breed = models.PositiveIntegerField(default=0)
  group  = models.CharField(max_length=128, blank=True,default='')
  groupspec = models.CharField(max_length=128, blank=True,default='')
  concept = models.CharField(max_length=128, blank=True,default='') 
  age = models.PositiveIntegerField(default=0)
  faction = models.CharField(max_length=64,blank=True,default='')
  lastmod = models.DateTimeField(auto_now=True)
  chronicle = models.CharField(max_length=8, default='NYBN')
  creature = models.CharField(max_length=20, default='kindred')
  sex = models.BooleanField(default = False)
  trueage = models.PositiveIntegerField(default=0)
  embrace = models.IntegerField(default=0)
  finaldeath = models.IntegerField(default=0)
  timeintorpor = models.PositiveIntegerField(default=0)  
  picture = models.CharField(max_length=128, blank=True,default='')
  sire = models.CharField(max_length=64, blank=True,default='')
  path = models.CharField(max_length=64, default='Humanity')
  nature = models.CharField(max_length=32, blank=True,default='')
  demeanor = models.CharField(max_length=32, blank=True,default='')
  condition = models.CharField(max_length=32, blank=True,default='OK')
  power1 = models.PositiveIntegerField(default=1)
  power2 = models.PositiveIntegerField(default=1)
  willpower = models.PositiveIntegerField(default=1)
  level0 = models.PositiveIntegerField(default=0)
  level1 = models.PositiveIntegerField(default=0)
  level2 = models.PositiveIntegerField(default=0)
  rank  = models.CharField(max_length=32, blank=True,default='')
  topic  = models.TextField(max_length=1024, blank=True,default='')
  status  = models.CharField(max_length=32, blank=True, default='OK')
  maj = models.PositiveIntegerField(default=0)
  freebiedif = models.IntegerField(default=0)
  expectedfreebies = models.IntegerField(default=0)
  disciplinepoints = models.IntegerField(default=0)
  experience = models.IntegerField(default=0)
  hidden = models.BooleanField(default=False)
  ghost = models.BooleanField(default=False)
  source = models.CharField(max_length=64, blank=True,default='Great Quail')
  attribute0 = models.PositiveIntegerField(default=1)
  attribute1 = models.PositiveIntegerField(default=1)
  attribute2 = models.PositiveIntegerField(default=1)
  attribute3 = models.PositiveIntegerField(default=1)
  attribute4 = models.PositiveIntegerField(default=1)
  attribute5 = models.PositiveIntegerField(default=1)
  attribute6 = models.PositiveIntegerField(default=1)
  attribute7 = models.PositiveIntegerField(default=1)
  attribute8 = models.PositiveIntegerField(default=1)
  talent0 = models.PositiveIntegerField(default=0)
  talent1 = models.PositiveIntegerField(default=0)
  talent2 = models.PositiveIntegerField(default=0)
  talent3 = models.PositiveIntegerField(default=0)
  talent4 = models.PositiveIntegerField(default=0)
  talent5 = models.PositiveIntegerField(default=0)
  talent6 = models.PositiveIntegerField(default=0)
  talent7 = models.PositiveIntegerField(default=0)
  talent8 = models.PositiveIntegerField(default=0)
  talent9 = models.PositiveIntegerField(default=0)
  skill0 = models.PositiveIntegerField(default=0)
  skill1 = models.PositiveIntegerField(default=0)
  skill2 = models.PositiveIntegerField(default=0)
  skill3 = models.PositiveIntegerField(default=0)
  skill4 = models.PositiveIntegerField(default=0)
  skill5 = models.PositiveIntegerField(default=0)
  skill6 = models.PositiveIntegerField(default=0)
  skill7 = models.PositiveIntegerField(default=0)
  skill8 = models.PositiveIntegerField(default=0)
  skill9 = models.PositiveIntegerField(default=0)
  knowledge0 = models.PositiveIntegerField(default=0)
  knowledge1 = models.PositiveIntegerField(default=0)
  knowledge2 = models.PositiveIntegerField(default=0)
  knowledge3 = models.PositiveIntegerField(default=0)
  knowledge4 = models.PositiveIntegerField(default=0)
  knowledge5 = models.PositiveIntegerField(default=0)
  knowledge6 = models.PositiveIntegerField(default=0)
  knowledge7 = models.PositiveIntegerField(default=0)
  knowledge8 = models.PositiveIntegerField(default=0)
  knowledge9 = models.PositiveIntegerField(default=0)
  background0 = models.PositiveIntegerField(default=0)
  background1 = models.PositiveIntegerField(default=0)
  background2 = models.PositiveIntegerField(default=0)
  background3 = models.PositiveIntegerField(default=0)
  background4 = models.PositiveIntegerField(default=0)
  background5 = models.PositiveIntegerField(default=0)
  background6 = models.PositiveIntegerField(default=0)
  background7 = models.PositiveIntegerField(default=0)
  background8 = models.PositiveIntegerField(default=0)
  background9 = models.PositiveIntegerField(default=0)
  gift0 = models.CharField(max_length=64, blank=True, default='')
  gift1 = models.CharField(max_length=64, blank=True, default='')
  gift2 = models.CharField(max_length=64, blank=True, default='')
  gift3 = models.CharField(max_length=64, blank=True, default='')
  gift4 = models.CharField(max_length=64, blank=True, default='')
  gift5 = models.CharField(max_length=64, blank=True, default='')
  gift6 = models.CharField(max_length=64, blank=True, default='')
  gift7 = models.CharField(max_length=64, blank=True, default='')
  gift8 = models.CharField(max_length=64, blank=True, default='')
  gift9 = models.CharField(max_length=64, blank=True, default='')
  gift10 = models.CharField(max_length=64, blank=True, default='')
  gift11 = models.CharField(max_length=64, blank=True, default='')
  gift12 = models.CharField(max_length=64, blank=True, default='')
  gift13 = models.CharField(max_length=64, blank=True, default='')
  gift14 = models.CharField(max_length=64, blank=True, default='')
  gift15 = models.CharField(max_length=64, blank=True, default='')
  gift16 = models.CharField(max_length=64, blank=True, default='')
  gift17 = models.CharField(max_length=64, blank=True, default='')
  gift18 = models.CharField(max_length=64, blank=True, default='')
  gift19 = models.CharField(max_length=64, blank=True, default='')
  merit0 = models.CharField(max_length=64, blank=True, default='')
  merit1 = models.CharField(max_length=64, blank=True, default='')
  merit2 = models.CharField(max_length=64, blank=True, default='')
  merit3 = models.CharField(max_length=64, blank=True, default='')
  merit4 = models.CharField(max_length=64, blank=True, default='')
  merit5 = models.CharField(max_length=64, blank=True, default='')
  merit6 = models.CharField(max_length=64, blank=True, default='')
  merit7 = models.CharField(max_length=64, blank=True, default='')
  merit8 = models.CharField(max_length=64, blank=True, default='')
  merit9 = models.CharField(max_length=64, blank=True, default='')
  flaw0 = models.CharField(max_length=64, blank=True, default='')
  flaw1 = models.CharField(max_length=64, blank=True, default='')
  flaw2 = models.CharField(max_length=64, blank=True, default='')
  flaw3 = models.CharField(max_length=64, blank=True, default='')
  flaw4 = models.CharField(max_length=64, blank=True, default='')
  flaw5 = models.CharField(max_length=64, blank=True, default='')
  flaw6 = models.CharField(max_length=64, blank=True, default='')
  flaw7 = models.CharField(max_length=64, blank=True, default='')
  flaw8 = models.CharField(max_length=64, blank=True, default='')
  flaw9 = models.CharField(max_length=64, blank=True, default='')
  rite0 = models.CharField(max_length=64, blank=True, default='')
  rite1 = models.CharField(max_length=64, blank=True, default='')
  rite2 = models.CharField(max_length=64, blank=True, default='')
  rite3 = models.CharField(max_length=64, blank=True, default='')
  rite4 = models.CharField(max_length=64, blank=True, default='')
  rite5 = models.CharField(max_length=64, blank=True, default='')
  rite6 = models.CharField(max_length=64, blank=True, default='')
  rite7 = models.CharField(max_length=64, blank=True, default='')
  rite8 = models.CharField(max_length=64, blank=True, default='')
  rite9 = models.CharField(max_length=64, blank=True, default='')
  rite10 = models.CharField(max_length=64, blank=True, default='')
  rite11 = models.CharField(max_length=64, blank=True, default='')
  rite12 = models.CharField(max_length=64, blank=True, default='')
  rite13 = models.CharField(max_length=64, blank=True, default='')
  rite14 = models.CharField(max_length=64, blank=True, default='')
  rite15 = models.CharField(max_length=64, blank=True, default='')
  rite16 = models.CharField(max_length=64, blank=True, default='')
  rite17 = models.CharField(max_length=64, blank=True, default='')
  rite18 = models.CharField(max_length=64, blank=True, default='')
  rite19 = models.CharField(max_length=64, blank=True, default='')  

  def root_family(self):
    if self.creature == 'kindred':
      return self.family.replace(' Antitribu','')
    else:
      return self.family

  def __str__(self):
    return "%s (%s | %s | %s)"%(self.name, self.family, self.group, self.player)

  def fix(self):
    freebies_by_age = {'0': 15,'50':30,'100':60,'150':90,'200':120,'250':150,'300':190,'400':240,'500':280,'700':320,'900':360,'1100':400,'1300':425,'1500':495,'1700':565,'2000':645,'2500':735,'3000':825}
    # Embrace and Age
    if (int(self.age)>0) and (int(self.trueage)>=int(self.age)):
      self.embrace = 2006-(int(self.trueage)-int(self.age))
    # Activity as a vampire
    time_awake = int(self.trueage) - int(self.timeintorpor)
    for key,val in freebies_by_age.items():
      if int(key) <= time_awake:
        self.expectedfreebies = val
        #print("%s => %d"%(key,val))
      else:
        #print("out ---> %s => %d"%(key,val))
        break
        
    # Willpower
    if self.willpower < self.level2:
      self.willpower = self.level2
    # Humanity
    if self.power1 < self.level0+self.level1:
      self.power1 = self.level0+self.level1
    # Bloodpool
    self.power2 = bloodpool[13 - self.background3]
    # Current Freebies
    freebies = 0
    freebies -= 120 + 54 + 21 + 5 + 20 + 10 + 15 
    #print("freebies: %d"%(freebies))
    for n in range(9):
      freebies += getattr(self,'attribute%d'%(n))*5
    for n in range(10):
      freebies += getattr(self,'talent%d'%(n))*2
      freebies += getattr(self,'skill%d'%(n))*2
      freebies += getattr(self,'knowledge%d'%(n))*2
      freebies += getattr(self,'background%d'%(n))*1
    for n in range(3):
      freebies += getattr(self,'level%d'%(n))*2
    freebies += getattr(self,'power1')*1
    freebies += getattr(self,'willpower')*1
    for n in range(10):
      merit = getattr(self,'merit%d'%(n))
      if merit != '':
        freebies += int(merit.split('(')[1].replace('(','').replace(')',''))
      flaw = getattr(self,'flaw%d'%(n))
      if flaw != '':
        freebies -= int(flaw.split('(')[1].replace('(','').replace(')',''))
    self.disciplinepoints = 0
    for n in range(20):
      discipline = getattr(self,'gift%d'%(n))
      if discipline != '':
        self.disciplinepoints += int(discipline.split('(')[1].replace('(','').replace(')',''))    
    freebies += self.disciplinepoints*7    
    self.freebiedif = freebies
    # Sort disciplines
    disciplines = []
    for x in range(15):
      disciplines.append(getattr(self,"gift%d"%(x)))
    disciplines = filter(None, disciplines)
    #print(disciplines)
    x = 0
    for disc in disciplines:
      setattr(self,"gift%d"%(x),disc)
      x += 1
      #print(disc)
    # Lineage
    if self.creature=='kindred':
      self.find_lineage()

  def json_str(self):
    return {'name':self.name,'clan':self.family,'sire':self.sire,'generation':(13-self.background3),'ghost':self.ghost,'faction':self.faction,'id':self.id,'children':[]}    

  def find_lineage(self,lockup=False):
    """ Find the full lineage for this character """    
    # if lockup == False:
      # sire = Creature.objects.filter(name=self.sire).first()
      # print("--> n:%s s:[%s]"%(self.name,self.sire))
      # if sire:
        # lineage = sire.find_lineage(False)
    # print("***********")
    # print("==> n:%s s:[%s]"%(self.name,self.sire))
    lineage = self.json_str()
    infans = Creature.objects.filter(creature='kindred',sire=self.name)
    if infans:  
      for childer in infans:
        lineage['children'].append(childer.find_lineage(True))
    return lineage

    
    
    
@receiver(pre_save, sender=Creature, dispatch_uid='update_creature')
def update_creature(sender, instance, **kwargs):
  """ Before saving, fix() and  get_RID() for the character """
  instance.fix()
  
    

class CreatureAdmin(admin.ModelAdmin):
  list_display = ('name','family', 'faction', 'group', 'groupspec','condition','status','embrace','finaldeath','age','source')
  ordering = ['chronicle','name','group','creature']
