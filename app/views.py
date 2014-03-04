# coding: utf-8
# Create your views here.
from app.models import CallOrder, Order
from django.core.mail import send_mail
from django.http import HttpResponse

def call_order(request):
    if 'name' in request.POST and 'phone' in request.POST:
        co = CallOrder.objects.create(
            name = request.POST['name'],
            phone = request.POST['phone']
        )
#        send_mail(u'Новая заявка на звонок', u'{}\n{}'.format(
#            request.POST['name'],request.POST['phone']
#        ),'info@socks.oldlord.ru', ['lifanov.a.v@gmail.com'])
    return HttpResponse('OK')

def order(request):
    if 'name' in request.POST and 'phone' in request.POST and 'email' in request.POST:
        co = Order.objects.create(
            name = request.POST['name'],
            phone = request.POST['phone'],
            email = request.POST['email']
        )
#        send_mail(u'Новая заявка', u'{}\n{}\n{}'.format(
#            request.POST['name'],request.POST['phone'], request.POST['email']
#        ),'info@socks.oldlord.ru', ['lifanov.a.v@gmail.com'])
    return HttpResponse('OK')