from django import forms
from django.forms import ModelForm
from .models import estoque,comanda

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
class ComandaForm(forms.ModelForm):

	class Meta:
		model = comanda
		fields = '__all__'
		widgets = {
		'nome_cliente':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'sexo':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'situacao':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'cpf':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'comanda':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'mesas':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'narguiles':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'rua':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'cidade':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'estado':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'celular':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		'email':forms.TextInput(attrs={'class':'control-label text-right col-md-3','maxlength':300}),
		}
