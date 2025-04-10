from django.shortcuts import render #é renderizar
from app.models import Fotografia #importo todos os objetos de models
# # Create your views here.

def index(request):
    fotografias = Fotografia.objects.all() #coloquei uma lista com todos os objetos criados em model
    print('Carregando a página INDEX!')
    return render(request, 'app/index.html', {"cards": fotografias}) #modifico para passar o html e a view renderiza o código

def imagem(request):
    print('Carregando a página IMAGEM!')
    return render(request, 'app/imagem.html')


