"""Urls for urls."""

from accueil import views
from django.urls import path

ACCUEIL_INDEX_NAME = 'accueil/index'

app_name = 'accueil'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name=ACCUEIL_INDEX_NAME),
]
