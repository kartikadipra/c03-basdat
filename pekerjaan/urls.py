from django.urls import path
from .views import *

app_name = 'pekerjaan'
urlpatterns = [
	path('', read, name='read'),
	path('create', create_pekerjaan, name='create_pekerjaan')
]