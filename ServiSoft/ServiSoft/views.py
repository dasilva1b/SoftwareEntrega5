from django.http import HttpResponse
import datetime
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
from Telefonia.models import Usuario

#View que despliega la pagina de inicio del sistema
def home(request):
  now=now = datetime.datetime.now()
  return render (request,'home.html',{'now':now})


  