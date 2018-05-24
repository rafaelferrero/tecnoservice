from django.contrib import admin
from servicios.models import Orden, Servicio, EstadoOrden


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'numero',
        'cliente',
        'equipo',
    )
    list_filter = (
        'cliente',
        'equipo',
    )


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        'orden',
        'fecha',
        'tarea',
    )
    list_filter = (
        'orden',
    )


@admin.register(EstadoOrden)
class EstadoOrdenAdmin(admin.ModelAdmin):
    pass
