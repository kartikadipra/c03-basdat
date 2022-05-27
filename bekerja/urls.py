from django.urls import path
from .views import *

app_name = 'bekerja'
urlpatterns = [
	path('', read, name='read'),
	path('create', create, name='create')
]