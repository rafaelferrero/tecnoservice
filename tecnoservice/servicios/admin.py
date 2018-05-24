from django.contrib import admin
from servicios.models import Orden, Servicio


class ServicioInLine(admin.TabularInline):
    model = Servicio


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    inlines = [ServicioInLine, ]
    list_display = (
        'fecha',
        'numero',
        'cliente',
        'equipo',
    )
