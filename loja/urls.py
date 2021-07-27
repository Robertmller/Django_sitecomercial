from django.urls import path, include
from .views import index, contato, sobre, servicos
from loja import views


urlpatterns = [
	path('index.html', index, name='index'),
	path('contato.html', contato, name='contato'),
	path('sobre.html', sobre, name='sobre'),
	path('servicos.html', servicos, name='serviços')

]