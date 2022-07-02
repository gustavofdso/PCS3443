from django import test
from . import models, signals

import datetime

# Create your tests here.

class VendaTestCase(test.TestCase):
    def setUp(self):
        models.Vendedor.objects.create(
            CPF = 12345678900,
            nome = 'Gustavo',
            email = 'gustavo@email.com',
            telefone = 123456789,
            dataNascimento = datetime.date(2000, 1, 1),
            dataAdmissao = datetime.date(2000, 1, 1),
            salarioBruto = 10000.00
        )
        models.Cliente.objects.create(
            CPF = 98765432100,
            nome = 'Roberta',
            email = 'roberta@email.com',
            telefone = 123456789,
            dataNascimento = datetime.date(2000, 1, 1),
            dataCadastro = datetime.date(2000, 1, 1)
        )
        models.Produto.objects.create(
            nome = 'Coca-Cola',
            quantidadeDisponivel = 100,
            precoUnitario = 1.99
        )

    def test_vendas(self):
        vendedor = models.Vendedor.objects.get(CPF = 12345678900)
        cliente = models.Cliente.objects.get(CPF = 98765432100)
        produto = models.Produto.objects.get(nome = 'Coca-Cola')

        # Testando criação de venda
        venda = models.Venda.objects.create(
            CPFVendedor = vendedor,
            CPFCliente = cliente,
            idProduto = produto,
            data = datetime.date(2010, 1, 1),
            quantidade = 10,
            precoUnitario = 1.99
        )
        produto.refresh_from_db()
        self.assertEqual(produto.quantidadeDisponivel, 90)

        # Testando atualização de venda
        venda.quantidade -= 5
        venda.save()
        produto.refresh_from_db()
        self.assertEqual(produto.quantidadeDisponivel, 95)

        # Testando deleção de venda
        venda.delete()
        produto.refresh_from_db()
        self.assertEqual(produto.quantidadeDisponivel, 100)