# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-26 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160426_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='percent',
            field=models.IntegerField(),
        ),
    ]
