from django.urls import path
from app.views import index, imagem

urlpatterns = [
    path('', index),
    path('imagem/', imagem) #faz o mesmo com o arquivo imagem
]#lista que vai receber as requisições? 