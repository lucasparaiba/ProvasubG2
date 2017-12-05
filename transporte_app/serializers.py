from rest_framework import routers, serializers, viewsets
from transporte_app.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'

class MotoristaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class SolicitarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solicitar
        fields = '__all__'

class AtenderSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = False)
    class Meta:
        model = Atender
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        a = User.objects.create(**user_data)
        a = Atender.objects.create(usuario = a, **validated_data)
        return a
