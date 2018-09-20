from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<str:f_name>/', views.bio, name='bio'),
]
