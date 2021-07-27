
from django.contrib import admin
from django.urls import path, include

from loja import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
]