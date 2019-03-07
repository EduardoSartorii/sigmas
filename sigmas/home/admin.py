from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

class admin_estoque(admin.ModelAdmin):
	list_display= (
		'marca',
		'nome',
		'sabor',
		'categoria',
		'preco',
		'quantidade',
		)
	model = estoque
	can_delete = True
class admin_comanda(admin.ModelAdmin):
	list_display= (
		'nome_cliente',
		'sexo',
		'situacao',
		'cpf',
		'comanda',
		'mesas',
		'narguiles',
		'rua',
		'cidade',
		'estado',
		'celular',
		'email',		
		)
	model = comanda
	can_delete = True
admin.site.register(estoque, admin_estoque)
admin.site.register(comanda, admin_comanda)
