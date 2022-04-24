# Generated by Django 4.0.4 on 2022-04-24 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sporty',
            name='zeme_puvod_sportu_zkratka',
        ),
        migrations.AddField(
            model_name='hvezdy',
            name='zeme_puvod_sportu_zkratka',
            field=models.CharField(default=1, max_length=5, verbose_name='Země průvodu zkratka'),
            preserve_default=False,
        ),
    ]