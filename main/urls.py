from django.urls import path

from . import views

# TODO: adicionar todas as views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('vendedor/', views.vendedor, name = 'vendedor'),
    path('cliente/', views.vendedor, name = 'cliente'),
    path('produto/', views.vendedor, name = 'produto'),
    path('venda/', views.vendedor, name = 'venda')
]