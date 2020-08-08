from rest_framework import serializers
from .serializerUser import UserSerializer
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'apellido', 'genero', 'edad','foto', 'arrendador', 'telefono')
