from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # renderiza o HTML
    path('atividades/', views.atividades),
    path('atividades/<int:id>/', views.atividade_detalhe),
]
