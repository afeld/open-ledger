# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageledger', '0004_auto_20161116_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
