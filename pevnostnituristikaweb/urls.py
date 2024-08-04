from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('museum/create', views.MuseumCreateView.as_view(), name='museum_create'),
]
