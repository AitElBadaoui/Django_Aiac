# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_horaire_jour_total_modif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horaire_jour',
            name='Jeudi',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Jeudi_modif',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Mardi',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Mardi_modif',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Mercredi',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Mercredi_modif',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Samedi',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Samedi_modif',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Vendredi',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='Vendredi_modif',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='lundi',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='horaire_jour',
            name='lundi_modif',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
