# Generated by Django 2.2.4 on 2021-04-27 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0035_remove_creature_merit4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('path', models.CharField(blank=True, default='', max_length=128)),
                ('level', models.PositiveIntegerField(default=0)),
                ('creature', models.CharField(blank=True, default='', max_length=32)),
                ('declaration', models.CharField(blank=True, default='', max_length=256)),
                ('description', models.TextField(blank=True, default='', max_length=1024)),
            ],
        ),
    ]
