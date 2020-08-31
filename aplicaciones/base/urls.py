from django.urls import path
from .views import Inicio,Listado,FormularioContacto,DetallePost, Suscribir, Portada
from django.conf.urls import (handler400,handler403,handler404,handler500)

#errors
handler404 = 'aplicaciones.base.views.handler404'
handler500 = 'aplicaciones.base.views.handler500'
handler403  = 'aplicaciones.base.views.handler403'
handler400  = 'aplicaciones.base.views.handler400'

#segundo paso para implementar vissta index
urlpatterns = [
    path('',Inicio.as_view(), name = 'index'),
    path('videojuegos/',Listado.as_view(),{'nombre_categoria':'Videojuegos'}, name = 'videojuegos'),
    path('generales/',Listado.as_view(),{'nombre_categoria':'General'}, name = 'generales'),
    path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
    path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
    path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),

]
