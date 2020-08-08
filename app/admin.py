from django.contrib import admin
from .models import Usuario, Inmueble, Fotos, SolicitudInmueble, Conversacion, ComentarioValoracion, Ciudad, Universidad

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Inmueble)
admin.site.register(Fotos)
admin.site.register(SolicitudInmueble)
admin.site.register(Conversacion)
admin.site.register(ComentarioValoracion)
admin.site.register(Ciudad)
admin.site.register(Universidad)
