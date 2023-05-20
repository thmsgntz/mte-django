from django.urls import path

from . import views

BLOG_INDEX_NAME = 'blog/index'

urlpatterns = [
    path('', views.index, name=BLOG_INDEX_NAME),
]
