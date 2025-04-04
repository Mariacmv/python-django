from django.shortcuts import render #é renderizar
# # Create your views here.

def index(request):
    return render(request, 'galeria/index.html') #modifico para passar o html e a view renderiza o código

def imagem(request):
    print('Carregando a página IMAGEM!')
    return render(request, 'galeria/imagem.html')


