from rest_framework import serializers
from .models import SolicitudInmueble
from .serializerUsuario import UsuarioSerializer
from .serializerInmueble import InmuebleSerializar

class SolicitudSerializar(serializers.ModelSerializer):
    inmueble = InmuebleSerializar(many=False)
    usuario = UsuarioSerializer(many=False)

    class Meta:
        model = SolicitudInmueble
        fields = ('id', 'inmueble', 'usuario')