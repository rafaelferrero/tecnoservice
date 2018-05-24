from django.db import models
from django.utils.translation import ugettext_lazy as _


class Marca(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Marca")
    )

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name =_("Marca")
        verbose_name_plural = _("Marcas")


class Modelo(models.Model):
    marca = models.ForeignKey(
        Marca,
        verbose_name=_("Marca"),
        related_name="marcas",
        on_delete=models.PROTECT,
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Modelo"),
    )
    tipo = models.CharField(
        max_length=255,
        verbose_name=_("Tipo"),
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(
            self.marca.nombre,
            self.nombre,
        )

    class Meta:
        verbose_name =_("Modelo")
        verbose_name_plural = _("Modelos")


class Version(models.Model):
    modelo = models.ForeignKey(
        Modelo,
        verbose_name=_("Modelo"),
        related_name="versiones",
        on_delete=models.PROTECT,
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Versión"),
    )

    def __str__(self):
        return "{} {} ({})".format(
            self.modelo.marca.nombre,
            self.modelo.nombre,
            self.nombre,
        )

    class Meta:
        verbose_name = _("Versión")
        verbose_name_plural = _("Versiones")
