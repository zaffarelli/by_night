# Generated by Django 2.2.4 on 2021-04-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0036_rite'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='gift11',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='creature',
            name='gift12',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='creature',
            name='gift13',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='creature',
            name='gift14',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AddField(
            model_name='creature',
            name='gift15',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]