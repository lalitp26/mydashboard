# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube',
            name='priority',
            field=models.CharField(choices=[('H', 'High'), ('L', 'Low'), ('M', 'Medium')], default='M', max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
