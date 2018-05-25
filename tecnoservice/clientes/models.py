from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from productos.models import Version


class Cliente(models.Model):
    usuario = models.ForeignKey(
        User,
        related_name="clientes",
        default=None,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    dni = models.CharField(
        max_length=10,
        verbose_name=_("DNI")
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Nombre"),
    )
    apellido = models.CharField(
        max_length=255,
        verbose_name=_("Apellido"),
    )
    direccion = models.CharField(
        max_length=500,
        verbose_name=_("Dirección"),
        blank=True,
        null=True,
    )
    telefono = models.CharField(
        max_length=255,
        verbose_name=_("Teléfono"),
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
        blank=True,
        null=True,
    )
    clave = models.CharField(
        max_length=30,
        verbose_name=_("Clave Autogenerada"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{}, {}".format(
            self.apellido.upper(),
            self.nombre,
        )

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")


class Equipo(models.Model):
    version = models.ForeignKey(
        Version,
        related_name="equipos",
        on_delete=models.PROTECT,
        verbose_name=_("Modelo"),
    )
    serial = models.CharField(
        max_length=255,
        verbose_name=_("Número de Serie"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} (S/N: {})".format(
            self.version.modelo,
            self.serial,
        )

    class Meta:
        verbose_name = _("Equipo")
        verbose_name_plural = _("Equipos")
