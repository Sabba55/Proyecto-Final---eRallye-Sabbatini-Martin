from django.urls import path

from AppSabba.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("inicio/", inicio, name="Start"),

    #CRUD DE PILOTOS
    path("pilotos/lista", PilotoLista.as_view(), name = "Ver Pilotos"),
    path("pilotos/nuevo", PilotoCrear.as_view(), name = "Crear Pilotos"),
    path("pilotos/borrar/<int:pk>", PilotoBorrar.as_view(), name="Borrar Pilotos"),
    path("pilotos/editar/<int:pk>", PilotoEditar.as_view(), name="Editar Pilotos"),

    #CRUD DE COPILOTOS
    path("copilotos/lista", CopilotoLista.as_view(), name = "Ver Copilotos"),
    path("copilotos/nuevo", CopilotoCrear.as_view(), name = "Crear Copilotos"),
    path("copilotos/borrar/<int:pk>", CopilotoBorrar.as_view(), name="Borrar Copilotos"),
    path("copilotos/editar/<int:pk>", CopilotoEditar.as_view(), name="Editar Copilotos"),
]
