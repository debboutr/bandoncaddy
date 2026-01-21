from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/', views.detail, name='detail'),
    path('add/', views.add_work, name='add_work'),
    path('player/add/', views.add_person, name='add_person'),
]   
