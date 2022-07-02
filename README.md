# PCS3443
Laboratório de Engenharia de Software I (2022)

Escola Politécnica da USP

Projeto de um sistema de controle de dados da Loja de 1,99.

Alunos:
* Alessandro Jiã Iong Li - 10291791
* Felipe Daniel Rodrigues Marques - 11325312
* Gustavo Freitas de Sá Oliveira - 11261062
* Rafael Xavier Souza Lattari - 9853130
* Roberta Boaventura Andrade - 11260832

--------------------

### Descrição do projeto

O projeto consiste num sistema capaz de guardar informações sobre operações realizada numa pequena loja. Ele foi projetado para ser usado por funcionários da loja, para fazer cadastro e manutenção dos dados. São implementados os CRUDs:

* Vendedor - nesse modelo, são guardadas informações gerais sobre os funcionários da loja. A tabela possui os seguintes campos:
    * `CPF` => IntegerField, primary_key = True
    * `nome` => CharField, max_length = 300
    * `email` => CharField, max_length = 300
    * `telefone` => IntegerField
    * `dataNascimento` => DateField
    * `dataAdmissao` => DateField
    * `salarioBruto` => DecimalField, max_digits = 10, decimal_places = 2

* Cliente - nesse modelo, são guardadas informações gerais sobre os clientes da loja. A tabela possui os seguintes campos:
    * `CPF` => IntegerField, primary_key = True
    * `nome` => CharField, max_length = 300
    * `email` => CharField, max_length = 300
    * `telefone` => IntegerField
    * `dataNascimento` => DateField
    * `dataCadastro` => DateField

* Produto - nesse modelo, são guardadas informações sobre os produtos vendidos pela loja. A tabela possui os seguintes campos:
    * `id` => AutoField, primary_key = True
    * `nome` => CharField, max_length = 300, unique = True
    * `quantidadeDisponivel` => IntegerField
    * `precoUnitario` => DecimalField, max_digits = 10, decimal_places = 2

* Venda - nesse modelo, são guardadas informações sobre os produtos vendas realizadas. A tabela possui os seguintes campos:
    * `id` => AutoField, primary_key = True
    * `CPFVendedor` => ForeignKey references Vendedor, on_delete = CASCADE
    * `CPFCliente` => ForeignKey references Cliente, on_delete = CASCADE
    * `idProduto` => ForeignKey references Produto, on_delete = CASCADE
    * `data` => DateField
    * `quantidade` => IntegerField
    * `precoUnitario` => DecimalField, max_digits = 10, decimal_places = 2

Para cada uma dessas CRUDs, é permitido aos funcionários da loja fazer todas as manipulações necessárias: realizar o cadastro de novas linhas, consultas, alterações e deleções. O sistema foi construído de forma a ser auto-explicativo, com botões simples para manipulação da base de dados.

--------------------

### Utilização do sistema

Para o funcionamento do sistema desenvolvido, é necessário um interpretador de Python 3.8.13 e a biblioteca `django 4.0.5`. A hospedagem do servidor que contém a base de dados pode ser feita com o seguinte comando:

```
python manage.py runserver
```

O servidor será hospedado em localhost, a partir do qual todas as demais páginas do projeto podem ser acessadas.

A execução do script de testes de atualização da quantidade de produtos pode ser feita com o seguinte comando:

```
python manage.py test main.tests
```

Para acessar a página de administrador, deve-se usar as credenciais:

Login: gustavo

Senha: gustavo