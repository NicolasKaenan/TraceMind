from django.contrib import admin
from .models import Stakeholder, Projeto

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dono', 'criado_em')
    search_fields = ('nome',)

@admin.register(Stakeholder)
class StakeholderAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'papel', 'responsabilidade', 'projeto', 'criado_em')
    list_filter = ('papel', 'responsabilidade', 'projeto')
    search_fields = ('nome', 'email')
    readonly_fields = ('criado_em', 'atualizado_em')
