# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0005_auto_20180109_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='source',
            field=models.CharField(blank=True, choices=[('Kindergarden', 'Kindergarden'), ('Best Friends', 'Best Friends'), ('TNR', 'TNR'), ('LAAS', 'LAAS'), ('U', 'Unknown')], default='U', max_length=15, null=True),
        ),
    ]
