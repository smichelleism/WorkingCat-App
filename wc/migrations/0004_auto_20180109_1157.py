# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-09 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wc', '0003_auto_20180108_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='source',
            field=models.CharField(blank=True, choices=[('U', 'Unknown'), ('TNR', 'TNR'), ('Kindergarden', 'Kindergarden'), ('LAAS', 'LAAS'), ('Best Friends', 'Best Friends')], default='U', max_length=15, null=True),
        ),
    ]
