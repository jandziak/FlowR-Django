# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 22:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RBlocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specification',
            old_name='name',
            new_name='param',
        ),
    ]
