__author__ = 'vampire'
from django.contrib import admin

from app.models import CallOrder, Order, Target

admin.site.register(CallOrder)
admin.site.register(Order)
admin.site.register(Target)