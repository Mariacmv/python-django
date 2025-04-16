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

def buscar(request): #3- Busca os itens do banco de dados
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True) 
    
    #4- Filtra os dados de acordo com a busca
    if "buscar" in request.GET: #verifico se as informações estão no request do usuário
        nome_a_buscar = request.GET['buscar'] #Guardo as informações do request do usuário (o que ele digitou para a procura) 
        if nome_a_buscar: #se existir alguma busca
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #busca se existe dentro do nome a buscar alguma semelhança com algum item dentro do site
    
    #5- Passa para o render
    return render(request, "app/buscar.html", {"cards":fotografias}) 
