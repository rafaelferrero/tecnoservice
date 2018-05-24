from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from clientes.models import Cliente, Equipo
from .choices import ESTADOS_ORDEN


def ultima_orden():
    orden = Orden.objects.all().order_by('-numero').first()
    if not orden:
        return 1
    else:
        return orden.numero + 1


class Orden(models.Model):
    fecha = models.DateField(
        verbose_name=_("Fecha"),
        default=timezone.now,
    )
    numero = models.BigIntegerField(
        verbose_name=_("Número"),
        default=ultima_orden,
    )
    cliente = models.ForeignKey(
        Cliente,
        related_name="clientes_ordenes",
        on_delete=models.PROTECT,
    )
    equipo = models.ForeignKey(
        Equipo,
        related_name="equipos_ordenes",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return "{} {} - {} ({})".format(
            self.numero,
            self.fecha,
            self.cliente,
            self.equipo,
        )


class Servicio(models.Model):
    orden = models.ForeignKey(
        Orden,
        related_name="servicios",
        on_delete=models.PROTECT,
        verbose_name=_("Orden"),
    )
    tarea = models.TextField(
        verbose_name=_("Tarea realizada"),
    )
    fecha = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Fecha"),
    )

    def __str__(self):
        return "Orden {} {} - {} ({})".format(
            self.orden.numero,
            self.orden.cliente,
            self.tarea[:20],
            self.fecha,
        )

    class Meta:
        verbose_name = _("Servicio"),
        verbose_name_plural = _("Servicios")


class EstadoOrden(models.Model):
    orden = models.ForeignKey(
        Orden,
        related_name="estados",
        verbose_name=_("Orden"),
        on_delete=models.PROTECT,
    )
    estado = models.CharField(
        max_length=255,
        choices=ESTADOS_ORDEN,
        default=ESTADOS_ORDEN[0][0],
        verbose_name=_("Estado")
    )
    fecha = models.DateTimeField(
        default=timezone.now,
        verbose_name=_("Fecha Cambio de Estado")
    )

    def __str__(self):
        return "Orden {} {} - {} ({})".format(
            self.orden.numero,
            self.orden.cliente,
            self.estado,
            self.fecha,
        )

    class Meta:
        verbose_name = _("Estado")
        verbose_name_plural = _("Estados")
