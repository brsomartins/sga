# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletim', '0008_auto_20161221_0223'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matricula',
            options={'ordering': ['periodo', 'disciplina'], 'verbose_name': 'matrícula'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'ordering': ['nome_exibicao'], 'verbose_name_plural': 'professores'},
        ),
        migrations.AddField(
            model_name='professor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome_completo',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
