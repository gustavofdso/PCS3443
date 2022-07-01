from django.urls import path

from . import views

# TODO: adicionar todas as views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),

    path('vendedor/', views.vendedor, name = 'vendedor'),
    path('vendedor/update/<int:CPF>', views.vendedor_update, name = 'vendedor-update'),
    path('vendedor/delete/<int:CPF>', views.vendedor_delete, name = 'vendedor-delete'),

    path('cliente/', views.cliente, name = 'cliente'),
    path('cliente/update/<int:CPF>', views.cliente_update, name = 'cliente-update'),
    path('cliente/delete/<int:CPF>', views.cliente_delete, name = 'cliente-delete'),

    path('produto/', views.produto, name = 'produto'),
    path('produto/update/<int:id>', views.produto_update, name = 'produto-update'),
    path('produto/delete/<int:id>', views.produto_delete, name = 'produto-delete'),

    path('venda/', views.venda, name = 'venda'),
    path('venda/update/<int:CPF>', views.venda_update, name = 'venda-update'),
    path('venda/delete/<int:CPF>', views.venda_delete, name = 'venda-delete'),
]