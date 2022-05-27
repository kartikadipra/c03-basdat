from django.urls import path
from .views import *

app_name = 'level'
urlpatterns = [
	path('', rud_level, name='level'),
	path('create/', c_level, name='c_level'),
	path('delete/<level>/<xp>/',d_level, name='d_level'),
]
