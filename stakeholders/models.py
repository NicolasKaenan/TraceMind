from django.db import models
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField('Nome', max_length=200)
    descricao = models.TextField('Descricao', blank=True)
    dono = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projetos')
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome


class Stakeholder(models.Model):
    PAPEL_CHOICES = [
        ('cliente', 'Cliente Solicitante'),
        ('analista', 'Analista de Requisitos'),
        ('dev', 'Equipe Dev/QA'),
        ('pmo', 'Gerente de Projetos / PMO'),
        ('suporte', 'Suporte / Manutencao'),
        ('compliance', 'Compliance / Juridico'),
        ('outro', 'Outro'),
    ]
    RESPONSABILIDADE_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baixa', 'Baixa'),
    ]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='stakeholders', null=True, blank=True)
    nome = models.CharField('Nome', max_length=150)
    email = models.EmailField('E-mail', unique=True)
    papel = models.CharField('Papel', max_length=20, choices=PAPEL_CHOICES)
    contato = models.CharField('Contato / Telefone', max_length=50, blank=True)
    responsabilidade = models.CharField('Nivel de Responsabilidade', max_length=10, choices=RESPONSABILIDADE_CHOICES, default='media')
    observacoes = models.TextField('Observacoes', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Stakeholder'
        verbose_name_plural = 'Stakeholders'
        ordering = ['nome']

    def __str__(self):
        return f'{self.nome} ({self.get_papel_display()})'
