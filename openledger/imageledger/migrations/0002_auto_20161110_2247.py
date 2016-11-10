# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 22:47
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageledger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='tags_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=255, null=True), default=2, size=None),
            preserve_default=False,
        ),
    ]