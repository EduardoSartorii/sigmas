from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import (TemplateView, View, ListView, DetailView)
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from  django.views import defaults
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required
def home(request):
	template_name = 'index.html'

	return render(request,template_name)

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username=request.POST['username'], password=request.POST["password"])
		if user is not None:
			login(request,user)
			return redirect('/home')
		else:
			messages.error(request, 'Usuário ou senha incorreta')
	return render(request,'login.html')

def do_logout(request):
	logout(request)
	return redirect('/')

@login_required
def register_product(request):
	if request.method == 'POST':
		form = Estoque(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response(request,'pages/product.html', RequestContext(request))
	else:
		form = Estoque()
		return render(request, 'pages/product.html')

@login_required
def captura_products(request):
	template_name = 'pages/product.html'
	capture = estoque.objects.all()
	context = {'capture':capture,}
	register_product(request)
	return render(request,template_name,context)




