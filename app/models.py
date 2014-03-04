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