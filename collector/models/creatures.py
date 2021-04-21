from django.db import models
from django.contrib import admin
from datetime import datetime
import json
from pdfrw import PdfReader, PdfWriter, PageMerge

import logging

logger = logging.Logger(__name__)

from collector.utils.wod_reference import get_current_chronicle


chronicle = get_current_chronicle()

bloodpool = {
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

GAROU_TALENTS = ["Alertness", "Athletics", "Brawl", "Dodge", "Empathy", "Expression", "Intimidation", "Primal-Urge",
                 "Streetwise", "Subterfuge"]
GAROU_SKILLS = ["Animal Ken", "Crafts", "Drive", "Etiquette", "Firearms", "Leadership", "Melee", "Performance",
                "Stealth", "Survival"]
GAROU_KNOWLEDGES = ["Computer", "Enigmas", "Investigation", "Law", "Linguistics", "Medicine", "Occult", "Politics",
                    "Rituals", "Science"]
GAROU_BACKGROUNDS = ["Allies", "Ancestors", "Contacts", "Fetish", "Kinfolk", "Mentor", "Pure Breed", "Resources",
                     "Rites", "Totem"]


class Creature(models.Model):
    class Meta:
        verbose_name = 'Creature'
        ordering = ['name']

    player = models.CharField(max_length=32, blank=True, default='')
    name = models.CharField(max_length=128, default='')
    nickname = models.CharField(max_length=128, blank=True, default='')
    primogen = models.BooleanField(default=False)
    mythic = models.BooleanField(default=False)
    family = models.CharField(max_length=32, blank=True, default='')
    rid = models.CharField(max_length=128, blank=True, default='')
    auspice = models.PositiveIntegerField(default=0)
    breed = models.PositiveIntegerField(default=0)
    domitor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='Domitor',
                                limit_choices_to={'chronicle': chronicle.acronym, 'creature': 'kindred'})
    group = models.CharField(max_length=128, blank=True, default='')
    groupspec = models.CharField(max_length=128, blank=True, default='')
    concept = models.CharField(max_length=128, blank=True, default='')
    age = models.PositiveIntegerField(default=0)
    faction = models.CharField(max_length=64, blank=True, default='')
    lastmod = models.DateTimeField(auto_now=True)
    chronicle = models.CharField(max_length=8, default='NYBN')
    creature = models.CharField(max_length=20, default='kindred')
    sex = models.BooleanField(default=False)

    display_gauge = models.PositiveIntegerField(default=0)
    display_pole = models.CharField(max_length=64, default='', blank=True)

    trueage = models.PositiveIntegerField(default=0)
    embrace = models.IntegerField(default=0)
    finaldeath = models.IntegerField(default=0)
    timeintorpor = models.PositiveIntegerField(default=0)
    picture = models.CharField(max_length=128, blank=True, default='')
    sire = models.CharField(max_length=64, blank=True, default='')
    rank = models.CharField(max_length=32, blank=True, default='')
    topic = models.TextField(max_length=1024, blank=True, default='')
    status = models.CharField(max_length=32, blank=True, default='OK')
    maj = models.PositiveIntegerField(default=0)
    freebiedif = models.IntegerField(default=0)
    freebies = models.IntegerField(default=0, blank=True)
    expectedfreebies = models.IntegerField(default=0)
    disciplinepoints = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    hidden = models.BooleanField(default=False)
    ghost = models.BooleanField(default=False)
    source = models.CharField(max_length=64, blank=True, default='zaffarelli')
    path = models.CharField(max_length=64, default='Humanity')
    nature = models.CharField(max_length=32, blank=True, default='')
    demeanor = models.CharField(max_length=32, blank=True, default='')
    condition = models.CharField(max_length=32, blank=True, default='OK')
    power1 = models.PositiveIntegerField(default=1)
    power2 = models.PositiveIntegerField(default=1)
    willpower = models.PositiveIntegerField(default=1)
    level0 = models.PositiveIntegerField(default=0)
    level1 = models.PositiveIntegerField(default=0)
    level2 = models.PositiveIntegerField(default=0)
    summary = models.TextField(default='', blank=True, max_length=2048)
    need_fix = models.BooleanField(default=False)

    total_physical = models.IntegerField(default=0)
    total_social = models.IntegerField(default=0)
    total_mental = models.IntegerField(default=0)
    total_talents = models.IntegerField(default=0)
    total_skills = models.IntegerField(default=0)
    total_knowledges = models.IntegerField(default=0)
    total_backgrounds = models.IntegerField(default=0)
    total_gifts = models.IntegerField(default=0)

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
            return self.family.replace(' Antitribu', '')
        else:
            return self.family

    @property
    def entrance(self):
        from collector.templatetags.wod_filters import as_generation, as_rank, as_breed, as_auspice, as_tribe_plural
        entrance = ''
        if self.creature == 'kindred':
            entrance = f'{as_generation(self.background3)} generation {self.family} of the {self.faction} ({self.group}).'
        elif self.creature == 'garou':
            entrance = f'{as_rank(self.rank)} {as_breed(self.breed)} {as_auspice(self.auspice)} of the  {as_tribe_plural(self.family)} ({self.group}).'
        return entrance

    def __str__(self):
        return "%s (%s %s of %s)" % (self.name, self.family, self.creature, self.faction)

    def fix_kindred(self):
        logger.info(f'Fixing kindred')
        freebies_by_age = {'0': 15, '50': 30, '100': 60, '150': 90, '200': 120, '250': 150, '300': 190, '400': 240,
                           '500': 280, '700': 320, '900': 360, '1100': 400, '1300': 425, '1500': 495, '1700': 565,
                           '2000': 645, '2500': 735, '3000': 825}
        # Embrace and Age
        condi = self.condition.split('-')
        if condi.count == 2:
            if condi[0] == 'DEAD':
                self.finaldeath == int(condi[1])
        if (int(self.age) > 0) and (int(self.trueage) >= int(self.age)):
            self.embrace = chronicle.era - (int(self.trueage) - int(self.age))
        # Activity as a vampire
        time_awake = int(self.trueage) - int(self.timeintorpor)
        for key, val in freebies_by_age.items():
            if int(key) <= time_awake:
                self.expectedfreebies = val
                # print("%s => %d"%(key,val))
            else:
                # print("out ---> %s => %d"%(key,val))
                break
        # Willpower
        if self.willpower < self.level2:
            self.willpower = self.level2
        # Humanity
        if self.power1 < self.level0 + self.level1:
            self.power1 = self.level0 + self.level1
        # Bloodpool
        self.power2 = bloodpool[13 - self.background3]

        self.display_gauge = (self.background3 *2) + int(self.trueage/50)
        self.display_pole = self.groupspec

    def fix_ghoul(self):
        if self.domitor:
            if self.family == '':
                self.family = self.domitor.family
                self.faction = self.domitor.faction
        self.expectedfreebies = int(((self.trueage - 10) / 10) * 3)
        self.display_gauge = self.domitor.display_gauge / 3

    def fix_mortal(self):
        self.trueage = self.age
        self.power2 = 5 + self.attribute2 + self.attribute3
        if self.willpower < 2:
            self.willpower = 2
        self.expectedfreebies = int(((self.age - 10) / 10) * 5)
        self.display_gauge = self.background7 + self.background9

    def fix_kinfolk(self):
        self.trueage = self.age
        self.expectedfreebies = int(((self.age - 10) / 10) * 5)

    def fix_fomori(self):
        self.display_gauge = self.power2
        self.expectedfreebies = int(((self.age - 10) / 10) * 5)

    def fix_bane(self):
        self.display_gauge = self.power2 * 2

    def fix_garou(self):
        self.trueage = self.age
        # Tribe
        if self.family in ["Bone Gnawer", "Children of Gaia", "Stargazer", "Wendigo"]:
            if self.willpower < 4:
                self.willpower = 4
        else:
            if self.willpower < 3:
                self.willpower = 3
        # Auspice
        if self.auspice == 0:
            # Initial Renown
            if self.level0 + self.level1 + self.level2 < 3:
                self.level0 = 1
                self.level1 = 1
                self.level2 = 1
            # Rank
            if self.level0 + self.level1 + self.level2 >= 25:
                self.rank = 5
            elif self.level0 + self.level1 + self.level2 >= 19:
                self.rank = 4
            elif self.level0 + self.level1 + self.level2 >= 13:
                self.rank = 3
            elif self.level0 + self.level1 + self.level2 >= 7:
                self.rank = 2
            elif self.level0 + self.level1 + self.level2 >= 3:
                self.rank = 1
            # Initial Rage
            if self.power1 < 1:
                self.power1 = 1
        elif self.auspice == 1:  # Theurge
            # Initial Renown
            if self.level2 < 3:
                self.level2 = 3
            # Rank
            if self.level0 >= 4 and self.level1 >= 9 and self.level2 >= 10:
                self.rank = 5
            elif self.level0 >= 4 and self.level1 >= 2 and self.level2 >= 9:
                self.rank = 4
            elif self.level0 >= 2 and self.level1 >= 1 and self.level2 >= 7:
                self.rank = 3
            elif self.level0 >= 1 and self.level1 >= 0 and self.level2 >= 5:
                self.rank = 2
            elif self.level0 >= 0 and self.level1 >= 0 and self.level2 >= 3:
                self.rank = 1
            # Initial Rage
            if self.power1 < 2:
                self.power1 = 2
        elif self.auspice == 2:  # Philodox
            # Initial Renown
            if self.level1 < 3:
                self.level1 = 3
            # Initial Rage
            if self.power1 < 3:
                self.power1 = 3
            # Rank
            if self.level0 >= 4 and self.level1 >= 10 and self.level2 >= 9:
                self.rank = 5
            elif self.level0 >= 3 and self.level1 >= 8 and self.level2 >= 4:
                self.rank = 4
            elif self.level0 >= 2 and self.level1 >= 6 and self.level2 >= 2:
                self.rank = 3
            elif self.level0 >= 1 and self.level1 >= 4 and self.level2 >= 1:
                self.rank = 2
            elif self.level0 >= 0 and self.level1 >= 3 and self.level2 >= 0:
                self.rank = 1
        elif self.auspice == 3:  # Galliard
            # Initial Renown
            if self.level0 < 2:
                self.level0 = 2
            if self.level2 < 1:
                self.level2 = 1
            # Initial Rage
            if self.power1 < 4:
                self.power1 = 4
            # Rank
            if self.level0 >= 9 and self.level1 >= 5 and self.level2 >= 9:
                self.rank = 5
            elif self.level0 >= 7 and self.level1 >= 2 and self.level2 >= 6:
                self.rank = 4
            elif self.level0 >= 4 and self.level1 >= 2 and self.level2 >= 4:
                self.rank = 3
            elif self.level0 >= 4 and self.level1 >= 2 and self.level2 >= 2:
                self.rank = 2
            elif self.level0 >= 2 and self.level1 >= 0 and self.level2 >= 1:
                self.rank = 1
        elif self.auspice == 4:  # Ahroun
            # Initial Renown
            if self.level0 < 2:
                self.level0 = 2
            if self.level1 < 1:
                self.level1 = 1
            # Initial Rage
            if self.power1 < 5:
                self.power1 = 5
            # Rank
            if self.level0 >= 10 and self.level1 >= 9 and self.level2 >= 4:
                self.rank = 5
            elif self.level0 >= 9 and self.level1 >= 5 and self.level2 >= 2:
                self.rank = 4
            elif self.level0 >= 6 and self.level1 >= 3 and self.level2 >= 1:
                self.rank = 3
            elif self.level0 >= 4 and self.level1 >= 1 and self.level2 >= 1:
                self.rank = 2
            elif self.level0 >= 2 and self.level1 >= 1 and self.level2 >= 0:
                self.rank = 1
        # Breed
        if self.breed == 0:  # Homid
            if self.power2 < 1:
                self.power2 = 1
        elif self.breed == 1:  # Metis
            if self.power2 < 3:
                self.power2 = 3
        elif self.breed == 2:  # Lupus
            if self.power2 < 5:
                self.power2 = 5
        self.display_gauge = ((self.auspice + self.power1 + self.power2) * self.rank + (
                    self.level0 / 2 + self.level1 + self.level2 * 2)) / 3
        if self.breed != 1:
            self.display_gauge += 1
        self.display_pole = self.sire

    def update_rid(self):
        s = self.name
        x = s.replace(' ', '_').replace("'", '').replace('é', 'e') \
            .replace('è', 'e').replace('ë', 'e').replace('â', 'a') \
            .replace('ô', 'o').replace('"', '').replace('ï', 'i') \
            .replace('à', 'a').replace('-', '').replace('ö', 'oe') \
            .replace('ä', 'ae').replace('ü', 'ue').replace('ß', 'ss')
        self.rid = x.lower()

    def fix(self):
        self.update_rid()
        logger.info(f'Fixing ............ [{self.name}]')
        # at:3/3/3 ab:7/5/3 b:3 w:2 f:15
        self.freebies = -((3 + 3 + 3 + 9) * 5 + (7 + 5 + 3) * 2 + 3 + 2 + 15)
        if self.creature == 'kindred':
            # at:7/5/3 ab:13/9/5 b:5 d:21 v:7 wh:10 f:15
            self.freebies = -((7 + 5 + 3 + 9) * 5 + (13 + 9 + 5) * 2 + 7 * 3 + (7 + 3) * 2 + 10 + 15)
            self.fix_kindred()
        elif self.creature == 'garou':
            # at:7/5/3 ab:13/9/5 b:5 g:21 rgw:16 f:15
            self.freebies = -((7 + 5 + 3 + 9) * 5 + (13 + 9 + 5) * 2 + 5 + 7 * 3 + 16 + 15)
            self.fix_garou()
        elif self.creature == 'ghoul':
            self.fix_ghoul()
        elif self.creature == 'kinfolk':
            # at:6/4/3 ab:11/7/4 b:5 w:3 f:21
            self.freebies -= 20
            self.freebies -= 14
            self.freebies -= 2
            self.freebies -= 3
            self.freebies -= 7
            self.fix_kinfolk()
        elif self.creature == 'fomori':
            self.fix_fomori()
        elif self.creature == 'bane':
            self.fix_bane()
        else:
            self.creature = 'mortal'
            self.fix_mortal()
        self.summary = f'Freebies: {self.freebies}'
        self.calculate_freebies()
        self.need_fix = False

    def val_as_dots(self, val):
        res = ''
        for x in range(5):
            if x < val:
                res += '●'
            else:
                res += '○'
        return res

    def extract_roster(self):
        lines = []
        lines.append(f'<strong>{self.name}</strong>')
        lines.append(f'<i>{self.entrance}</i>')
        lines.append(f'Concept: {self.concept}<BR/>Age: {self.age} yo ({self.trueage} yo)')
        lines.append(f'Nature: {self.nature}<BR/>Demeanor: {self.demeanor}')

        lines.append(f'<b>Attributes</b> <small>({self.total_physical}/{self.total_social}/{self.total_mental})</small>:')
        lines.append(f'Strength {self.attribute0}, Dexterity {self.attribute1}, Stamina {self.attribute2}')
        lines.append(f'Charisma {self.attribute3}, Manipulation {self.attribute4}, Appearance {self.attribute5}')
        lines.append(f'Perception {self.attribute6}, Intelligence {self.attribute7}, Wits {self.attribute8}')

        lines.append(f'<b>Abilities</b> <small>({self.total_talents}/{self.total_skills}/{self.total_knowledges})</small>:')

        # lines.append(f'<b>Attributes</b> ({self.total_physical})/{self.total_social})/({self.total_mental})')
        #
        #
        #     f'Strength\t{self.val_as_dots(self.attribute0)}\tCharisma\t{self.val_as_dots(self.attribute3)}\tPerception\t{self.val_as_dots(self.attribute6)}\n')
        # lines.append(
        #     f'Dexterity\t{self.val_as_dots(self.attribute1)}\tManipulation\t{self.val_as_dots(self.attribute4)}\tIntelligence\t{self.val_as_dots(self.attribute7)}\n')
        # lines.append(
        #     f'Stamina\t{self.val_as_dots(self.attribute2)}\tAppearance\t{self.val_as_dots(self.attribute5)}\tWits\t{self.val_as_dots(self.attribute8)}\n')
        # lines.append(
        #     f'Talents\t({self.total_talents})\tSkills\t({self.total_skills})\tKnowledges\t({self.total_knowledges})\t\n')
        # for n in range(10):
        #     lines.append(
        #         f'{GAROU_TALENTS[n]}\t{self.val_as_dots(getattr(self, f"talent{n}"))}\t{GAROU_SKILLS[n]}\t{self.val_as_dots(getattr(self, f"skill{n}"))}\t{GAROU_KNOWLEDGES[n]}\t{self.val_as_dots(getattr(self, f"knowledge{n}"))}\n')
        # blines = []
        # for n in range(10):
        #     if getattr(self, f"background{n}") > 0:
        #         blines.append(f'{GAROU_BACKGROUNDS[n]} ({getattr(self, f"background{n}")})')
        # lines.append(f'Backgrounds: {", ".join(blines)}.')
        # glines = []
        # for n in range(20):
        #     if getattr(self, f"gift{n}"):
        #         glines.append(f'{getattr(self, f"gift{n}")}')
        # lines.append(f'Gifts: {", ".join(glines)}.<BR/>')
        return "<BR/>".join(lines)


    def extract_raw(self):
        # filename = f'./raw/{self.rid}.txt'
        lines = []
        lines.append(f'{self.name}\n')
        lines.append(f'Nature\t\t{self.nature}\tDemeanor\t{self.demeanor}\n')
        lines.append(f'Concept\t\t{self.concept}\tAge\t{self.age}\n')
        lines.append(
            f'Physical\t({self.total_physical})\tSocial\t({self.total_social})\tMental\t({self.total_mental})\n')
        lines.append(
            f'Strength\t{self.val_as_dots(self.attribute0)}\tCharisma\t{self.val_as_dots(self.attribute3)}\tPerception\t{self.val_as_dots(self.attribute6)}\n')
        lines.append(
            f'Dexterity\t{self.val_as_dots(self.attribute1)}\tManipulation\t{self.val_as_dots(self.attribute4)}\tIntelligence\t{self.val_as_dots(self.attribute7)}\n')
        lines.append(
            f'Stamina\t{self.val_as_dots(self.attribute2)}\tAppearance\t{self.val_as_dots(self.attribute5)}\tWits\t{self.val_as_dots(self.attribute8)}\n')
        lines.append(
            f'Talents\t({self.total_talents})\tSkills\t({self.total_skills})\tKnowledges\t({self.total_knowledges})\t\n')
        for n in range(10):
            lines.append(
                f'{GAROU_TALENTS[n]}\t{self.val_as_dots(getattr(self, f"talent{n}"))}\t{GAROU_SKILLS[n]}\t{self.val_as_dots(getattr(self, f"skill{n}"))}\t{GAROU_KNOWLEDGES[n]}\t{self.val_as_dots(getattr(self, f"knowledge{n}"))}\n')
        blines = []
        for n in range(10):
            if getattr(self, f"background{n}") > 0:
                blines.append(f'{GAROU_BACKGROUNDS[n]} ({getattr(self, f"background{n}")})')
        lines.append(f'Backgrounds: {", ".join(blines)}.\n')
        glines = []
        for n in range(20):
            if getattr(self, f"gift{n}"):
                glines.append(f'{getattr(self, f"gift{n}")}')
        lines.append(f'Gifts: {", ".join(glines)}.\n')
        # f = open(filename, 'w')
        # if f:
        #     f.writelines(lines)
        #     f.close()
        return "".join(lines)

    def calculate_freebies(self):
        # Attributes
        self.total_physical = -3
        self.total_social = -3
        self.total_mental = -3
        for n in range(3):
            p = getattr(self, 'attribute%d' % (n))
            s = getattr(self, 'attribute%d' % (n + 3))
            m = getattr(self, 'attribute%d' % (n + 6))
            self.freebies += (p + s + m) * 5
            self.total_physical += p
            self.total_social += s
            self.total_mental += m
        # Abilities
        self.total_talents = 0
        self.total_skills = 0
        self.total_knowledges = 0
        for n in range(10):
            t = getattr(self, 'talent%d' % (n))
            s = getattr(self, 'skill%d' % (n))
            k = getattr(self, 'knowledge%d' % (n))
            self.freebies += (t + s + k) * 2
            self.total_talents += t
            self.total_skills += s
            self.total_knowledges += k
        # Backgrounds
        self.total_backgrounds = 0
        for n in range(10):
            b = getattr(self, 'background%d' % (n))
            self.freebies += b * 1
            self.total_backgrounds += b
        # Merits & Flaws
        for n in range(10):
            merit = getattr(self, 'merit%d' % (n))
            if merit != '':
                self.freebies += int(merit.split('(')[1].replace('(', '').replace(')', ''))
            flaw = getattr(self, 'flaw%d' % (n))
            if flaw != '':
                self.freebies -= int(flaw.split('(')[1].replace('(', '').replace(')', ''))
        # Gifts/Disciplines
        self.total_gifts = 0
        self.disciplinepoints = 0
        for n in range(20):
            discipline = getattr(self, 'gift%d' % (n))
            if discipline != '':
                self.disciplinepoints += int(discipline.split('(')[1].replace('(', '').replace(')', ''))
        self.total_gifts = self.disciplinepoints
        self.freebies += self.total_gifts * 7
        # willpower, powers and levels
        if self.creature == "kindred":
            # Virtues
            for n in range(3):
                self.freebies += getattr(self, 'level%d' % (n)) * 2
            # power2 doesn't has sense for a kindred = bloodpoints
            # power1 + willpower are at least sum(virtues)/2 for a kindred
        elif self.creature == "garou":
            # A garou will have virtual 16 points as attributions to power1 (rage 4), power2(gnosis 4) and willpower (4)
            self.freebies += getattr(self, 'power2') * 2
        else:
            pass  # power 2 doesn't has sense for a mortal
        self.freebies += getattr(self, 'power1') * 1  # Rage or Humanity
        self.freebies += getattr(self, 'willpower') * 1  # Willpower

        self.freebiesdif = self.expectedfreebies - self.freebies
        if self.freebiesdif == 0:
            self.status = 'OK'
        elif self.freebiesdif < 0:
            self.status = 'UNBALANCED'
        else:
            self.status = 'OK+'

        # Sort disciplines
        disciplines = []
        for x in range(15):
            disciplines.append(getattr(self, "gift%d" % (x)))
        disciplines = filter(None, disciplines)

        x = 0
        for disc in disciplines:
            setattr(self, "gift%d" % (x), disc)
            x += 1

        if self.creature == 'kinfolk':
            if self.freebies > 0:
                self.display_gauge = self.freebies / 5
            else:
                self.display_gauge = 1

    def json_str(self):
        sire = ''
        if self.domitor:
            sire = self.domitor.name
        # else:
        #     if self.sire != '':
        #         sire = self.sire
        return {'name': self.name, 'clan': self.family, 'condition': self.condition, 'status': self.status,
                'sire': sire, 'generation': (13 - self.background3),
                'ghost': self.ghost, 'faction': self.faction, 'id': self.id, 'children': []}

    def find_lineage(self, lockup=False):
        """ Find the full lineage for this character
        """
        lineage = self.json_str()
        infans = Creature.objects.filter(creature='kindred', sire=self.name)
        if infans:
            for childer in infans:
                if childer.ghost or childer.mythic:
                    lineage['children'].append(childer.find_lineage(True))
                else:
                    if childer.chronicle == chronicle.acronym:
                        lineage['children'].append(childer.find_lineage(True))
        return lineage

    @property
    def generation(self):
        if self.creature == 'kindred':
            return 13 - self.background3
        else:
            return 0


def refix(modeladmin, request, queryset):
    for creature in queryset:
        creature.need_fix = True
        creature.save()
    short_description = 'Fix creature'

def push_to_RAM(modeladmin, request, queryset):
    for creature in queryset:
        creature.chronicle = 'RAM'
        creature.need_fix = True
        creature.save()
    short_description = 'Push to Rage Across Munich'

def push_to_MBN(modeladmin, request, queryset):
    for creature in queryset:
        creature.chronicle = 'MBN'
        creature.need_fix = True
        creature.save()
    short_description = 'Push to Munich By Night'


class CreatureAdmin(admin.ModelAdmin):
    list_display = [  # 'domitor',
        'name', 'rid', 'family', 'display_gauge', 'display_pole', 'freebies', 'concept', 'groupspec', 'faction', 'sire',
        'domitor', 'condition',
        'status', 'embrace', 'finaldeath',
        'age', 'source', 'generation']
    ordering = ['name', 'group', 'creature']
    actions = [refix, push_to_RAM, push_to_MBN]
    list_filter = ['chronicle', 'group', 'groupspec', 'faction', 'family', 'creature']
    search_fields = ['name']
