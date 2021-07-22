from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('useful_links', views.useful_links, name="useful_links"),
]
