from django.db.models import signals
from django.dispatch import receiver
from . import models

@receiver(signals.post_save, sender = models.Venda)
def post_save_venda(**kwargs):
    if kwargs['created']:
        produto = models.Produto.objects.get(id = kwargs['instance'].idProduto.id)
        produto.quantidadeDisponivel -= kwargs['instance'].quantidade
        produto.save()

@receiver(signals.post_delete, sender = models.Venda)
def post_delete_venda(**kwargs):
    produto = models.Produto.objects.get(id = kwargs['instance'].idProduto.id)
    produto.quantidadeDisponivel += kwargs['instance'].quantidade
    produto.save()