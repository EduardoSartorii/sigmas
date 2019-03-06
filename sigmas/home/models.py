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
		editable=False)
	preco = models.CharField(
		'Preço do produto',
		help_text= 'Digite o preço do produto',
		max_length= 50,)
	quantidade = models.CharField(
		'Quantidade desejada',
		help_text= 'Informe a quantidade desejada de produtos',
		max_length=100,)
