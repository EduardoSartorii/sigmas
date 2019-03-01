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

def do_login(request):
	template_name = 'login.html'

	return render(request,template_name)

def home(request):
	template_name = 'index.html'

	return render(request,template_name)
