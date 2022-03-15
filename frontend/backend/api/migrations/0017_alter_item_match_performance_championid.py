# Generated by Django 3.2.6 on 2021-08-31 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_item_match_performance_championid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_match_performance',
            name='championId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.champions', to_field='key'),
        ),
    ]
