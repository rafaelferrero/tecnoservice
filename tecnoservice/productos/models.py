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
    )
    nombre = models.CharField(
        max_length=255,
        verbose_name=_("Modelo")
    )

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        verbose_name =_("Modelo")
        verbose_name_plural = _("Modelos")
