from django.conf.urls import patterns, include, url

from app.views import call_order, order, FoodView
from django.views.generic import TemplateView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^socks/$', TemplateView.as_view(template_name='socks.html'), name='home'),
    url(r'^order/$', order),
    url(r'^call_order/$', call_order),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<site>[\w-]+)/$', FoodView.as_view()),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)
