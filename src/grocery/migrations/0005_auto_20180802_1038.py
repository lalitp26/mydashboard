# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-02 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0004_auto_20180802_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='currency',
            field=models.CharField(choices=[('inr', 'inr'), ('dollar', 'dollar')], default='inr', max_length=10),
        ),
    ]
