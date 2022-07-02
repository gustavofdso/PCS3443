from django.shortcuts import redirect, render
from . import models
from . import forms
from . import signals

# Create your views here.

def index(response):
    return render(response, "main/base.html", {"title": "Home"})

# CRUD Vendedor

def vendedor(response):
    form = forms.VendedorCreate()
    if response.method == 'POST':
        form = forms.VendedorCreate(response.POST)
        if form.is_valid():
            form.save()

    dataset = models.Vendedor.objects.all()
    return render(response, "main/vendedor.html", {"form": form, "dataset": dataset})

def vendedor_update(response, CPF):
    try: vendedor = models.Vendedor.objects.get(CPF = CPF)
    except models.Vendedor.DoesNotExist: return redirect('vendedor')
    form = forms.VendedorCreate(response.POST or None, instance = vendedor)
    if form.is_valid():
        form.save()
        return redirect('vendedor')

    return render(response, "main/crud.html", {"form": form})

def vendedor_delete(response, CPF):
    try: vendedor = models.Vendedor.objects.get(CPF = CPF)
    except models.Vendedor.DoesNotExist: return redirect('vendedor')
    vendedor.delete()
    return redirect('vendedor')

# CRUD Cliente

def cliente(response):
    form = forms.ClienteCreate()
    if response.method == 'POST':
        form = forms.ClienteCreate(response.POST)
        if form.is_valid():
            form.save()

    dataset = models.Cliente.objects.all()
    return render(response, "main/cliente.html", {"form": form, "dataset": dataset})

def cliente_update(response, CPF):
    try: cliente = models.Cliente.objects.get(CPF = CPF)
    except models.Cliente.DoesNotExist: return redirect('cliente')
    form = forms.ClienteCreate(response.POST or None, instance = cliente)
    if form.is_valid():
        form.save()
        return redirect('cliente')

    return render(response, "main/crud.html", {"form": form})

def cliente_delete(response, CPF):
    try: cliente = models.Cliente.objects.get(CPF = CPF)
    except models.Cliente.DoesNotExist: return redirect('cliente')
    cliente.delete()
    return redirect('cliente')

# CRUD Produto

def produto(response):
    form = forms.ProdutoCreate()
    if response.method == 'POST':
        form = forms.ProdutoCreate(response.POST)
        if form.is_valid():
            form.save()

    dataset = models.Produto.objects.all()
    return render(response, "main/produto.html", {"form": form, "dataset": dataset})

def produto_update(response, id):
    try: produto = models.Produto.objects.get(id = id)
    except models.Produto.DoesNotExist: return redirect('produto')
    form = forms.ProdutoCreate(response.POST or None, instance = produto)
    if form.is_valid():
        form.save()
        return redirect('produto')

    return render(response, "main/crud.html", {"form": form})

def produto_delete(response, id):
    try: produto = models.Produto.objects.get(id = id)
    except models.Produto.DoesNotExist: return redirect('produto')
    produto.delete()
    return redirect('produto')

# CRUD Venda

def venda(response):
    form = forms.VendaCreate()
    if response.method == 'POST':
        form = forms.VendaCreate(response.POST)
        if form.is_valid():
            form.save()
            
    dataset = models.Venda.objects.all()
    return render(response, "main/venda.html", {"form": form, "dataset": dataset})

def venda_update(response, id):
    try: venda = models.Venda.objects.get(id = id)
    except models.Venda.DoesNotExist: return redirect('venda')
    form = forms.VendaCreate(response.POST or None, instance = venda)
    if form.is_valid():
        form.save()
        return redirect('venda')

    return render(response, "main/crud.html", {"form": form})

def venda_delete(response, id):
    try: venda = models.Venda.objects.get(id = id)
    except models.Venda.DoesNotExist: return redirect('venda')
    venda.delete()
    return redirect('venda')