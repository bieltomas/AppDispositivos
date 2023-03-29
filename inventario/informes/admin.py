from django.contrib import admin
from .models import Empleado, Prestamo, Aplicaciones

class AplicacionesPrestamo(admin.TabularInline):
    model = Aplicaciones
    extra = 1

class PrestamoAdmin(admin.ModelAdmin):
    inlines = [AplicacionesPrestamo]
    list_display = ('empleado','Dispositivo','Identificador','Marca','Modelo','CPU','RAM','Almacenamiento','NumeroSerie','Observaciones','FechaInicio','FechaDevolucion')
    search_fields = ['empleado__Nombre','Dispositivo','Identificador','Marca','Modelo','CPU','RAM','Almacenamiento','NumeroSerie']
    list_filter = ['FechaInicio']


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','DNI','Pais','Departamento','Email')
    search_fields = ['Nombre','DNI','Pais','Departamento','Email']

admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Prestamo, PrestamoAdmin)

