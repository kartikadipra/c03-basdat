from django.urls import path
from .views import *

app_name = 'kategori_apparel'
urlpatterns = [
	path('', index, name='index')
]
