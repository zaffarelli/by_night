# Generated by Django 3.2.1 on 2021-06-18 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectorNybnKindreds',
            fields=[
                ('player', models.CharField(blank=True, db_column='Player', max_length=32, null=True)),
                ('name', models.CharField(db_column='Name', max_length=128, primary_key=True, serialize=False)),
                ('clan', models.CharField(blank=True, db_column='Clan', max_length=32, null=True)),
                ('gen', models.IntegerField(blank=True, db_column='Gen', null=True)),
                ('nature', models.CharField(blank=True, db_column='Nature', max_length=32, null=True)),
                ('demeanor', models.CharField(blank=True, db_column='Demeanor', max_length=32, null=True)),
                ('disc_animalism', models.IntegerField(blank=True, db_column='Animalism', null=True)),
                ('disc_auspex', models.IntegerField(blank=True, db_column='Auspex', null=True)),
                ('disc_celerity', models.IntegerField(blank=True, db_column='Celerity', null=True)),
                ('disc_chimerstry', models.IntegerField(blank=True, db_column='Chimerstry', null=True)),
                ('disc_daimoinon', models.IntegerField(blank=True, db_column='Daimoinon', null=True)),
                ('disc_dementation', models.IntegerField(blank=True, db_column='Dementation', null=True)),
                ('disc_dominate', models.IntegerField(blank=True, db_column='Dominate', null=True)),
                ('disc_fortitude', models.IntegerField(blank=True, db_column='Fortitude', null=True)),
                ('disc_melpominee', models.IntegerField(blank=True, db_column='Melpominee', null=True)),
                ('disc_mytherceria', models.IntegerField(blank=True, db_column='Mytherceria', null=True)),
                ('disc_necromancy', models.IntegerField(blank=True, db_column='Necromancy', null=True)),
                ('disc_obeah', models.IntegerField(blank=True, db_column='Obeah', null=True)),
                ('disc_obfuscate', models.IntegerField(blank=True, db_column='Obfuscate', null=True)),
                ('disc_obtenebration', models.IntegerField(blank=True, db_column='Obtenebration', null=True)),
                ('disc_potence', models.IntegerField(blank=True, db_column='Potence', null=True)),
                ('disc_presence', models.IntegerField(blank=True, db_column='Presence', null=True)),
                ('disc_protean', models.IntegerField(blank=True, db_column='Protean', null=True)),
                ('disc_quietus', models.IntegerField(blank=True, db_column='Quietus', null=True)),
                ('disc_sanguinus', models.IntegerField(blank=True, db_column='Sanguinus', null=True)),
                ('disc_serpentis', models.IntegerField(blank=True, db_column='Serpentis', null=True)),
                ('disc_temporis', models.IntegerField(blank=True, db_column='Temporis', null=True)),
                ('disc_thanatosis', models.IntegerField(blank=True, db_column='Thanatosis', null=True)),
                ('disc_thaumaturgy', models.IntegerField(blank=True, db_column='Thaumaturgy', null=True)),
                ('disc_valeren', models.IntegerField(blank=True, db_column='Valeren', null=True)),
                ('disc_vicissitude', models.IntegerField(blank=True, db_column='Vicissitude', null=True)),
                ('disc_visceratika', models.IntegerField(blank=True, db_column='Visceratika', null=True)),
                ('coterie', models.CharField(blank=True, db_column='Coterie', max_length=128, null=True)),
                ('role', models.CharField(blank=True, db_column='Role', max_length=128, null=True)),
                ('strength', models.IntegerField(blank=True, db_column='Strength', null=True)),
                ('dexterity', models.IntegerField(blank=True, db_column='Dexterity', null=True)),
                ('stamina', models.IntegerField(blank=True, db_column='Stamina', null=True)),
                ('charisma', models.IntegerField(blank=True, db_column='Charisma', null=True)),
                ('manipulation', models.IntegerField(blank=True, db_column='Manipulation', null=True)),
                ('appearance', models.IntegerField(blank=True, db_column='Appearance', null=True)),
                ('perception', models.IntegerField(blank=True, db_column='Perception', null=True)),
                ('intelligence', models.IntegerField(blank=True, db_column='Intelligence', null=True)),
                ('wits', models.IntegerField(blank=True, db_column='Wits', null=True)),
                ('alertness', models.IntegerField(blank=True, db_column='Alertness', null=True)),
                ('athletics', models.IntegerField(blank=True, db_column='Athletics', null=True)),
                ('brawl', models.IntegerField(blank=True, db_column='Brawl', null=True)),
                ('dodge', models.IntegerField(blank=True, db_column='Dodge', null=True)),
                ('empathy', models.IntegerField(blank=True, db_column='Empathy', null=True)),
                ('expression', models.IntegerField(blank=True, db_column='Expression', null=True)),
                ('intimidation', models.IntegerField(blank=True, db_column='Intimidation', null=True)),
                ('leadership', models.IntegerField(blank=True, db_column='Leadership', null=True)),
                ('streetwise', models.IntegerField(blank=True, db_column='Streetwise', null=True)),
                ('subterfuge', models.IntegerField(blank=True, db_column='Subterfuge', null=True)),
                ('animalken', models.IntegerField(blank=True, db_column='AnimalKen', null=True)),
                ('crafts', models.IntegerField(blank=True, db_column='Crafts', null=True)),
                ('drive', models.IntegerField(blank=True, db_column='Drive', null=True)),
                ('etiquette', models.IntegerField(blank=True, db_column='Etiquette', null=True)),
                ('firearms', models.IntegerField(blank=True, db_column='Firearms', null=True)),
                ('melee', models.IntegerField(blank=True, db_column='Melee', null=True)),
                ('performance', models.IntegerField(blank=True, db_column='Performance', null=True)),
                ('security', models.IntegerField(blank=True, db_column='Security', null=True)),
                ('stealth', models.IntegerField(blank=True, db_column='Stealth', null=True)),
                ('survival', models.IntegerField(blank=True, db_column='Survival', null=True)),
                ('academics', models.IntegerField(blank=True, db_column='Academics', null=True)),
                ('computer', models.IntegerField(blank=True, db_column='Computer', null=True)),
                ('finance', models.IntegerField(blank=True, db_column='Finance', null=True)),
                ('investigation', models.IntegerField(blank=True, db_column='Investigation', null=True)),
                ('law', models.IntegerField(blank=True, db_column='Law', null=True)),
                ('linguistics', models.IntegerField(blank=True, db_column='Linguistics', null=True)),
                ('medicine', models.IntegerField(blank=True, db_column='Medicine', null=True)),
                ('occult', models.IntegerField(blank=True, db_column='Occult', null=True)),
                ('politics', models.IntegerField(blank=True, db_column='Politics', null=True)),
                ('science', models.IntegerField(blank=True, db_column='Science', null=True)),
                ('humanity', models.IntegerField(blank=True, db_column='Humanity', null=True)),
                ('willpower', models.IntegerField(blank=True, db_column='Willpower', null=True)),
                ('conscience', models.IntegerField(blank=True, db_column='Conscience', null=True)),
                ('selfcontrol', models.IntegerField(blank=True, db_column='SelfControl', null=True)),
                ('courage', models.IntegerField(blank=True, db_column='Courage', null=True)),
                ('bloodpool', models.IntegerField(blank=True, db_column='BloodPool', null=True)),
                ('path', models.CharField(blank=True, db_column='Path', max_length=64, null=True)),
                ('sect', models.CharField(blank=True, db_column='Sect', max_length=64, null=True)),
                ('allies', models.IntegerField(blank=True, db_column='Allies', null=True)),
                ('contact', models.IntegerField(blank=True, db_column='Contact', null=True)),
                ('fame', models.IntegerField(blank=True, db_column='Fame', null=True)),
                ('generation', models.IntegerField(blank=True, db_column='Generation', null=True)),
                ('herd', models.IntegerField(blank=True, db_column='Herd', null=True)),
                ('influence', models.IntegerField(blank=True, db_column='Influence', null=True)),
                ('mentor', models.IntegerField(blank=True, db_column='Mentor', null=True)),
                ('resources', models.IntegerField(blank=True, db_column='Resources', null=True)),
                ('retainers', models.IntegerField(blank=True, db_column='Retainers', null=True)),
                ('status', models.IntegerField(blank=True, db_column='Status', null=True)),
                ('sire', models.CharField(blank=True, db_column='Sire', max_length=128, null=True)),
                ('embraceyear', models.IntegerField(blank=True, db_column='EmbraceYear', null=True)),
                ('torpor', models.IntegerField()),
                ('merit_1', models.CharField(max_length=32)),
                ('merit_2', models.CharField(max_length=32)),
                ('merit_3', models.CharField(max_length=32)),
                ('merit_4', models.CharField(max_length=32)),
                ('merit_5', models.CharField(max_length=32)),
                ('flaw_1', models.CharField(max_length=32)),
                ('flaw_2', models.CharField(max_length=32)),
                ('flaw_3', models.CharField(max_length=32)),
                ('flaw_4', models.CharField(max_length=32)),
                ('flaw_5', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'collector_nybn_kindreds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CollectorRanyGarous',
            fields=[
                ('player', models.CharField(blank=True, db_column='Player', max_length=32, null=True)),
                ('name', models.CharField(db_column='Name', max_length=128, primary_key=True, serialize=False)),
                ('family', models.CharField(blank=True, db_column='Family', max_length=32, null=True)),
                ('auspice', models.IntegerField(blank=True, db_column='Auspice', null=True)),
                ('breed', models.IntegerField(blank=True, db_column='Breed', null=True)),
                ('group', models.CharField(blank=True, db_column='Group', max_length=128, null=True)),
                ('groupspec', models.CharField(blank=True, db_column='GroupSpec', max_length=128, null=True)),
                ('concept', models.CharField(blank=True, db_column='Concept', max_length=128, null=True)),
                ('strength', models.IntegerField(blank=True, db_column='Strength', null=True)),
                ('dexterity', models.IntegerField(blank=True, db_column='Dexterity', null=True)),
                ('stamina', models.IntegerField(blank=True, db_column='Stamina', null=True)),
                ('charisma', models.IntegerField(blank=True, db_column='Charisma', null=True)),
                ('manipulation', models.IntegerField(blank=True, db_column='Manipulation', null=True)),
                ('appearance', models.IntegerField(blank=True, db_column='Appearance', null=True)),
                ('perception', models.IntegerField(blank=True, db_column='Perception', null=True)),
                ('intelligence', models.IntegerField(blank=True, db_column='Intelligence', null=True)),
                ('wits', models.IntegerField(blank=True, db_column='Wits', null=True)),
                ('talent0', models.IntegerField(blank=True, db_column='Talent0', null=True)),
                ('talent1', models.IntegerField(blank=True, db_column='Talent1', null=True)),
                ('talent2', models.IntegerField(blank=True, db_column='Talent2', null=True)),
                ('talent3', models.IntegerField(blank=True, db_column='Talent3', null=True)),
                ('talent4', models.IntegerField(blank=True, db_column='Talent4', null=True)),
                ('talent5', models.IntegerField(blank=True, db_column='Talent5', null=True)),
                ('talent6', models.IntegerField(blank=True, db_column='Talent6', null=True)),
                ('talent7', models.IntegerField(blank=True, db_column='Talent7', null=True)),
                ('talent8', models.IntegerField(blank=True, db_column='Talent8', null=True)),
                ('talent9', models.IntegerField(blank=True, db_column='Talent9', null=True)),
                ('skill0', models.IntegerField(blank=True, db_column='Skill0', null=True)),
                ('skill1', models.IntegerField(blank=True, db_column='Skill1', null=True)),
                ('skill2', models.IntegerField(blank=True, db_column='Skill2', null=True)),
                ('skill3', models.IntegerField(blank=True, db_column='Skill3', null=True)),
                ('skill4', models.IntegerField(blank=True, db_column='Skill4', null=True)),
                ('skill5', models.IntegerField(blank=True, db_column='Skill5', null=True)),
                ('skill6', models.IntegerField(blank=True, db_column='Skill6', null=True)),
                ('skill7', models.IntegerField(blank=True, db_column='Skill7', null=True)),
                ('skill8', models.IntegerField(blank=True, db_column='Skill8', null=True)),
                ('skill9', models.IntegerField(blank=True, db_column='Skill9', null=True)),
                ('knowledge0', models.IntegerField(blank=True, db_column='Knowledge0', null=True)),
                ('knowledge1', models.IntegerField(blank=True, db_column='Knowledge1', null=True)),
                ('knowledge2', models.IntegerField(blank=True, db_column='Knowledge2', null=True)),
                ('knowledge3', models.IntegerField(blank=True, db_column='Knowledge3', null=True)),
                ('knowledge4', models.IntegerField(blank=True, db_column='Knowledge4', null=True)),
                ('knowledge5', models.IntegerField(blank=True, db_column='Knowledge5', null=True)),
                ('knowledge6', models.IntegerField(blank=True, db_column='Knowledge6', null=True)),
                ('knowledge7', models.IntegerField(blank=True, db_column='Knowledge7', null=True)),
                ('knowledge8', models.IntegerField(blank=True, db_column='Knowledge8', null=True)),
                ('knowledge9', models.IntegerField(blank=True, db_column='Knowledge9', null=True)),
                ('power1', models.IntegerField(blank=True, db_column='Power1', null=True)),
                ('power2', models.IntegerField(blank=True, db_column='Power2', null=True)),
                ('willpower', models.IntegerField(blank=True, db_column='Willpower', null=True)),
                ('level0', models.IntegerField(blank=True, db_column='Level0', null=True)),
                ('level1', models.IntegerField(blank=True, db_column='Level1', null=True)),
                ('level2', models.IntegerField(blank=True, db_column='Level2', null=True)),
                ('rank', models.CharField(blank=True, db_column='Rank', max_length=128, null=True)),
                ('background0', models.IntegerField(blank=True, db_column='Background0', null=True)),
                ('background1', models.IntegerField(blank=True, db_column='Background1', null=True)),
                ('background2', models.IntegerField(blank=True, db_column='Background2', null=True)),
                ('background3', models.IntegerField(blank=True, db_column='Background3', null=True)),
                ('background4', models.IntegerField(blank=True, db_column='Background4', null=True)),
                ('background5', models.IntegerField(blank=True, db_column='Background5', null=True)),
                ('background6', models.IntegerField(blank=True, db_column='Background6', null=True)),
                ('background7', models.IntegerField(blank=True, db_column='Background7', null=True)),
                ('background8', models.IntegerField(blank=True, db_column='Background8', null=True)),
                ('background9', models.IntegerField(blank=True, db_column='Background9', null=True)),
                ('gift0', models.CharField(blank=True, db_column='Gift0', max_length=64, null=True)),
                ('gift1', models.CharField(blank=True, db_column='Gift1', max_length=64, null=True)),
                ('gift2', models.CharField(blank=True, db_column='Gift2', max_length=64, null=True)),
                ('gift3', models.CharField(blank=True, db_column='Gift3', max_length=64, null=True)),
                ('gift4', models.CharField(blank=True, db_column='Gift4', max_length=64, null=True)),
                ('gift5', models.CharField(blank=True, db_column='Gift5', max_length=64, null=True)),
                ('gift6', models.CharField(blank=True, db_column='Gift6', max_length=64, null=True)),
                ('gift7', models.CharField(blank=True, db_column='Gift7', max_length=64, null=True)),
                ('gift8', models.CharField(blank=True, db_column='Gift8', max_length=64, null=True)),
                ('gift9', models.CharField(blank=True, db_column='Gift9', max_length=64, null=True)),
                ('merit0', models.CharField(blank=True, db_column='Merit0', max_length=64, null=True)),
                ('merit1', models.CharField(blank=True, db_column='Merit1', max_length=64, null=True)),
                ('merit2', models.CharField(blank=True, db_column='Merit2', max_length=64, null=True)),
                ('merit3', models.CharField(blank=True, db_column='Merit3', max_length=64, null=True)),
                ('merit4', models.CharField(blank=True, db_column='Merit4', max_length=64, null=True)),
                ('merit5', models.CharField(blank=True, db_column='Merit5', max_length=64, null=True)),
                ('merit6', models.CharField(blank=True, db_column='Merit6', max_length=64, null=True)),
                ('merit7', models.CharField(blank=True, db_column='Merit7', max_length=64, null=True)),
                ('merit8', models.CharField(blank=True, db_column='Merit8', max_length=64, null=True)),
                ('merit9', models.CharField(blank=True, db_column='Merit9', max_length=64, null=True)),
                ('flaw0', models.CharField(blank=True, db_column='Flaw0', max_length=64, null=True)),
                ('flaw1', models.CharField(blank=True, db_column='Flaw1', max_length=64, null=True)),
                ('flaw2', models.CharField(blank=True, db_column='Flaw2', max_length=64, null=True)),
                ('flaw3', models.CharField(blank=True, db_column='Flaw3', max_length=64, null=True)),
                ('flaw4', models.CharField(blank=True, db_column='Flaw4', max_length=64, null=True)),
                ('flaw5', models.CharField(blank=True, db_column='Flaw5', max_length=64, null=True)),
                ('flaw6', models.CharField(blank=True, db_column='Flaw6', max_length=64, null=True)),
                ('flaw7', models.CharField(blank=True, db_column='Flaw7', max_length=64, null=True)),
                ('flaw8', models.CharField(blank=True, db_column='Flaw8', max_length=64, null=True)),
                ('flaw9', models.CharField(blank=True, db_column='Flaw9', max_length=64, null=True)),
                ('topic', models.CharField(blank=True, db_column='Topic', max_length=128, null=True)),
                ('status', models.CharField(db_column='Status', max_length=128)),
                ('maj', models.IntegerField()),
                ('freebiedif', models.IntegerField(db_column='FreebieDif')),
                ('experience', models.IntegerField(db_column='Experience')),
                ('hidden', models.IntegerField(db_column='Hidden')),
                ('rite0', models.CharField(db_column='Rite0', max_length=64)),
                ('rite1', models.CharField(db_column='Rite1', max_length=64)),
                ('rite2', models.CharField(db_column='Rite2', max_length=64)),
                ('rite3', models.CharField(db_column='Rite3', max_length=64)),
                ('rite4', models.CharField(db_column='Rite4', max_length=64)),
                ('rite5', models.CharField(db_column='Rite5', max_length=64)),
                ('rite6', models.CharField(db_column='Rite6', max_length=64)),
                ('rite7', models.CharField(db_column='Rite7', max_length=64)),
                ('rite8', models.CharField(db_column='Rite8', max_length=64)),
                ('rite9', models.CharField(db_column='Rite9', max_length=64)),
                ('rite10', models.CharField(db_column='Rite10', max_length=64)),
                ('rite11', models.CharField(db_column='Rite11', max_length=64)),
                ('rite12', models.CharField(db_column='Rite12', max_length=64)),
                ('rite13', models.CharField(db_column='Rite13', max_length=64)),
                ('rite14', models.CharField(db_column='Rite14', max_length=64)),
                ('rite15', models.CharField(db_column='Rite15', max_length=64)),
                ('visibility', models.IntegerField(db_column='Visibility')),
                ('gift10', models.CharField(db_column='Gift10', max_length=64)),
                ('gift11', models.CharField(db_column='Gift11', max_length=64)),
                ('gift12', models.CharField(db_column='Gift12', max_length=64)),
                ('gift13', models.CharField(db_column='Gift13', max_length=64)),
                ('gift14', models.CharField(db_column='Gift14', max_length=64)),
                ('gift15', models.CharField(db_column='Gift15', max_length=64)),
                ('gift16', models.CharField(db_column='Gift16', max_length=64)),
                ('gift17', models.CharField(db_column='Gift17', max_length=64)),
                ('gift18', models.CharField(db_column='Gift18', max_length=64)),
                ('gift19', models.CharField(db_column='Gift19', max_length=64)),
                ('rite16', models.CharField(db_column='Rite16', max_length=64)),
                ('rite17', models.CharField(db_column='Rite17', max_length=64)),
                ('rite18', models.CharField(db_column='Rite18', max_length=64)),
                ('rite19', models.CharField(db_column='Rite19', max_length=64)),
                ('faction', models.CharField(db_column='Faction', max_length=64)),
                ('lastmod', models.DateTimeField()),
                ('chronicle', models.CharField(max_length=8)),
                ('creature', models.CharField(max_length=20)),
                ('sex', models.IntegerField()),
                ('trueage', models.IntegerField(db_column='TrueAge')),
            ],
            options={
                'db_table': 'collector_rany_garous',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chronicle',
            fields=[
                ('name', models.CharField(default='', max_length=128, primary_key=True, serialize=False)),
                ('acronym', models.CharField(blank=True, default='', max_length=16)),
                ('era', models.IntegerField(default=2019)),
                ('main_creature', models.CharField(blank=True, default='', max_length=128)),
                ('image_logo', models.CharField(blank=True, default='', max_length=128)),
                ('description', models.TextField(blank=True, default='', max_length=1024)),
                ('is_current', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.CharField(blank=True, default='', max_length=32)),
                ('name', models.CharField(default='', max_length=128)),
                ('rid', models.CharField(blank=True, default='', max_length=128)),
                ('nickname', models.CharField(blank=True, default='', max_length=128)),
                ('primogen', models.BooleanField(default=False)),
                ('mythic', models.BooleanField(default=False)),
                ('family', models.CharField(blank=True, default='', max_length=32)),
                ('auspice', models.PositiveIntegerField(default=0)),
                ('breed', models.PositiveIntegerField(default=0)),
                ('domitor', models.CharField(blank=True, default='', max_length=128)),
                ('group', models.CharField(blank=True, default='', max_length=128)),
                ('groupspec', models.CharField(blank=True, default='', max_length=128)),
                ('concept', models.CharField(blank=True, default='', max_length=128)),
                ('age', models.PositiveIntegerField(default=0)),
                ('faction', models.CharField(blank=True, default='', max_length=64)),
                ('lastmod', models.DateTimeField(auto_now=True)),
                ('chronicle', models.CharField(default='NYBN', max_length=8)),
                ('creature', models.CharField(default='kindred', max_length=20)),
                ('sex', models.BooleanField(default=False)),
                ('display_gauge', models.PositiveIntegerField(default=0)),
                ('display_pole', models.CharField(blank=True, default='', max_length=64)),
                ('trueage', models.PositiveIntegerField(default=0)),
                ('embrace', models.IntegerField(default=0)),
                ('finaldeath', models.IntegerField(default=0)),
                ('timeintorpor', models.PositiveIntegerField(default=0)),
                ('picture', models.CharField(blank=True, default='', max_length=128)),
                ('sire', models.CharField(blank=True, default='', max_length=64)),
                ('patron', models.CharField(blank=True, default='', max_length=64)),
                ('rank', models.CharField(blank=True, default='', max_length=32)),
                ('topic', models.TextField(blank=True, default='', max_length=1024)),
                ('status', models.CharField(blank=True, default='OK', max_length=32)),
                ('position', models.CharField(blank=True, default='', max_length=64)),
                ('maj', models.PositiveIntegerField(default=0)),
                ('need_fix', models.BooleanField(default=False)),
                ('is_new', models.BooleanField(default=True)),
                ('freebiedif', models.IntegerField(default=0)),
                ('freebies', models.IntegerField(blank=True, default=0)),
                ('expectedfreebies', models.IntegerField(default=0)),
                ('disciplinepoints', models.IntegerField(default=0)),
                ('experience', models.IntegerField(default=0)),
                ('extra', models.IntegerField(default=0)),
                ('hidden', models.BooleanField(default=False)),
                ('ghost', models.BooleanField(default=False)),
                ('source', models.CharField(blank=True, default='zaffarelli', max_length=64)),
                ('total_physical', models.IntegerField(default=0)),
                ('total_social', models.IntegerField(default=0)),
                ('total_mental', models.IntegerField(default=0)),
                ('total_talents', models.IntegerField(default=0)),
                ('total_skills', models.IntegerField(default=0)),
                ('total_knowledges', models.IntegerField(default=0)),
                ('total_backgrounds', models.IntegerField(default=0)),
                ('total_gifts', models.IntegerField(default=0)),
                ('path', models.CharField(default='Humanity', max_length=64)),
                ('nature', models.CharField(blank=True, default='', max_length=32)),
                ('demeanor', models.CharField(blank=True, default='', max_length=32)),
                ('condition', models.CharField(blank=True, default='OK', max_length=32)),
                ('territory', models.CharField(blank=True, default='', max_length=128)),
                ('weakness', models.CharField(blank=True, default='', max_length=128)),
                ('power1', models.PositiveIntegerField(default=1)),
                ('power2', models.PositiveIntegerField(default=1)),
                ('willpower', models.PositiveIntegerField(default=1)),
                ('level0', models.PositiveIntegerField(default=0)),
                ('level1', models.PositiveIntegerField(default=0)),
                ('level2', models.PositiveIntegerField(default=0)),
                ('summary', models.TextField(blank=True, default='', max_length=2048)),
                ('attribute0', models.PositiveIntegerField(default=1)),
                ('attribute1', models.PositiveIntegerField(default=1)),
                ('attribute2', models.PositiveIntegerField(default=1)),
                ('attribute3', models.PositiveIntegerField(default=1)),
                ('attribute4', models.PositiveIntegerField(default=1)),
                ('attribute5', models.PositiveIntegerField(default=1)),
                ('attribute6', models.PositiveIntegerField(default=1)),
                ('attribute7', models.PositiveIntegerField(default=1)),
                ('attribute8', models.PositiveIntegerField(default=1)),
                ('talent0', models.PositiveIntegerField(default=0)),
                ('talent1', models.PositiveIntegerField(default=0)),
                ('talent2', models.PositiveIntegerField(default=0)),
                ('talent3', models.PositiveIntegerField(default=0)),
                ('talent4', models.PositiveIntegerField(default=0)),
                ('talent5', models.PositiveIntegerField(default=0)),
                ('talent6', models.PositiveIntegerField(default=0)),
                ('talent7', models.PositiveIntegerField(default=0)),
                ('talent8', models.PositiveIntegerField(default=0)),
                ('talent9', models.PositiveIntegerField(default=0)),
                ('skill0', models.PositiveIntegerField(default=0)),
                ('skill1', models.PositiveIntegerField(default=0)),
                ('skill2', models.PositiveIntegerField(default=0)),
                ('skill3', models.PositiveIntegerField(default=0)),
                ('skill4', models.PositiveIntegerField(default=0)),
                ('skill5', models.PositiveIntegerField(default=0)),
                ('skill6', models.PositiveIntegerField(default=0)),
                ('skill7', models.PositiveIntegerField(default=0)),
                ('skill8', models.PositiveIntegerField(default=0)),
                ('skill9', models.PositiveIntegerField(default=0)),
                ('knowledge0', models.PositiveIntegerField(default=0)),
                ('knowledge1', models.PositiveIntegerField(default=0)),
                ('knowledge2', models.PositiveIntegerField(default=0)),
                ('knowledge3', models.PositiveIntegerField(default=0)),
                ('knowledge4', models.PositiveIntegerField(default=0)),
                ('knowledge5', models.PositiveIntegerField(default=0)),
                ('knowledge6', models.PositiveIntegerField(default=0)),
                ('knowledge7', models.PositiveIntegerField(default=0)),
                ('knowledge8', models.PositiveIntegerField(default=0)),
                ('knowledge9', models.PositiveIntegerField(default=0)),
                ('background0', models.PositiveIntegerField(default=0)),
                ('background1', models.PositiveIntegerField(default=0)),
                ('background2', models.PositiveIntegerField(default=0)),
                ('background3', models.PositiveIntegerField(default=0)),
                ('background4', models.PositiveIntegerField(default=0)),
                ('background5', models.PositiveIntegerField(default=0)),
                ('background6', models.PositiveIntegerField(default=0)),
                ('background7', models.PositiveIntegerField(default=0)),
                ('background8', models.PositiveIntegerField(default=0)),
                ('background9', models.PositiveIntegerField(default=0)),
                ('gift0', models.CharField(blank=True, default='', max_length=64)),
                ('gift1', models.CharField(blank=True, default='', max_length=64)),
                ('gift2', models.CharField(blank=True, default='', max_length=64)),
                ('gift3', models.CharField(blank=True, default='', max_length=64)),
                ('gift4', models.CharField(blank=True, default='', max_length=64)),
                ('gift5', models.CharField(blank=True, default='', max_length=64)),
                ('gift6', models.CharField(blank=True, default='', max_length=64)),
                ('gift7', models.CharField(blank=True, default='', max_length=64)),
                ('gift8', models.CharField(blank=True, default='', max_length=64)),
                ('gift9', models.CharField(blank=True, default='', max_length=64)),
                ('gift10', models.CharField(blank=True, default='', max_length=64)),
                ('gift11', models.CharField(blank=True, default='', max_length=64)),
                ('gift12', models.CharField(blank=True, default='', max_length=64)),
                ('gift13', models.CharField(blank=True, default='', max_length=64)),
                ('gift14', models.CharField(blank=True, default='', max_length=64)),
                ('gift15', models.CharField(blank=True, default='', max_length=64)),
                ('merit0', models.CharField(blank=True, default='', max_length=64)),
                ('merit1', models.CharField(blank=True, default='', max_length=64)),
                ('merit2', models.CharField(blank=True, default='', max_length=64)),
                ('merit3', models.CharField(blank=True, default='', max_length=64)),
                ('merit4', models.CharField(blank=True, default='', max_length=64)),
                ('flaw0', models.CharField(blank=True, default='', max_length=64)),
                ('flaw1', models.CharField(blank=True, default='', max_length=64)),
                ('flaw2', models.CharField(blank=True, default='', max_length=64)),
                ('flaw3', models.CharField(blank=True, default='', max_length=64)),
                ('flaw4', models.CharField(blank=True, default='', max_length=64)),
                ('rite0', models.CharField(blank=True, default='', max_length=64)),
                ('rite1', models.CharField(blank=True, default='', max_length=64)),
                ('rite2', models.CharField(blank=True, default='', max_length=64)),
                ('rite3', models.CharField(blank=True, default='', max_length=64)),
                ('rite4', models.CharField(blank=True, default='', max_length=64)),
                ('rite5', models.CharField(blank=True, default='', max_length=64)),
                ('rite6', models.CharField(blank=True, default='', max_length=64)),
                ('rite7', models.CharField(blank=True, default='', max_length=64)),
                ('rite8', models.CharField(blank=True, default='', max_length=64)),
                ('rite9', models.CharField(blank=True, default='', max_length=64)),
            ],
            options={
                'verbose_name': 'Creature',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('name', models.CharField(default='', max_length=128, primary_key=True, serialize=False)),
                ('alternative_name', models.CharField(blank=True, default='', max_length=128)),
                ('level', models.PositiveIntegerField(default=0)),
                ('declaration', models.CharField(blank=True, default='', max_length=256)),
                ('breed_0', models.BooleanField(default=False, verbose_name='Homid')),
                ('breed_1', models.BooleanField(default=False, verbose_name='Metis')),
                ('breed_2', models.BooleanField(default=False, verbose_name='Lupus')),
                ('breeds', models.CharField(default='...', max_length=3)),
                ('auspices', models.CharField(default='.....', max_length=5)),
                ('tribes', models.CharField(default='________________', max_length=16)),
                ('auspice_0', models.BooleanField(default=False, verbose_name='Ragabash')),
                ('auspice_1', models.BooleanField(default=False, verbose_name='Theurge')),
                ('auspice_2', models.BooleanField(default=False, verbose_name='Philodox')),
                ('auspice_3', models.BooleanField(default=False, verbose_name='Galliard')),
                ('auspice_4', models.BooleanField(default=False, verbose_name='Ahroun')),
                ('tribe_0', models.BooleanField(default=False, verbose_name='Black Furies')),
                ('tribe_1', models.BooleanField(default=False, verbose_name='Black Spiral Dancers')),
                ('tribe_2', models.BooleanField(default=False, verbose_name='Bone Gnawers')),
                ('tribe_3', models.BooleanField(default=False, verbose_name='Bunyips')),
                ('tribe_4', models.BooleanField(default=False, verbose_name='Children of Gaia')),
                ('tribe_5', models.BooleanField(default=False, verbose_name='Croatans')),
                ('tribe_6', models.BooleanField(default=False, verbose_name='Fiannas')),
                ('tribe_7', models.BooleanField(default=False, verbose_name='Glass Walkers')),
                ('tribe_8', models.BooleanField(default=False, verbose_name='Gets of Fenris')),
                ('tribe_9', models.BooleanField(default=False, verbose_name='Red Talons')),
                ('tribe_10', models.BooleanField(default=False, verbose_name='Silent Striders')),
                ('tribe_11', models.BooleanField(default=False, verbose_name='Silver Fangs')),
                ('tribe_12', models.BooleanField(default=False, verbose_name='Stargazers')),
                ('tribe_13', models.BooleanField(default=False, verbose_name='Uktenas')),
                ('tribe_14', models.BooleanField(default=False, verbose_name='Wendigos')),
                ('tribe_15', models.BooleanField(default=False, verbose_name='White Howlers')),
                ('description', models.TextField(blank=True, default='', max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Rite',
            fields=[
                ('name', models.CharField(default='', max_length=128, primary_key=True, serialize=False)),
                ('path', models.CharField(blank=True, default='', max_length=128)),
                ('level', models.PositiveIntegerField(default=0)),
                ('creature', models.CharField(blank=True, default='', max_length=32)),
                ('declaration', models.CharField(blank=True, default='', max_length=256)),
                ('description', models.TextField(blank=True, default='', max_length=1024)),
            ],
        ),
    ]
