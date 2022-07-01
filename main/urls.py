from django.urls import path

from . import views

# TODO: adicionar todas as views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('vendedor/create/', views.vendedor_create, name = 'vendedor-create'),
    path('vendedor/update/<int:CPF>', views.vendedor_update, name = 'vendedor-update'),
    path('vendedor/delete/<int:CPF>', views.vendedor_delete, name = 'vendedor-delete'),

    path('cliente/create/', views.cliente_create, name = 'cliente-create'),
    path('cliente/update/<int:CPF>', views.cliente_update, name = 'cliente-update'),
    path('cliente/delete/<int:CPF>', views.cliente_delete, name = 'cliente-delete'),

    path('produto/create/', views.produto_create, name = 'produto-create'),
    path('produto/update/<int:CPF>', views.produto_update, name = 'produto-update'),
    path('produto/delete/<int:CPF>', views.produto_delete, name = 'produto-delete'),

    path('venda/create/', views.venda_create, name = 'venda-create'),
    path('venda/update/<int:CPF>', views.venda_update, name = 'venda-update'),
    path('venda/delete/<int:CPF>', views.venda_delete, name = 'venda-delete'),
]