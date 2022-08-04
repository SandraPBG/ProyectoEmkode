
from django.contrib import admin
from django.urls import path
from applications.empleados. views import Listar, CrearRegistro, EditarRegistro, EliminarRegistro, Home

app_name='empleado_app'
urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('', Home.as_view()),
    path('lista', Listar.as_view(), name='ir_lista'),
    path('crear', CrearRegistro.as_view(), name='crear_empleado'),
    path('editar/<pk>', EditarRegistro.as_view(), name='editar_empleado'),
    path('eliminar/<pk>', EliminarRegistro.as_view(), name='eliminar_empleado'),

    
]
