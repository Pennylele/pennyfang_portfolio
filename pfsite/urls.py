from django.urls import path
from . import views

app_name = "pfsite"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('resume/', views.ResumeView.as_view(), name='resume')
]