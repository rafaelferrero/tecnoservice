from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from productos.models import Marca, Modelo, Version


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
    )


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = (
        'marca',
        'nombre',
    )
    list_filter = (
        'marca',
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        'modelo',
        'nombre',
    )
    list_filter = (
        'modelo',
    )
