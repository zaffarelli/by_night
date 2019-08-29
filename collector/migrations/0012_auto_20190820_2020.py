# Generated by Django 2.2 on 2019-08-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0011_auto_20190819_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creature',
            name='chronicle',
            field=models.CharField(default='NYBN', max_length=8),
        ),
        migrations.AlterField(
            model_name='creature',
            name='creature',
            field=models.CharField(default='kindred', max_length=20),
        ),
        migrations.AlterField(
            model_name='creature',
            name='family',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='creature',
            name='nickname',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='creature',
            name='player',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
    ]