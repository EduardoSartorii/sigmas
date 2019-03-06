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
admin.site.register(estoque, admin_estoque)
