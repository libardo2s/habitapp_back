from rest_framework import serializers
from .models import Conversacion

class ConversacionSerializar(serializers.ModelSerializer):
    class Meta:
        model = Conversacion
        fields = ('id', 'usuario', 'conversacion', 'emisor', 'receptor')