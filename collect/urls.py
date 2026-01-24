from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/", views.detail, name="detail"),
    path("loop/add/", views.add_loop, name="add_loop"),
    path("loop/edit/<int:pk>", views.edit_loop, name="edit_loop"),
    path("player/add/", views.add_person, name="add_person"),
    path("player/edit/<int:pk>", views.edit_person, name="edit_person"),
]
