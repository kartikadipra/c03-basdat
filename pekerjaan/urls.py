from django.urls import path
from .views import *
from pekerjaan import views

app_name = 'pekerjaan'
urlpatterns = [
	path('', read, name='read'),
	path('create/', create_pekerjaan, name='create_pekerjaan'),
	path('update', update, name='update'),
	path('delete/<str:nama_pekerjaan>/', views.delete, name='delete'),
]