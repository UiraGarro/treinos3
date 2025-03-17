from rest_framework import serializers
from .models import Usuario, Visitante, AccessLog

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'usuario'
        fields = ['id', 'username', 'email', 'tipo_usuario']
        
class VisitanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'visitante'
        fields = '__all__'
        
class AccessLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'accesslog'
        fields = '__all__'