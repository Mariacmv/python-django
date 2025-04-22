from django.shortcuts import render

from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms() #instância da classe LoginForms
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    form = CadastroForms()
    return render(request, "usuarios/cadastro.html", {"form": form})
