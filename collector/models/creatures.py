from django.db import models
from django.contrib import admin
from datetime import datetime
import json
from pdfrw import PdfReader, PdfWriter, PageMerge
import logging
from collector.utils.wod_reference import get_current_chronicle, find_stat_property, STATS_NAMES

logger = logging.Logger(__name__)
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


def json_default(value):
    import datetime
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__


class Creature(models.Model):
    class Meta:
        verbose_name = 'Creature'
        ordering = ['name']

    player = models.CharField(max_length=32, blank=True, default='')
    name = models.CharField(max_length=128, default='')
    rid = models.CharField(max_length=128, blank=True, default='', primary_key=True)
    nickname = models.CharField(max_length=128, blank=True, default='')
    primogen = models.BooleanField(default=False)
    mythic = models.BooleanField(default=False)
    family = models.CharField(max_length=32, blank=True, default='')

    auspice = models.PositiveIntegerField(default=0)
    breed = models.PositiveIntegerField(default=0)
    domitor = models.CharField(max_length=128, blank=True, default='')
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
    patron = models.CharField(max_length=64, blank=True, default='')
    rank = models.CharField(max_length=32, blank=True, default='')
    topic = models.TextField(max_length=1024, blank=True, default='')
    status = models.CharField(max_length=32, blank=True, default='OK')
    position = models.CharField(max_length=64, blank=True, default='')
    maj = models.PositiveIntegerField(default=0)
    freebiedif = models.IntegerField(default=0)
    freebies = models.IntegerField(default=0, blank=True)
    expectedfreebies = models.IntegerField(default=0)
    disciplinepoints = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    extra = models.IntegerField(default=0)
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
    merit0 = models.CharField(max_length=64, blank=True, default='')
    merit1 = models.CharField(max_length=64, blank=True, default='')
    merit2 = models.CharField(max_length=64, blank=True, default='')
    merit3 = models.CharField(max_length=64, blank=True, default='')
    merit4 = models.CharField(max_length=64, blank=True, default='')
    flaw0 = models.CharField(max_length=64, blank=True, default='')
    flaw1 = models.CharField(max_length=64, blank=True, default='')
    flaw2 = models.CharField(max_length=64, blank=True, default='')
    flaw3 = models.CharField(max_length=64, blank=True, default='')
    flaw4 = models.CharField(max_length=64, blank=True, default='')
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

    @property
    def shapeshifter(self):
        glabro = {'strength': +2, 'dexterity': 0, 'stamina': +2,
                  'charisma': 0, 'manipulation': -1, 'appearance': -1,
                  'perception': 0, 'intelligence': 0, 'wits': 0}
        crinos = {'strength': +4, 'dexterity': +1, 'stamina': +3,
                  'charisma': 0, 'manipulation': -3, 'appearance': -10,
                  'perception': 0, 'intelligence': 0, 'wits': 0}
        hispo = {'strength': +3, 'dexterity': +2, 'stamina': +3,
                 'charisma': 0, 'manipulation': -3, 'appearance': 0,
                 'perception': 0, 'intelligence': 0, 'wits': 0}
        lupus = {'strength': +1, 'dexterity': +2, 'stamina': +2,
                 'charisma': 0, 'manipulation': -3, 'appearance': 0,
                 'perception': 0, 'intelligence': 0, 'wits': 0}
        return glabro, crinos, hispo, lupus

    def root_family(self):
        if self.creature == 'kindred':
            return self.family.replace(' Antitribu', '')
        else:
            return self.family

    def value_of(self, stat):
        found = find_stat_property(self.creature, stat)
        if found == 'n/a':
            logger.error(f'Error finding {stat} for {self.creature} ({self.name})')
        return getattr(self, found)

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
            else:
                break
        # Willpower
        if self.willpower < self.level2:
            self.willpower = self.level2
        # Humanity
        if self.power1 < self.level0 + self.level1:
            self.power1 = self.level0 + self.level1
        # Bloodpool
        self.power2 = bloodpool[13 - self.background3]

        self.display_gauge = self.value_of('generation') + self.value_of('status') + int(self.trueage / 50)
        self.display_pole = self.groupspec

    def fix_ghoul(self):
        self.display_gauge = 1
        if self.domitor:
            if self.family == '':
                domitor = Creature.objects.get(name=self.domitor)
                self.family = domitor.family
                self.faction = domitor.faction
                if domitor:
                    self.display_gauge = domitor.display_gauge / 3
        self.expectedfreebies = int(((self.trueage - 10) / 10) * 3)
        self.power2 = 10
        self.display_pole = self.groupspec

    def fix_mortal(self):
        self.trueage = self.age
        self.power2 = 5 + self.attribute2 + self.attribute3
        if self.willpower < 2:
            self.willpower = 2
        self.expectedfreebies = int(((self.age - 10) / 10) * 5)
        self.display_gauge = self.value_of('family') + self.value_of('career')
        self.display_pole = self.groupspec

    def fix_kinfolk(self):
        self.trueage = self.age
        self.expectedfreebies = int(((self.age - 10) / 10) * 5)
        self.display_pole = self.groupspec
        self.display_gauge = self.value_of('renown') + self.value_of('status') + self.value_of('pure-breed')

    def fix_fomori(self):
        self.display_gauge = self.power2
        self.expectedfreebies = int(((self.age - 10) / 10) * 5)

    def fix_bane(self):
        self.display_gauge = self.power2 * 2
        self.display_pole = self.groupspec

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
        self.display_gauge = self.level0 + self.level1 + self.level2
        if self.breed != 1:
            self.display_gauge += 1
        self.display_pole = self.groupspec
        expected_freebies_by_rank = [0, 55, 134, 234, 345]
        self.expectedfreebies = int(((self.age - 10) / 10) * 5) + expected_freebies_by_rank[self.rank - 1]

    def update_rid(self):
        s = self.name.lower()
        x = s.replace(' ', '_').replace("'", '').replace('é', 'e') \
            .replace('è', 'e').replace('ë', 'e').replace('â', 'a') \
            .replace('ô', 'o').replace('"', '').replace('ï', 'i') \
            .replace('à', 'a').replace('-', '').replace('ö', 'oe') \
            .replace('ä', 'ae').replace('ü', 'ue').replace('ß', 'ss')
        self.rid = x.lower()

    def fix(self):
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
            self.freebies = -((6 + 4 + 3 + 9) * 5 + (11 + 7 + 4) * 2 + 5 + 3 + 21)
            self.fix_kinfolk()
        elif self.creature == 'fomori':
            self.freebies = -((6 + 4 + 3 + 9) * 5 + (11 + 7 + 4) * 2 + 5 + 3 + 21)
            self.fix_fomori()
        elif self.creature == 'bane':
            self.fix_bane()
        else:
            self.creature = 'mortal'
            self.fix_mortal()
        self.display_gauge += int(self.extra / 5)
        self.expectedfreebies += self.extra
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

    def get_roster(self):
        lines = []
        lines.append(f'<strong>{self.name}</strong>')
        if (self.entrance):
            lines.append(f'<i>{self.entrance}</i>')
        lines.append(f'Concept: {self.concept}')
        if self.creature == 'kindred' or self.creature == 'ghoul':
            lines.append(f'Age: {self.age}')
            lines.append(f'Real Age: {self.trueage}')
            lines.append(f'Embrace: {self.embrace}')
        else:
            lines.append(f'Age: {self.age}')
        lines.append(f'Nature: {self.nature}')
        lines.append(f'Demeanor: {self.demeanor}')
        lines.append(
            f'<b>Attributes</b> <small>({self.total_physical}/{self.total_social}/{self.total_mental})</small>:')
        lines.append(f'Strength {self.attribute0}, Dexterity {self.attribute1}, Stamina {self.attribute2}')
        lines.append(f'Charisma {self.attribute3}, Manipulation {self.attribute4}, Appearance {self.attribute5}')
        lines.append(f'Perception {self.attribute6}, Intelligence {self.attribute7}, Wits {self.attribute8}')
        abilities_list = []
        topics = ['talents', 'skills', 'knowledges']
        for topic in topics:
            for ability in STATS_NAMES[self.creature][topic]:
                val = self.value_of(ability)
                if val > 0:
                    abilities_list.append(f'{ability.title()} {val}')
        lines.append(
            f'<b>Abilities</b> <small>({self.total_talents}/{self.total_skills}/{self.total_knowledges})</small>: {", ".join(abilities_list)}.')
        backgrounds_list = []
        topics = ['backgrounds']
        for topic in topics:
            for ability in STATS_NAMES[self.creature][topic]:
                val = self.value_of(ability)
                if val > 0:
                    abilities_list.append(f'{ability.title()} {val}')
        if len(backgrounds_list) > 0:
            lines.append(
                f'<b>Backgrounds</b> <small>({self.total_backgrounds})</small>: {", ".join(backgrounds_list)}.')
        gifts_list = []
        for n in range(10):
            if getattr(self, f"gift{n}"):
                gifts_list.append(f'{getattr(self, f"gift{n}")}')
        if len(gifts_list) > 0:
            if self.creature == 'kindred' or self.creature == 'ghoul':
                lines.append(f'<b>Disciplines</b>: {", ".join(gifts_list)}.')
            else:
                lines.append(f'<b>Gifts</b>: {", ".join(gifts_list)}.')
        merits_list = []
        for n in range(4):
            if getattr(self, f"merit{n}"):
                merits_list.append(f'{getattr(self, f"merit{n}")}')
        if len(merits_list) > 0:
            lines.append(f'<b>Merits:</b> {", ".join(merits_list)}.')
        flaws_list = []
        for n in range(4):
            if getattr(self, f"flaw{n}"):
                flaws_list.append(f'{getattr(self, f"flaw{n}")}')
        if len(flaws_list) > 0:
            lines.append(f'<b>Flaw:</b> {", ".join(flaws_list)}.')
        powers_line = ''
        if self.creature == 'kindred' or self.creature == 'ghoul':
            lines.append(
                f'<b>Virtues</b>: Conscience {self.level0}, Self-Control {self.level1}, Courage {self.level2}.')
            powers_line += f'<b>Blood Pool</b> {self.power2} '
            powers_line += f'<b>{self.path}</b> {self.power1}'
        elif self.creature == 'garou' or self.creature == 'kinfolk':
            powers_line += f'<b>Rage</b> {self.power1} '
            powers_line += f'<b>Gnosis</b> {self.power2}'
        else:
            powers_line += f'<b>Blood Pool</b> {self.power2}'
        powers_line += f' <b>Willpower</b> {self.willpower}'
        lines.append(powers_line)
        lines.append(" ")
        lines.append(" ")
        return "<BR/>".join(lines)

    def extract_roster(self):
        return self.get_roster()

    def randomize_kinfolk(self):
        import random
        self.willpower = 3
        for t in range(10):
            setattr(self, f'attribute{t}', 1)
            setattr(self, f'talent{t}', 0)
            setattr(self, f'skill{t}', 0)
            setattr(self, f'knowledge{t}', 0)
            setattr(self, f'background{t}', 0)
        attributes = [2, 5, 8]
        random.shuffle(attributes)
        abilities = ["talent", "skill", "knowledge"]
        random.shuffle(abilities)
        attribute_points = [6, 4, 3]
        abilities_points = [11, 7, 4]
        for t in range(3):
            while attribute_points[t] > 0:
                attribute_points[t] -= 1
                a = random.randrange(0, 3)
                stat = f'attribute{attributes[t] - a}'
                v = getattr(self, stat)
                setattr(self, stat, v + 1)
        for t in range(3):
            while abilities_points[t] > 0:
                abilities_points[t] -= 1
                a = random.randrange(0, 10)
                stat = f'{abilities[t]}{a}'
                v = getattr(self, stat)
                setattr(self, stat, v + 1)
        for i in range(5):
            a = random.randrange(0, 10)
            stat = f'background{a}'
            v = getattr(self, stat)
            setattr(self, stat, v + 1)
        self.condition = "OK"
        self.need_fix = True
        self.save()

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
        for n in range(4):
            merit = getattr(self, 'merit%d' % (n))
            if merit != '':
                self.freebies += int(merit.split('(')[1].replace('(', '').replace(')', ''))
            flaw = getattr(self, 'flaw%d' % (n))
            if flaw != '':
                self.freebies -= int(flaw.split('(')[1].replace('(', '').replace(')', ''))
        # Gifts/Disciplines
        self.total_gifts = 0
        self.disciplinepoints = 0
        for n in range(10):
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
        for x in range(10):
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
            sire = self.domitor
        else:
            sire = self.sire
        d = {
            'name': self.name,
            'clan': self.family,
            'family': self.root_family(),
            'condition': self.condition,
            'status': self.status,
            'sire': sire,
            'generation': (13 - self.background3),
            'ghost': self.ghost,
            'faction': self.faction,
            'rid': self.rid,
            'children': []
        }
        print(f'd:{d}')
        return d

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

    def toJSON(self):
        self.guideline = self.stats_template
        jstr = json.dumps(self, default=json_default, sort_keys=True, indent=4)
        return jstr

    @property
    def stats_template(self):
        from collector.utils.wod_reference import STATS_TEMPLATES
        list = []
        for v in STATS_TEMPLATES[self.creature]:
            list.append(f'{v.title()}:{STATS_TEMPLATES[self.creature][v]}')
        return '[' + ' '.join(list) + ']'


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


def set_female(modeladmin, request, queryset):
    for creature in queryset:
        creature.sex = False
        creature.need_fix = True
        creature.save()
    short_description = 'Make female'


def set_male(modeladmin, request, queryset):
    for creature in queryset:
        creature.sex = True
        creature.need_fix = True
        creature.save()
    short_description = 'Make male'


def push_to_MBN(modeladmin, request, queryset):
    for creature in queryset:
        creature.chronicle = 'MBN'
        creature.need_fix = True
        creature.save()
    short_description = 'Push to Munich By Night'

def push_to_BAV(modeladmin, request, queryset):
    for creature in queryset:
        creature.chronicle = 'BAV'
        creature.need_fix = True
        creature.save()
    short_description = 'Push to BAV'



class CreatureAdmin(admin.ModelAdmin):
    list_display = [  # 'domitor',
        'name', 'rid', 'creature', 'family', 'display_gauge', 'display_pole', 'freebies', 'concept', 'groupspec',
        'faction',
        'status', 'trueage']
    ordering = ['name', 'group', 'creature']
    actions = [refix, set_male, set_female, push_to_RAM, push_to_MBN, push_to_BAV]
    list_filter = ['chronicle', 'group', 'patron', 'groupspec', 'faction', 'family', 'creature']
    search_fields = ['name']
