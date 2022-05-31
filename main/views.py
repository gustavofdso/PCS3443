from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

# TODO: criar HTML template e alterar para CRUDs
# TODO: colocar forms de cada CRUD, codar os diagramas de sequecia
# TODO: gets e posts

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

# CRUD Vendedor

def cadastrar_vendedor(response):
    # HTML com form de cadastro

    # vendedor = models.Vendedor(
    #     CPF = CPF,
    #     nome = nome,
    #     email = email,
    #     telefone = telefone,
    #     dataNascimento = dataNascimento,
    #     dataAdmissao = dataAdmissao,
    #     salarioBruto = salarioBruto
    # )
    # POST INSERT
    return HttpResponse(response)
    

def consultar_vendedor(response):
    # GET vendedor
    # vendedor = models.Vendedor.objects.get(CPF = CPF)
    
    return HttpResponse(response)

def editar_vendedor(response):
    # GET vendedor
    # vendedor = models.Vendedor.objects.get(CPF = CPF)
    
    # Atualizar dados
    # vendedor.nome = nome

    # vendedor.save()

    # POST UPDATE
    
    return HttpResponse(response)

def remover_vendedor(response):
    # GET vendedor
    # vendedor = models.Vendedor.objects.get(CPF = CPF)

    # POST DELETE
    
    return HttpResponse(response)

# REPETIR para todos abaixo

################################################################

# CRUD Clientes

def cadastrar_cliente(response):
    pass

def consultar_cliente(response):
    pass

def editar_cliente(response):
    pass

def remover_cliente(response):
    pass

# CRUD Produto

def cadastrar_produto(response):
    pass

def consultar_produto(response):
    pass

def editar_produto(response):
    pass

def remover_produto(response):
    pass

# CRUD Vendas

def cadastrar_venda(response):
    pass

def consultar_venda(response):
    pass

def editar_venda(response):
    pass

def remover_venda(response):
    pass