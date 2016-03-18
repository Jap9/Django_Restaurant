from django.conf.urls import patterns, include, url
from django.contrib import admin
from Restaurantapp.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projecteRestaurant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',mainpage),
    url(r'^admin/', include(admin.site.urls)),
)
