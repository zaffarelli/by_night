# Generated by Django 2.2.4 on 2021-01-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0018_auto_20210107_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creature',
            name='mythic_entity',
        ),
        migrations.AddField(
            model_name='creature',
            name='mythic',
            field=models.BooleanField(default=False),
        ),
    ]