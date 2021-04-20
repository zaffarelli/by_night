# Generated by Django 2.2.4 on 2021-04-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0017_auto_20210412_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='display_gauge',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='creature',
            name='display_pole',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
