# Generated by Django 3.1.2 on 2021-11-22 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0066_auto_20211116_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillorders',
            name='spell_1_level_6',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='skillorders',
            name='spell_2_level_6',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='skillorders',
            name='spell_3_level_6',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='skillorders',
            name='spell_4_level_4',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='skillorders',
            name='spell_4_level_5',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='skillorders',
            name='spell_4_level_6',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
    ]
