from django import forms
from django.forms import ModelForm
from .models import estoque

class EstoqueForm(forms.ModelForm):
	
	class Meta:	
		model = estoque
		fields ='__all__'
		widgets = {

		'marca':forms.TextInput(attrs={'class':'form-control','maxlength':255,'placeholder':'Marca'}),
		'nome':forms.TextInput(attrs={'class':'form-control','maxlength':255,'placeholder':'Nome'}),
		'sabor':forms.TextInput(attrs={'class':'form-control','maxlength':255,'placeholder':'Sabor'}),
		'categoria':forms.TextInput(attrs={'class':'form-control','maxlength':255,'placeholder':'Categoria'}),
		'preco':forms.TextInput(attrs={'class':'form-control','maxlength':255,'placeholder':'Preco'}),
		'quantidade':forms.TextInput(attrs={'class':'form-control','maxlength':255,'placeholder':'Quantidade'}),

		}