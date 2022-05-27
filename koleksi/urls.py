from django.urls import path
from .views import *

app_name = 'koleksi'
urlpatterns = [
	path('', rud_koleksi, name='koleksi'),
	path('create/', c_koleksi, name='c_koleksi'),
	path('delete/<id>/<harga>/',d_koleksi, name='d_koleksi'),
]