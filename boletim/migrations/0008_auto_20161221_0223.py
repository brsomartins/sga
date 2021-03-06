# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 04:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletim', '0007_auto_20161221_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='professor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='boletim.Professor'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='matricula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boletim.Matricula', verbose_name='matrícula'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='nota_maxima',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='nota máxima'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='título'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='creditos',
            field=models.IntegerField(verbose_name='créditos'),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='periodo_ideal',
            field=models.IntegerField(verbose_name='período ideal'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='periodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boletim.Periodo', verbose_name='período'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='situacao',
            field=models.CharField(choices=[('C', 'Cursando'), ('A', 'Aprovado'), ('R', 'Reprovado'), ('T', 'Trancamento')], default='C', max_length=1, verbose_name='situação'),
        ),
        migrations.AlterField(
            model_name='professor',
            name='nome_exibicao',
            field=models.CharField(max_length=200, verbose_name='nome de exibição'),
        ),
    ]
