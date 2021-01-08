# Generated by Django 2.2.4 on 2021-01-07 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0017_chronicle_is_current'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creature',
            options={'ordering': ['name'], 'verbose_name': 'Creatures'},
        ),
        migrations.AddField(
            model_name='creature',
            name='mythic_entity',
            field=models.BooleanField(default=False),
        ),
    ]
