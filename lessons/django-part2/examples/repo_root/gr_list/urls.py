from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.post_list, name='main'),
    )