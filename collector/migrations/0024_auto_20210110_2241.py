# Generated by Django 2.2.4 on 2021-01-10 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0023_auto_20210110_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='domitor',
            field=models.ForeignKey(blank=True, limit_choices_to={'chronicle': 'NYBN', 'creature': 'kindred'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Domitor', to='collector.Creature'),
        ),
    ]