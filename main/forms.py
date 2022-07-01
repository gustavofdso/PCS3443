from django import forms
from . import models

class VendedorCreate(forms.ModelForm):
    class Meta:
        model = models.Vendedor
        fields = '__all__'
        labels = {
            'CPF': 'CPF',
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de nascimento',
            'dataAdmissao': 'Data de admissão',
            'salarioBruto': 'Salário bruto'
        }
        widgets = {
            'dataNascimento': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'}),
            'dataAdmissao': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'}),
        }

class ClienteCreate(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'
        exclude = ['dataCadastro']
        labels = {
            'CPF': 'CPF',
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de nascimento'
        }
        widgets = {
            'dataNascimento': forms.DateInput(format=('%d/%m/%Y'), attrs={'type': 'date'}),
        }

class ProdutoCreate(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'quantidadeDisponivel': 'Quantidade disponível',
            'precoUnitario': 'Preço unitário'
        }


class VendaCreate(forms.ModelForm):
    class Meta:
        model = models.Venda
        fields = '__all__'
        exclude = ['data']
        labels = {
            'CPFVendedor': 'CPF do vendedor',
            'CPFCliente': 'CPF do cliente',
            'idProduto': 'Id do produto',
            'quantidade': 'Quantidade',
            'precoUnitario': 'Preço unitário'
        }