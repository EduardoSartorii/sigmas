from django import forms
from .models import estoque

class Estoque(forms.Form):
	marca = forms.CharField(required=True)
	nome = forms.CharField(required=True)
	sabor = forms.CharField(required=True)
	categoria = forms.CharField(required=True)
	preco = forms.CharField(required=True)
	quantidade = forms.CharField(required=True)
