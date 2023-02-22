from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User


class PilotoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=20)
    marca_vehiculo = forms.CharField(max_length=40)
    modelo_vehiculo = forms.CharField(max_length=40)

class CopilotoFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    nacionalidad = forms.CharField(max_length=20)