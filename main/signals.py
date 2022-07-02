from django.db.models import signals
from django.dispatch import receiver
from . import models

@receiver(signals.pre_save, sender = models.Venda)
def pre_save_venda(**kwargs):
    produto = models.Produto.objects.get(id = kwargs['instance'].idProduto.id)
    try:
        old = models.Venda.objects.get(id = kwargs['instance'].id)
        produto.quantidadeDisponivel -= kwargs['instance'].quantidade - old.quantidade
    except models.Venda.DoesNotExist:
        produto.quantidadeDisponivel -= kwargs['instance'].quantidade
    produto.save()

@receiver(signals.pre_delete, sender = models.Venda)
def pre_delete_venda(**kwargs):
    produto = models.Produto.objects.get(id = kwargs['instance'].idProduto.id)
    produto.quantidadeDisponivel += kwargs['instance'].quantidade
    produto.save()