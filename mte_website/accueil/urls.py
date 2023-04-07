"""Urls for urls."""

from accueil import views
from django.urls import path

app_name = 'accueil'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]
