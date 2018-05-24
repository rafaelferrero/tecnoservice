from django.utils.translation import ugettext_lazy as _

ESTADOS_ORDEN = (
    ('NUEVA', _("Nueva")),
    ('PROCESANDO', _("Procesando")),
    ('ESPERANDO', _("Esperando")),
    ('SOLUCIONADA', _("Solucionada")),
    ('CERRADA', _("Cerrada")),
)

TIPO_TAREA = (
    ('TRABAJO', _("Trabajo")),
    ('PAUSA', _("Pausa")),
    ('SOLUCION', _("Solucion")),
)
