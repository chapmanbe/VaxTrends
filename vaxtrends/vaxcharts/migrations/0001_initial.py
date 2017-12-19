# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 18:37
"""
Migration 0001
"""
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Migration 0001
    """
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VaxCoverage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('vaccine', models.CharField(max_length=200)),
                ('ci_lower', models.FloatField()),
                ('ci_upper', models.FloatField()),
                ('ci', models.FloatField()),
                ('coverage', models.FloatField()),
            ],
        ),
    ]
