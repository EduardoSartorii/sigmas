from django.conf.urls import include, url
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
from .views import *


app_name = 'home'

urlpatterns = [
	url(r'^$', do_login ,name='do_login'),
	url(r'^logout/$', do_logout ,name='do_logout'),
	url(r'^home/$', home ,name='home'),
	url(r'^home/produtos/$',captura_products, name='produtos'),
]
