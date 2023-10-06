from django.urls import path
from . import views

urlpatterns = [
    path('', views.plataforma, name='plataforma'),

    path('listar/', views.listar_transacoes, name='listar_transacoes'),
    path('adicionar/', views.adicionar_transacao, name='adicionar_transacao'),
    path('editar/<int:pk>', views.editar_transacao, name='editar_transacao'),
    path('apagar/<int:pk>', views.apagar_transacao, name='apagar_transacao'),
]
