# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-10-31 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20181031_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviewatchlist',
            name='list_of_movies',
            field=models.TextField(null=True),
        ),
    ]
