# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaxcharts', '0004_diseasechoices_vaxincidencerate'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaxHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=200)),
                ('current_vaccine', models.CharField(max_length=200)),
                ('first_available', models.IntegerField()),
            ],
        ),
    ]