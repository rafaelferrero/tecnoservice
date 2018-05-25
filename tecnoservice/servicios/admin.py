from django.contrib import admin
from servicios.models import Orden, Servicio, EstadoOrden
from django.utils.translation import ugettext_lazy as _


def marcar_entragada(modeladmin, request, queryset):
    for q in queryset:
        EstadoOrden.objects.create(
            orden=q,
            estado='CERRADA',
        )


marcar_entragada.short_description = _("Entrega Realizada")


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    actions = [marcar_entragada, ]
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
