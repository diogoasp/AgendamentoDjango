from django.contrib import admin
from .models import Agendamento

@admin.register(Agendamento)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'tipo_unidade', 'horario')
    