# Generated by Django 3.2.6 on 2021-08-31 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_item_match_performance_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_match_performance',
            name='championId',
            field=models.ForeignKey(default='champion', on_delete=django.db.models.deletion.PROTECT, to='api.champions', to_field='key'),
        ),
    ]
