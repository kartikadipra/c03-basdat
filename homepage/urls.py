from django.urls import path
from homepage import views

app_name = 'homepage'
urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('pemain', views.homePemain, name='homePemain'),
	path('admin', views.homeAdmin, name='homeAdmin')
]
