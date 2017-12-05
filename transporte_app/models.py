from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    nomedoVeiculo = models.CharField(max_length=128)
    anodoveiculo = models.CharField(max_length=128)
    placa = models.CharField(max_length=128)

    def __str__(self):
        return self.nomedoVeiculo +" "+ "/" +" "+ "Placa: ( " + self.placa + " )"

class Funcionario(models.Model):
    nome = models.CharField(max_length=128)
    cpf = models.CharField(max_length=128)
    datadenascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome + " "+ "/" +" " + "CPF: ( " + self.cpf + " )"

class Motorista(models.Model):
    funcionario = models.ForeignKey(Funcionario, null=True, blank=False)
    cnh = models.CharField(max_length=128)

    def __str__(self):
        return self.funcionario.nome +" "+ "/" +" "+ "CNH: ( " + self.cnh + " )"

class Departamento(models.Model):
    nomedoDepartamento = models.CharField(max_length=128)
    local = models.CharField(max_length=128)

    def __str__(self):
        return self.nomedoDepartamento

class Solicitar(models.Model):
    departamento = models.ForeignKey(Departamento, null=True, blank=False)
    Funcionarios = models.ForeignKey(Funcionario, null=True, blank=False)
    dataH_solicitacao = models.DateTimeField(blank=True, null=True)
    origem = models.CharField(max_length=128)
    destino = models.CharField(max_length=128)

    def __str__(self):
        return "Solicitante: " + self.departamento.nomedoDepartamento

class Atender(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=False)
    veiculo = models.ForeignKey(Veiculo, null=True, blank=False)
    motorista = models.OneToOneField(Motorista, null=True, blank=False)
    solicitacao = models.ForeignKey(Solicitar, null=True, blank=False)

    def __str__(self):
         return "Atendimento da Solicitação do Setor: " + self.solicitacao.departamento.nomedoDepartamento +" "+ "/" +" "+ "Funcionario que irá Atender: " + self.motorista.funcionario.nome +" "+ "/" +" "+ "CNH: (" + self.motorista.cnh + ")"
