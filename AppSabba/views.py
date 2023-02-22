from django.shortcuts import render

from django.http import HttpResponse
#Importamos de models y de forms
from AppSabba.models import *
from AppSabba.forms import *
#otros importaciones para iniciar sesion
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#def para tener mi app en el inicio
def inicio(request):
    return render(request, "AppSabba/inicio.html")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CRUD DE PILOTOS con vistas basadas en clases

class PilotoLista(ListView): #piloto_list / base de template
    model = Piloto
    template_name = "AppSabba/drivers/piloto_list.html"
#LoginRequiredMixin
class PilotoCrear(CreateView): #..._form.html
    model = Piloto
    fields = ["nombre", "apellido", "edad", "nacionalidad", "marca_vehiculo", "modelo_vehiculo"]
    success_url = "/AppSabba/pilotos/lista"
    template_name = "AppSabba/drivers/piloto_form.html"

class PilotoBorrar(DeleteView):  #..._confirm_delete.html
    model = Piloto
    success_url = "/AppSabba/pilotos/lista"
    template_name = "AppSabba/drivers/piloto_confirm_delete.html"

class PilotoEditar(UpdateView): #..._form.html
    model = Piloto
    fields = ["nombre", "apellido", "edad", "nacionalidad", "marca_vehiculo", "modelo_vehiculo"]
    success_url = "/AppSabba/pilotos/lista"
    template_name = "AppSabba/drivers/piloto_form.html"

#--------------------------------------------------

#CRUD DE COPILOTO con vistas basadas en clases
class CopilotoLista(ListView): #piloto_list / base de template
    model = Copiloto
    template_name = "AppSabba/codriver/copiloto_list.html"

class CopilotoCrear(CreateView): #..._form.html
    model = Copiloto
    fields = ["nombre", "apellido", "edad", "nacionalidad"]
    success_url = "/AppSabba/copilotos/lista"
    template_name = "AppSabba/codriver/copiloto_form.html"

class CopilotoBorrar(DeleteView):  #..._confirm_delete.html
    model = Copiloto
    success_url = "/AppSabba/copilotos/lista"
    template_name = "AppSabba/codriver/copiloto_confirm_delete.html"

class CopilotoEditar(UpdateView): #..._form.html
    model = Copiloto
    fields = ["nombre", "apellido", "edad", "nacionalidad"]
    success_url = "/AppSabba/copilotos/lista"
    template_name = "AppSabba/codriver/copiloto_form.html"