from django.shortcuts import redirect, render
from . import models
from . import forms

# Create your views here.

def index(response):
    return render(response, "main/base.html", {"title": "Home"})

# CRUD Vendedor

def vendedor_create(response):
    form = forms.VendedorCreate()
    if response.method == 'POST':
        form = forms.VendedorCreate(response.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(response, "main/forms.html", {"form": form})

def vendedor_update(response, CPF):
    try: vendedor = models.Vendedor.objects.get(CPF = CPF)
    except models.Vendedor.DoesNotExist: return redirect('index')
    form = forms.VendedorCreate(response.POST or None, instance = vendedor)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(response, "main/forms.html", {"form": form})

def vendedor_delete(response, CPF):
    try: vendedor = models.Vendedor.objects.get(CPF = CPF)
    except models.Vendedor.DoesNotExist: return redirect('index')
    vendedor.delete()
    return redirect('index')

# CRUD Clientes

def cliente_create(response):
    form = forms.ClienteCreate()
    if response.method == 'POST':
        form = forms.ClienteCreate(response.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(response, "main/forms.html", {"form": form})

def cliente_update(response, CPF):
    try: cliente = models.Cliente.objects.get(CPF = CPF)
    except models.Cliente.DoesNotExist: return redirect('index')
    form = forms.ClienteCreate(response.POST or None, instance = cliente)
    if form.is_valid():
        form.save()
        return redirect('index')

    return render(response, "main/forms.html", {"form": form})

def cliente_delete(response, CPF):
    try: cliente = models.Cliente.objects.get(CPF = CPF)
    except models.Cliente.DoesNotExist: return redirect('index')
    cliente.delete()
    return redirect('index')

# CRUD Produto

# CRUD Vendas
