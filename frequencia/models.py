from django.db import models

class Excursao(models.Model):
    nome = models.CharField(max_length=150, verbose_name="Nome da Viagem")
    descricao = models.TextField(verbose_name="Descrição da Viagem")
    cidade_inicio = models.CharField(max_length=100, verbose_name="Cidade de Início")
    cidade_termino = models.CharField(max_length=100, verbose_name="Cidade de Término")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_termino = models.DateField(verbose_name="Data de Término")
    horario_saida = models.TimeField(verbose_name="Horário de Saída")
    horario_chegada = models.TimeField(verbose_name="Horário de Chegada")

    def __str__(self):
        return f"{self.nome} ({self.cidade_inicio} para {self.cidade_termino})"

class Passageiro(models.Model):
    STATUS_CHOICES = [
        ('Aguardando', 'Aguardando Embarque'),
        ('Embarcado', 'Embarcado / Presente'),
        ('Ausente', 'Ausente'),
    ]

    excursao = models.ForeignKey(Excursao, on_delete=models.CASCADE, related_name='passageiros', verbose_name="Excursão")
    nome_completo = models.CharField(max_length=150, verbose_name="Nome Completo")
    documento = models.CharField(max_length=50, verbose_name="RG / Documento")
    contato_emergencia = models.CharField(max_length=50, verbose_name="Contato de Emergência")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Aguardando', verbose_name="Status de Presença")

    def __str__(self):
        return f"{self.nome_completo} ({self.status})"