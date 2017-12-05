from rest_framework import routers, serializers, viewsets
from django.shortcuts import render
from django.http import HttpResponse
from transporte_app.models import *
from transporte_app.serializers import *

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class SolicitarViewSet(viewsets.ModelViewSet):
    queryset = Solicitar.objects.all()
    serializer_class = SolicitarSerializer

class AtenderViewSet(viewsets.ModelViewSet):
    queryset = Atender.objects.all()
    serializer_class = AtenderSerializer
