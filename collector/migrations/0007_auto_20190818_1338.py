# Generated by Django 2.2 on 2019-08-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_auto_20190816_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='creature',
            name='embrace',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='creature',
            name='status',
            field=models.CharField(blank=True, default='OK', max_length=32),
        ),
    ]
