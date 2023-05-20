from django.urls import path

from . import views

ANNUAIRE_INDEX_NAME = 'annuaire/index'

urlpatterns = [
    path('', views.index, name=ANNUAIRE_INDEX_NAME),
]
