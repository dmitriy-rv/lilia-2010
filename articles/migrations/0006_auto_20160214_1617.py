# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20160214_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houses',
            name='city',
            field=models.CharField(choices=[('\u0426\u0430\u043d\u0434\u0440\u0438\u043f\u0448', '\u0426\u0430\u043d\u0434\u0440\u0438\u043f\u0448'), ('\u0413\u0430\u0433\u0440\u0430', '\u0413\u0430\u0433\u0440\u0430'), ('\u0413\u0443\u0434\u0430\u0443\u0442\u0430', '\u0413\u0443\u0434\u0430\u0443\u0442\u0430'), ('\u041f\u0438\u0446\u0443\u043d\u0434\u0430', '\u041f\u0438\u0446\u0443\u043d\u0434\u0430'), ('\u041d\u043e\u0432\u044b\u0439 \u0410\u0444\u043e\u043d', '\u041d\u043e\u0432\u044b\u0439 \u0410\u0444\u043e\u043d'), ('\u0421\u0443\u0445\u0443\u043c', '\u0421\u0443\u0445\u0443\u043c')], max_length=1, verbose_name='\u0413\u043e\u0440\u043e\u0434'),
        ),
    ]