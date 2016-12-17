# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 03:39
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20160216_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '240x180', adapt_rotation=False, allow_fullsize=True, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='excursions',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '300x200', adapt_rotation=False, allow_fullsize=True, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='excursions',
            name='image',
            field=models.ImageField(upload_to='./img', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e'),
        ),
        migrations.AlterField(
            model_name='houses',
            name='main_img',
            field=models.ImageField(upload_to='./img', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043d\u0430 \u0433\u043b\u0430\u0432\u043d\u0443\u044e'),
        ),
    ]