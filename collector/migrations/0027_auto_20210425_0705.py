# Generated by Django 2.2.4 on 2021-04-25 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0026_gift_declaration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='aupice_0',
            new_name='auspice_0',
        ),
        migrations.RenameField(
            model_name='gift',
            old_name='aupice_1',
            new_name='auspice_1',
        ),
        migrations.RenameField(
            model_name='gift',
            old_name='aupice_2',
            new_name='auspice_2',
        ),
        migrations.RenameField(
            model_name='gift',
            old_name='aupice_3',
            new_name='auspice_3',
        ),
        migrations.RenameField(
            model_name='gift',
            old_name='aupice_4',
            new_name='auspice_4',
        ),
    ]