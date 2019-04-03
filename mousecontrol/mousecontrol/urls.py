from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from runface import views as qq

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^runface/',include('runface.urls')),
]
