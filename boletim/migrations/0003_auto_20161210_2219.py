# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-11 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletim', '0002_auto_20161210_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
