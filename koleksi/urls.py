from django.urls import path
from .views import *

app_name = 'koleksi'
urlpatterns = [
	path('', index, name='index')
]