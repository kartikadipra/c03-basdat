from django.urls import path
from login import views
from .views import *

app_name = 'login'
urlpatterns = [
	path('', login_page, name='login'),
	# path('user_login', user_login, name='user_login')
	
	# path('home/', views.login_page, name='login_page'),
   
]

