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
		'nome_cliente':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite o nome do cliente'}),
		'sexo':forms.TextInput(attrs={'class':'form-control','maxlength':300,}),
		'situacao':forms.TextInput(attrs={'class':'form-control','maxlength':300,}),
		'cpf':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite o cpf do cliente'}),
		'comanda':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite a comanda do cliente'}),
		'mesas':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Qual a mesa do cliente'}),
		'narguiles':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Quantidade de narguiles'}),
		'rua':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite a rua do cliente'}),
		'cidade':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite a cidade do cliente'}),
		'estado':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite o estado do cliente'}),
		'celular':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite o celular do cliente'}),
		'email':forms.TextInput(attrs={'class':'form-control','maxlength':300,'placeholder':'Digite o email do cliente'}),
		}
