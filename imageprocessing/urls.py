from django.urls import path
from .views import processar_imagem

urlpatterns = [
    path('processar_imagem/', processar_imagem, name='processar_imagem'),
]


