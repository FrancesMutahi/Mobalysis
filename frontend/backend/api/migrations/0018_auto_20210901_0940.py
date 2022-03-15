# Generated by Django 3.2.6 on 2021-09-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_item_match_performance_championid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item_match_performance',
            old_name='regionId',
            new_name='platformId',
        ),
        migrations.RemoveField(
            model_name='item_match_performance',
            name='picks',
        ),
        migrations.RemoveField(
            model_name='regions',
            name='id',
        ),
        migrations.RemoveField(
            model_name='regions',
            name='regionName',
        ),
        migrations.AlterField(
            model_name='item_match_performance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='regions',
            name='platformId',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]