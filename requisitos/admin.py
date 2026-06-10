from django.contrib import admin
from .models import Requisito, MensagemChat, TemplateElicitacao, PerguntaTemplate

@admin.register(Requisito)
class RequisitoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'titulo', 'tipo', 'prioridade', 'status', 'criado_por', 'criado_em')
    list_filter = ('tipo', 'prioridade', 'status')
    search_fields = ('codigo', 'titulo')
    filter_horizontal = ('stakeholders',)
    readonly_fields = ('criado_em', 'atualizado_em', 'criado_por')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)

@admin.register(MensagemChat)
class MensagemChatAdmin(admin.ModelAdmin):
    list_display = ('requisito', 'usuario', 'data', 'total_likes')
    list_filter = ('requisito',)

class PerguntaInline(admin.TabularInline):
    model = PerguntaTemplate
    extra = 1

@admin.register(TemplateElicitacao)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    inlines = [PerguntaInline]
