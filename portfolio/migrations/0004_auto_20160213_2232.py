# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20160213_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]