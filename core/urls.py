from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.cliente_list, name='cliente_list'),
    path('clientes/novo/', views.cliente_form, name='cliente_create'),
    path('clientes/<int:id>/', views.cliente_form, name='cliente_update'),

    path('produtos/', views.produto_list, name='produto_list'),
    path('produtos/novo/', views.produto_form, name='produto_create'),
    path('produtos/<int:id>/', views.produto_form, name='produto_update'),

    path('vendas/', views.vendas, name='vendas'),

]
