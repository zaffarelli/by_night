# Generated by Django 2.2.4 on 2021-04-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0020_auto_20210418_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='rid',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
