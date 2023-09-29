from django.urls import path
from . import views

urlpatterns = [
    path('', views.plataforma, name='plataforma'),

    path('listar/', views.listar_transacoes, name='listar_transacoes'),
    path('adicionar/', views.adicionar_transacao, name='adicionar_transacao'),
]
