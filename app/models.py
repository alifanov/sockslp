# coding: utf-8
from django.db import models

# Create your models here.
class CallOrder(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'Имя')
    phone = models.CharField(max_length=100, verbose_name=u'Телефон')
    created = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)

    def __unicode__(self):
        return u'{} -- {}: {}'.format(self.created, self.name, self.phone)

    class Meta:
        verbose_name = u'Заказ звонка'
        verbose_name_plural = u'Заказы звонка'


class Order(models.Model):
    name = models.CharField(max_length=256, verbose_name=u'Имя')
    phone = models.CharField(max_length=100, verbose_name=u'Телефон')
    email = models.CharField(max_length=256, verbose_name=u'Email')
    created = models.DateTimeField(verbose_name=u'Дата создания', auto_now_add=True)

    def __unicode__(self):
        return u'{} -- [{}]({}): {}'.format(self.created, self.email, self.name, self.phone)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'


class Target(models.Model):
    sitename = models.CharField(max_length=100, verbose_name=u'Имя сайта')
    title = models.CharField(max_length=256, verbose_name=u'Title для Landing Page')
    description = models.TextField(verbose_name=u'Описание')
    banner = models.ImageField(verbose_name=u'Картинка', upload_to='upload/')
    banner_text = models.TextField(verbose_name=u'Текст для баннера')
    price = models.CharField(max_length=100)
    sad_pet = models.ImageField(upload_to='upload/', verbose_name=u'Печальное животное')
    nice_pet = models.ImageField(upload_to='upload/', verbose_name=u'Радостное животное')
    period = models.CharField(max_length=100, verbose_name=u'Период')

    def __unicode__(self):
        return self.sitename

    class Meta:
        verbose_name = u'Цель'
        verbose_name_plural = u'Цели'