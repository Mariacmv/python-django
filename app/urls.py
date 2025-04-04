from django.urls import path
from app.views import index, imagem

urlpatterns = [
    path('', index, name='index'), #determino um nome a url
    path('imagem/', imagem, name='imagem') #faz o mesmo com o arquivo imagem. Passo esse nome e devolvo ao html para que ele entenda a página
]#lista que vai receber as requisições? 