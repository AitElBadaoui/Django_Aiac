# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-31 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verrou',
            field=models.BooleanField(default=False),
        ),
    ]