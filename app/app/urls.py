from django.conf.urls import patterns, include, url
from django.contrib import admin

from serviceApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^serviceApp/', include('serviceApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^openid/(.*)', SessionConsumer()),
)
