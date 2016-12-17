### -*- coding: utf-8 -*- ###

from __future__ import unicode_literals
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from image_cropping import ImageRatioField

# Create your models here.


class Article(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	text = RichTextUploadingField(verbose_name='Содержание')

	def __unicode__(self):
		return self.title


class Excursions(models.Model):
	title = models.CharField(max_length=30, verbose_name='Заголовок')
	text = RichTextUploadingField(verbose_name='Содержание')
	main = models.BooleanField(default=False, blank=True,  verbose_name='На главную')
	image = models.ImageField(upload_to='./img', verbose_name='Изображение на главную')
	cropping = ImageRatioField('image', '450x300', allow_fullsize=True)
	slide_image = models.ImageField(upload_to='./img', blank=True, verbose_name='Изображение в слайдер')
	slide_cropping = ImageRatioField('slide_image', '1000x350', allow_fullsize=True)
	slide = models.BooleanField(default=False, blank=True,  verbose_name='На слайдер')

	def __unicode__(self):
		return self.title

city_choise = (
    ('Цандрипш', 'Цандрипш'),
    ('Гагра', 'Гагра'),
    ('Гудаута', 'Гудаута'),
    ('Пицунда', 'Пицунда'),
    ('Новый Афон', 'Новый Афон'),
    ('Сухум', 'Сухум'),
)

type_choice = (
    ('Мини-отель', 'Мини-отель'),
    ('Частный дом', 'Частный дом'),
    ('Квартира', 'Квартира'),
    ('Коттедж', 'Коттедж'),
    ('Отель', 'Отель'),
)

class Houses(models.Model):
	title = models.CharField(max_length=30, verbose_name='Название')
	text = RichTextUploadingField(verbose_name='Описание')
	main = models.BooleanField(default=False, blank=True, verbose_name='На главную')
	main_img = models.ImageField(upload_to='./img', verbose_name='Изображение на главную')
	cropping = ImageRatioField('main_img', '320x240', allow_fullsize=True)
	city = models.CharField(max_length=20, choices=city_choise, verbose_name='Город')
	phone = models.IntegerField(blank=True, null=True, verbose_name='Телефон')
	house_type = models.CharField(max_length=20, choices=type_choice, verbose_name='Тип помещения') 
	price = models.IntegerField(verbose_name='Цена')
	sea = models.IntegerField(verbose_name='До моря')
	hot_w = models.BooleanField(default=False, blank=True, verbose_name='Горячая вода')
	lavatory = models.BooleanField(default=False, blank=True, verbose_name='Уборная')
	w_machine = models.BooleanField(default=False, blank=True, verbose_name='Стиральная машина')
	shower = models.BooleanField(default=False, blank=True, verbose_name='Душ')
	fridge = models.BooleanField(default=False, blank=True, verbose_name='Холодильник')
	tv = models.BooleanField(default=False, blank=True, verbose_name='Телевизор')
	internet = models.BooleanField(default=False, blank=True, verbose_name='Интернет')
	conditioner = models.BooleanField(default=False, blank=True, verbose_name='Кондиционер')
	safe = models.BooleanField(default=False, blank=True, verbose_name='Сейф')
	food =  models.BooleanField(default=False, blank=True, verbose_name='Питание')
	balcony =  models.BooleanField(default=False, blank=True, verbose_name='Балкон')
	park =  models.BooleanField(default=False, blank=True, verbose_name='Парковка')
	date_from = models.DateField(blank=True, null=True, verbose_name='Заезд')
	date_to = models.DateField(blank=True, null=True, verbose_name='Выезд')
	map = models.CharField(max_length=90, blank=True)
	map_visible = models.BooleanField(default=False, verbose_name='Показать карту на старанице')
	


	def __unicode__(self):
		if self.date_from:
			if self.date_to:
				return u'%s Заезд: %s; Выезд: %s' % (self.title, self.date_from, self.date_to)
		else:
			return self.title


class Image(models.Model):
	title = models.ForeignKey(Houses)
	images = models.ImageField(upload_to='./img', verbose_name='Фотографии')

