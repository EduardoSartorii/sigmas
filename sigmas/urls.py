from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    url(r'^', include('sigmas.home.urls', namespace='home')),
    url('admin/', admin.site.urls),
]
