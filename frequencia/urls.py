from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), # <-- Adiciona esta linha
    path('viagens/', views.relacao_viagens, name='relacao_viagens'),
    path('viagens/nova/', views.nova_viagem, name='nova_viagem'),
    path('viagens/<int:pk>/', views.detalhe_viagem, name='detalhe_viagem'),
    path('passageiros/novo/', views.novo_passageiro, name='novo_passageiro'),
    path('passageiros/<int:pk>/', views.detalhe_passageiro, name='detalhe_passageiro'),
    path('viagens/<int:pk>/editar/', views.editar_viagem, name='editar_viagem'),
    path('viagens/<int:pk>/deletar/', views.deletar_viagem, name='deletar_viagem'),
]