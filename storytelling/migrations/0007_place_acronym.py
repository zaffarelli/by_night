# Generated by Django 3.2 on 2021-06-01 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storytelling', '0006_scene_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='acronym',
            field=models.CharField(default='', max_length=24),
        ),
    ]
