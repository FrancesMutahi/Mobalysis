# Generated by Django 3.2.6 on 2021-09-07 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_merge_20210907_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item_match_performance',
            old_name='participantId',
            new_name='summonerId',
        ),
    ]
