# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 10:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_events'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matiere',
            name='seanceRealiseTemp',
        ),
    ]
