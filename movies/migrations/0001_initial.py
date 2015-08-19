# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('release_year', models.IntegerField(blank=True)),
                ('locations', models.CharField(blank=True, max_length=200)),
                ('fun_facts', models.CharField(blank=True, max_length=500)),
                ('production_company', models.CharField(blank=True, max_length=200)),
                ('distributor', models.CharField(blank=True, max_length=200)),
                ('director', models.CharField(blank=True, max_length=100)),
                ('writer', models.CharField(blank=True, max_length=100)),
                ('actor_1', models.CharField(blank=True, max_length=100)),
                ('actor_2', models.CharField(blank=True, max_length=100)),
                ('actor_3', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('locations_details', models.CharField(max_length=200)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
