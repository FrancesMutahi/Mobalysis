# Generated by Django 3.1.2 on 2021-11-03 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0059_runepage_runestatistics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='runestatistics',
            old_name='banrate',
            new_name='pickrate',
        ),
    ]
