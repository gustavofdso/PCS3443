from django.db import models

# Create your models here.

class Vendedor(models.Model):
    CPF = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 300, default = '')
    email = models.CharField(max_length = 300)
    telefone = models.IntegerField()
    dataNascimento = models.DateField()
    dataAdmissao = models.DateField()
    salarioBruto = models.DecimalField(max_digits = 10, decimal_places = 2)

class Cliente(models.Model):
    CPF = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 300, default = '')
    email = models.CharField(max_length = 300, null = True)
    telefone = models.IntegerField(null = True)
    dataNascimento = models.DateField(null = True)
    dataCadastro = models.DateField()
    
class Produto(models.Model):
    nome = models.CharField(max_length = 300, default = '')
    quantidadeDisponivel = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)

class Venda(models.Model):
    CPFVendedor = models.ForeignKey(Vendedor, on_delete = models.CASCADE)
    CPFCliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    idProduto = models.ForeignKey(Produto, on_delete = models.CASCADE)
    data = models.DateField()
    quantidade = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)