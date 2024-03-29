from django.db import models

# Create your models here.

class Vendedor(models.Model):
    CPF = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 300)
    telefone = models.IntegerField()
    dataNascimento = models.DateField()
    dataAdmissao = models.DateField()
    salarioBruto = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return str(self.CPF)

class Cliente(models.Model):
    CPF = models.IntegerField(primary_key = True)
    nome = models.CharField(max_length = 300)
    email = models.EmailField(max_length = 300, null = True)
    telefone = models.IntegerField(null = True)
    dataNascimento = models.DateField(null = True)
    dataCadastro = models.DateField()

    def __str__(self):
        return str(self.CPF)

    def get_elegibilidade(self):
        vendas = Venda.objects.filter(CPFCliente = self.CPF).count()
        if vendas % 5 == 0: return 'SIM'
        else: return 'NÃO'

class Produto(models.Model):
    id = models.AutoField(primary_key = True)
    nome = models.CharField(max_length = 300, unique = True)
    quantidadeDisponivel = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return str(self.nome)

class Venda(models.Model):
    id = models.AutoField(primary_key = True)
    CPFVendedor = models.ForeignKey(Vendedor, on_delete = models.SET_NULL)
    CPFCliente = models.ForeignKey(Cliente, on_delete = models.SET_NULL)
    idProduto = models.ForeignKey(Produto, on_delete = models.SET_NULL)
    data = models.DateField()
    quantidade = models.IntegerField()
    precoUnitario = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return str(self.id)
