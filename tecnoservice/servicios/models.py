from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from clientes.models import Cliente, Equipo
from django.contrib.auth.models import User
from .choices import ESTADOS_ORDEN, TIPO_TAREA
import string
import random


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
    tipo = models.CharField(
        max_length=255,
        verbose_name=_("Tipo de tarea"),
        choices=TIPO_TAREA,
        default=TIPO_TAREA[0][0],
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

    @receiver(post_save, sender=Orden)
    def set_nuevo(sender, **kwargs):
        if kwargs.get('created', True):
            EstadoOrden.objects.create(
                orden=kwargs.get('instance'),
                estado='NUEVA',
            )

            nombreusuario = kwargs.get('instance').cliente.nombre.split()[0].lower() + \
                            kwargs.get('instance').cliente.apellido.split()[0].lower(),

            dic = {
                'first_name': kwargs.get('instance').cliente.nombre,
                'last_name': kwargs.get('instance').cliente.apellido,
                'email': kwargs.get('instance').cliente.email,
                'password': ''.join(
                    random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(10)),
            }

            Cliente.objects.filter(pk=kwargs.get('instance').cliente.pk).update(clave=dic['password'])

            u, created = User.objects.update_or_create(
                username=nombreusuario[0],
                defaults=dic
            )

    @receiver(post_save, sender=Servicio)
    def set_estado(sender, **kwargs):
        if kwargs.get('created', True):
            servicio = kwargs.get('instance')
            if servicio.tipo == 'TRABAJO':
                valor = 'PROCESANDO'
            elif servicio.tipo == 'SOLUCION':
                valor = 'SOLUCIONADA'
            else:
                valor = 'ESPERANDO'
            EstadoOrden.objects.create(
                orden=servicio.orden,
                estado=valor
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
