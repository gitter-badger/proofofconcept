# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-09 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_fields_physics_operators_symbols'),
    ]

    operations = [
        migrations.CreateModel(
            name='Derivation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=250, null=True)),
                ('goal', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
