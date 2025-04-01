from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'galeria/index.html') #modifico para passar o html e a view renderiza o código

def imagem(request):
    return render(request, 'galeria/imagem.html')