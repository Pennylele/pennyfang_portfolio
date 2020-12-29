from django.urls import path
from . import views

app_name = 'timezone'

urlpatterns = [
	path('', views.home, name='timezone_home'),
]