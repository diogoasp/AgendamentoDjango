from pyexpat import model
from tabnanny import verbose
from django.db import models

# Create your models here.
class Agendamento(models.Model):
    PRIORITARIO_CHOICES = [(1, 'Pessoas com 60 anos ou mais institucionalizadas'),(2, 'Pessoas com deficiencias institucionalizadas'),(3, 'Povos indígenas'),(4, 'Servidor público'),(5,'Sem priodade')]
    TIPO_UNIDADE_CHOICES = [(1, 'CRAS'),(2,'CREAS'),(3,'CAPS'),(4,'PROJETO LARA')]
    HORARIO_CHOICES = [(8,8),(9,9),(10,10),(11,11),(14,14),(15,15),(16,16)]

    nome = models.CharField('Nome', max_length=250)
    cpf = models.CharField('CPF', max_length=11)
    grupo_prioritario = models.IntegerField(verbose_name="Prioridade", choices=PRIORITARIO_CHOICES)
    email = models.CharField('E-mail', max_length=40, null=True, blank=True)
    data_nascimento = models.DateField('Data Nascimento')
    celular = models.CharField('Número do celular', max_length=15)
    tipo_unidade = models.IntegerField('Tipo da unidade', choices=TIPO_UNIDADE_CHOICES)
    horario = models.IntegerField('Horário de atendimento', choices=HORARIO_CHOICES)

    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Atendimento agendado'
        verbose_name_plural = 'Atendimentos agendados'
