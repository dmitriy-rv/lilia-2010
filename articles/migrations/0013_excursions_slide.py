# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20160219_0554'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursions',
            name='slide',
            field=models.BooleanField(default=False, verbose_name='\u041d\u0430 \u0441\u043b\u0430\u0439\u0434\u0435\u0440'),
        ),
    ]
