from rest_framework import serializers
from .serializerUniversidad import UniversidadSerializer
from .models import Inmueble


class InmuebleSerializar(serializers.ModelSerializer):
    universidad = UniversidadSerializer(many=False)

    class Meta:
        model = Inmueble
        fields = ('id', 'usuarioInmueble', 'direccion', 'barrio', 'precio',
                  'universidad', 'tipoVivienda', 'descripcion', 'bano', 'cama',
                  'wifi', 'ciudad', 'accesible', 'almuerzo', 'amueblado',
                  'tv', 'lavado', 'mascota', 'fumador', 'piscina',
                  'portero', 'camarote', 'espacio_estudio', 'pareja', 'aire_acondicionado',
                  'fechaEntrada', 'fechaSalida', 'instancia', 'foto', 'hombre',
                  'mujeres', 'estado', 'comentarios', 'valoracionPromedio', 'propietario',
                  'telefono_propietario', 'panoramica', 'panoramica_imagen')
