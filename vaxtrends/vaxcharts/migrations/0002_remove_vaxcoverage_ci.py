# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 18:46
"""
Migration 0002
"""
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    """
    Migration 0002
    """
    dependencies = [
        ('vaxcharts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaxcoverage',
            name='ci',
        ),
    ]
