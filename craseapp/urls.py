from django.urls import path
from . import views

urlpatterns = [
    # Rota de Consulta Dinâmica (Página principal do app: /crase/)
    path('', views.consulta_dinamica, name='consulta_dinamica'),

    # Rota de Listagem Estática (/crase/listagem/)
    path('listagem/', views.validar_crase, name='validar_crase'),
]