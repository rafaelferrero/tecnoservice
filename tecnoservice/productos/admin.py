from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from productos.models import Marca, Modelo


@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    pass


@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    pass
