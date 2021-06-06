# Generated by Django 3.2 on 2021-06-05 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storytelling', '0018_remove_place_is_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='consequences',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='scene',
            name='preamble',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AddField(
            model_name='scene',
            name='rewards',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
    ]
