from rest_framework import serializers
from .models import Universidad
from .serializerCiudad import CiudadSerializer


class UniversidadSerializer(serializers.ModelSerializer):
    ciudad =  CiudadSerializer(many=False)

    class Meta:
        model = Universidad
        fields = ('nombre', 'ciudad', 'id')
