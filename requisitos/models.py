from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords
from stakeholders.models import Stakeholder, Projeto

class TemplateElicitacao(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descricao', blank=True)

    class Meta:
        verbose_name = 'Template de Elicitacao'
        verbose_name_plural = 'Templates de Elicitacao'

    def __str__(self):
        return self.nome


class PerguntaTemplate(models.Model):
    template = models.ForeignKey(TemplateElicitacao, on_delete=models.CASCADE, related_name='perguntas')
    texto = models.TextField('Pergunta')
    ordem = models.IntegerField('Ordem', default=0)

    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return f'{self.template.nome} - P{self.ordem}'


class Requisito(models.Model):
    TIPO_CHOICES = [
        ('funcional', 'Funcional'),
        ('nao_funcional', 'Nao Funcional'),
    ]
    PRIORIDADE_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baixa', 'Baixa'),
    ]
    STATUS_CHOICES = [
        ('rascunho', 'Rascunho'),
        ('em_revisao', 'Em Revisao'),
        ('aprovado', 'Aprovado'),
        ('rejeitado', 'Rejeitado'),
    ]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='requisitos', null=True, blank=True)
    codigo = models.CharField('Codigo', max_length=10, unique=True)
    titulo = models.CharField('Titulo', max_length=200)
    descricao = models.TextField('Descricao')
    tipo = models.CharField('Tipo', max_length=15, choices=TIPO_CHOICES, default='funcional')
    prioridade = models.CharField('Prioridade', max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    status = models.CharField('Status', max_length=15, choices=STATUS_CHOICES, default='rascunho')
    stakeholders = models.ManyToManyField(Stakeholder, blank=True, verbose_name='Stakeholders relacionados')
    criado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='requisitos_criados')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
        ordering = ['codigo']

    def __str__(self):
        return f'{self.codigo} - {self.titulo}'


class MensagemChat(models.Model):
    requisito = models.ForeignKey(Requisito, on_delete=models.CASCADE, related_name='mensagens')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField('Mensagem')
    data = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes_mensagens', blank=True)

    class Meta:
        ordering = ['data']
        verbose_name = 'Mensagem do Chat'
        verbose_name_plural = 'Mensagens do Chat'

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.usuario.username} em {self.requisito.codigo}'
