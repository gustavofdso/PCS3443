from django import forms
from . import models

class VendedorForm(forms.ModelForm):
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
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'dataAdmissao': forms.DateInput(attrs={'type': 'date'})
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'
        labels = {
            'CPF': 'CPF',
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'dataNascimento': 'Data de nascimento',
            'dataCadastro': 'Data de cadastro'
        }
        widgets = {
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'dataCadastro': forms.DateInput(attrs={'type': 'date'})
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = models.Produto
        fields = '__all__'
        labels = {
            'nome': 'Nome',
            'quantidadeDisponivel': 'Quantidade disponível',
            'precoUnitario': 'Preço unitário'
        }

class VendaForm(forms.ModelForm):
    class Meta:
        model = models.Venda
        fields = '__all__'
        labels = {
            'CPFVendedor': 'CPF do vendedor',
            'CPFCliente': 'CPF do cliente',
            'idProduto': 'Nome do produto',
            'data': 'Data da venda',
            'quantidade': 'Quantidade',
            'precoUnitario': 'Preço unitário'
        }
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }