# Generated by Django 5.0.6 on 2024-05-27 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_region_district'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regions'},
        ),
    ]
