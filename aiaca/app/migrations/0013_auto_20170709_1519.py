# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-09 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_etudiant_cne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='Cne',
            field=models.CharField(max_length=25),
        ),
    ]
