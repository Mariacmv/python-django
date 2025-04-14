from django.db import models
from datetime import datetime

class Fotografia(models.Model): #herda a biblioteca
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]#lista de tuplas porque charfield só entende tuplas
    
    nome = models.CharField(max_length=100, null=False, blank=False) #nome será uma string e defino a quantidade de caracteres que os nomes podem assumir. Não pode não ter informação e não pode conter string vazia
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False) #textfield porque é maior
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicada = models.BooleanField(default=False) #para o usuário adicionar itens ao site. É padrão false
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)#incrementando a data de adição
    
    #uma boa prática é devolver o nome de cada um dos itens através de uma função
    def __str__(self):
        return f'Fotografia [nome={self.nome}]'
    

