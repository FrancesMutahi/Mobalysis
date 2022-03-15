# Generated by Django 3.1.2 on 2021-10-27 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0050_auto_20211025_2126"),
    ]

    operations = [
        migrations.CreateModel(
            name="championsummoners",
            fields=[
                ("summonername", models.TextField(blank=False, null=False)),
                (
                    "championid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.champions"
                    ),
                ),
                ("platformid", models.TextField(blank=True, max_length=100, null=True)),
                ("tier", models.TextField(blank=False, null=False)),
                ("winrate", models.DecimalField(max_digits=5, decimal_places=2)),
                ("rank", models.IntegerField(blank=True, null=True)),
            ],
        )
    ]
