# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-20 18:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('va', '0004_auto_20200320_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='ques',
            name='ques_num',
            field=models.IntegerField(default=0),
        ),
    ]
