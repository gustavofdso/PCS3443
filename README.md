# PCS3443
Laboratório de Engenharia de Software I (2022)

Escola Politécnica da USP

Projeto de um sistema de controle de dados de uma Loja de 1,99.

Alunos:
* Alessandro Jiã Iong Li - 10291791
* Felipe Daniel Rodrigues Marques - 11325312
* Gustavo Freitas de Sá Oliveira - 11261062
* Rafael Xavier Souza Lattari - 9853130
* Roberta Boaventura Andrade - 11260832

--------------------

### Utilização do sistema

Para o funcionamento do sistema desenvolvido, é necessário um interpretador de Python 3.8.13 e a biblioteca `django 4.0.5`. Para hospedar o servidor que contém a base de dados, na pasta do projeto, deve-se executar:

```
python manage.py runserver
```

O servidor deve ser hospedado na URL http://127.0.0.1:8000/, A partir do qual todas as demais páginas do projeto podem ser acessadas.

Para confirmar alterações no código, na pasta do projeto, deve-se executar:

```
python manage.py migrate
```