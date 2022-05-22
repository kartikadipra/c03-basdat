from django.urls import path
from .views import *

app_name = 'koleksi_tokoh'
urlpatterns = [
	path('', index, name='index')
]