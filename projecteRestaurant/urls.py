from django.conf.urls import patterns, include, url
from django.contrib import admin
from Restaurantapp.views import *
from Restaurantapp import views

urlpatterns = patterns('',

    url(r'^$',mainpage),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/new/$', views.new_restaurant, name='new_restaurant'),
    url(r'^post/reservar/$', views.reservar_restaurant, name='reservar_restaurant'),
    url(r'^delete_restaurant/(?P<rest_pk>\d+)/$', views.delete_restaurant, name='delete_restaurant')

)
