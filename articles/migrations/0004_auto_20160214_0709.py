# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_excursions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursions',
            name='main_img',
            field=models.ImageField(upload_to='./mysite/static/img', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e'),
        ),
    ]
