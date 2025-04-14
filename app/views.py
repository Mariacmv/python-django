from django.shortcuts import render, get_object_or_404 #é renderizar
from app.models import Fotografia #importo todos os objetos de models
# # Create your views here.

def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) #coloquei uma lista com todos os objetos criados em model
    print('Carregando a página INDEX!')
    return render(request, 'app/index.html', {"cards": fotografias}) #modifico para passar o html e a view renderiza o código

def imagem(request, foto_id): #função view
    print('Carregando a página IMAGEM!')
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'app/imagem.html', {"fotografia": fotografia})


