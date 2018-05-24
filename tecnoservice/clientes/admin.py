from django.contrib import admin
from clientes.models import Cliente, Equipo


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    fields = (
        'dni',
        ('apellido', 'nombre'),
        'direccion',
        'telefono',
        'email',
    )
    exclude = ('usuario', )
    list_display = (
        'dni',
        '__str__',
        'direccion',
        'telefono',
        'email',
    )
    list_filter = (
        'apellido',
        'nombre',
    )


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = (
        'version',
        'serial',
    )
