from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),

    # CRUD Vendedor
    path('vendedor/', views.vendedor, name = 'vendedor'),
    path('vendedor/update/<int:CPF>', views.vendedor_update, name = 'vendedor-update'),
    path('vendedor/delete/<int:CPF>', views.vendedor_delete, name = 'vendedor-delete'),

    # CRUD Cliente
    path('cliente/', views.cliente, name = 'cliente'),
    path('cliente/update/<int:CPF>', views.cliente_update, name = 'cliente-update'),
    path('cliente/delete/<int:CPF>', views.cliente_delete, name = 'cliente-delete'),

    # CRUD Produto
    path('produto/', views.produto, name = 'produto'),
    path('produto/update/<int:id>', views.produto_update, name = 'produto-update'),
    path('produto/delete/<int:id>', views.produto_delete, name = 'produto-delete'),

    # CRUD Venda
    path('venda/', views.venda, name = 'venda'),
    path('venda/update/<int:id>/', views.venda_update, name = 'venda-update'),
    path('venda/delete/<int:id>/', views.venda_delete, name = 'venda-delete'),
]