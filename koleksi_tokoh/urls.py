from django.urls import path
from .views import *

app_name = 'koleksi_tokoh'
urlpatterns = [
	path('', rud_koleksi_tokoh, name='koleksi_tokoh'),
	path('create/', c_koleksi_tokoh, name='c_koleksi_tokoh'),
	path('delete/<id_koleksi>/<username_pengguna>/<nama_tokoh>/',d_koleksi_tokoh, name='d_koleksi_tokoh'),

]