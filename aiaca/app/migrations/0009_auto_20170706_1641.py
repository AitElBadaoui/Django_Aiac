# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-06 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170706_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='grade',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
