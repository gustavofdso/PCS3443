from django.urls import path

from . import views

# TODO: adicionar todas as views

urlpatterns = [
    path('', views.index, name='index'),
]