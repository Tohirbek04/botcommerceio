# Generated by Django 5.0.6 on 2024-05-27 07:58

import django.contrib.postgres.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_alter_region_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='id',
            field=models.UUIDField(db_default=django.contrib.postgres.functions.RandomUUID(), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.UUIDField(db_default=django.contrib.postgres.functions.RandomUUID(), primary_key=True, serialize=False),
        ),
    ]