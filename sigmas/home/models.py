import re
from datetime import date, datetime
from django.db import models
from django.core import validators
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

class estoque(models.Model):
	marca = models.CharField(
		'Marca do produto',
		help_text = 'Informe a marca do produto',
		max_length = 300,)
	nome = models.CharField(
		'Nome do produto',
		help_text= 'Informe o nome do produto',
		max_length = 150,)
	sabor = models.CharField(
		'Sabor do produto',
		help_text= 'Informe o sabor do produto',
		max_length=150,)
	categoria = models.CharField(
		'Categoria do produto',
		help_text= 'Informe a categoria do produto',
		max_length=150,
		default="", 
		editable=True)
	preco = models.CharField(
		'Preço do produto',
		help_text= 'Digite o preço do produto',
		max_length= 50,)
	quantidade = models.CharField(
		'Quantidade desejada',
		help_text= 'Informe a quantidade desejada de produtos',
		max_length=100,)

class comanda(models.Model):
	nome_cliente = models.CharField(
		'Nome do cliente',
		help_text = 'Informe o nome do cliente',
		max_length = 300,)
	sexo = (
		('Masculino', 'Masculino'),
		('Feminino', 'Feminino'),
		'Genero do cliente',)
	situacao =(
		('V','Vip'),
		('P','Pagante'))
	cpf = models.CharField(
		'Marca do produto',
		unique=True,
		help_text = 'Informe a marca do produto',
		max_length = 14,)
	comanda = models.CharField(
		'Comanda',
		help_text = 'Informe o número da comanda',
		max_length = 8,)
	mesas = models.CharField(
		'Mesa',
		help_text = 'Informe a mesa do cliente',
		max_length = 3,)
	narguiles = models.CharField(
		'Narguile',
		help_text = 'Informe a marca do produto',
		max_length = 5,)
	rua = models.CharField(
		'Endereço do cliente',
		help_text = 'Endereço do cliente',
		max_length = 300,)
	cidade = models.CharField(
		'Cidade do Cliente',
		help_text = 'Informe a cidade do cliente',
		max_length = 300,)
	estado = models.CharField(
		'Marca do produto',
		help_text = 'Informe a marca do produto',
		max_length = 300,)
	celular = models.CharField(
		'Marca do produto',
		help_text = 'Informe a marca do produto',
		max_length = 300,)
	email = models.CharField(
		'Marca do produto',
		help_text = 'Informe a marca do produto',
		max_length = 300,)

