# Generated by Django 2.2.4 on 2021-01-10 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0005_creature_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='domitor',
        ),
    ]