# Generated by Django 3.2.6 on 2021-09-06 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0025_summoner"),
    ]

    operations = [
        migrations.AddField(
            model_name="champion_match_performance",
            name="tierId",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="api.ranks",
            ),
        ),
    ]
