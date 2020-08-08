from rest_framework import serializers
from .models import ComentarioValoracion
from .serializerUsuario import UsuarioSerializer
from .serializerInmueble import InmuebleSerializar

class ComentiarioSerializar(serializers.ModelSerializer):
    inmueble = InmuebleSerializar(many=False)
    usuario = UsuarioSerializer(many=False)

    class Meta:
        model = ComentarioValoracion
        fields = ('id', 'inmueble', 'usuario', 'comentario', 'valoracion')