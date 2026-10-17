from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_excursoes, name='lista_excursoes'),
    path('excursao/nova/', views.criar_excursao, name='criar_excursao'),
    path('excursao/<int:pk>/', views.detalhe_excursao, name='detalhe_excursao'),
    path('excursao/<int:pk>/editar/', views.editar_excursao, name='editar_excursao'),
    path('excursao/<int:pk>/excluir/', views.excluir_excursao, name='excluir_excursao'),
    
    path('passageiro/novo/', views.criar_passageiro, name='criar_passageiro'),
    path('passageiro/<int:pk>/editar/', views.editar_passageiro, name='editar_passageiro'),
    path('passageiro/<int:pk>/excluir/', views.excluir_passageiro, name='excluir_passageiro'),
    path('login/', views.login_view, name='login'),
]