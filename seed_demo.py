# -*- coding: utf-8 -*-
"""
Script para popular dados de demonstracao para o video.
Execute: chcp 65001 && python manage.py shell < seed_demo.py
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reqplatform.settings')

import django
django.setup()

from django.contrib.auth.models import User
from stakeholders.models import Stakeholder
from requisitos.models import Requisito

print("Criando superusuario admin...")
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@tracemind.com', 'admin123')
    print("  admin / admin123 criado.")
else:
    print("  admin ja existe.")

admin = User.objects.get(username='admin')

print("Criando stakeholders...")
shs = [
    ('Joao Silva', 'joao.silva@empresa.com', 'cliente', '(48) 99101-1111', 'alta'),
    ('Maria Oliveira', 'maria.o@empresa.com', 'analista', '(48) 99202-2222', 'alta'),
    ('Carlos Dev', 'carlos.dev@empresa.com', 'dev', '(48) 99303-3333', 'media'),
    ('Ana PMO', 'ana.pmo@empresa.com', 'pmo', '(48) 99404-4444', 'media'),
    ('Pedro Juridico', 'pedro.j@empresa.com', 'compliance', '(48) 99505-5555', 'baixa'),
]
created_shs = []
for nome, email, papel, contato, resp in shs:
    s, created = Stakeholder.objects.get_or_create(email=email, defaults={
        'nome': nome, 'papel': papel, 'contato': contato, 'responsabilidade': resp
    })
    created_shs.append(s)
    print(f"  {'Criado' if created else 'Ja existe'}: {nome}")

print("Criando requisitos...")
reqs = [
    ('RF01', 'Cadastro e gestao de stakeholders', 'Permitir cadastrar, editar e remover stakeholders com papeis, contatos e niveis de responsabilidade.', 'funcional', 'alta', 'aprovado'),
    ('RF02', 'Elicitacao guiada com templates', 'Fornecer questionarios dinamicos e templates para entrevistas e workshops.', 'funcional', 'alta', 'aprovado'),
    ('RF03', 'Colaboracao em tempo real', 'Suportar edicao simultanea de documentos, comentarios e chat contextual.', 'funcional', 'alta', 'em_revisao'),
    ('RF04', 'Geracao automatica de documentacao', 'Gerar automaticamente Especificacao de Requisitos, User Stories e Casos de Uso.', 'funcional', 'media', 'em_revisao'),
    ('RF05', 'Rastreabilidade e versionamento', 'Vincular requisitos a tarefas, casos de teste e commits com historico de versoes.', 'funcional', 'alta', 'rascunho'),
    ('RF06', 'Fluxos de aprovacao com assinatura digital', 'Workflows configuráveis de aprovacao com notificacoes automaticas.', 'funcional', 'media', 'rascunho'),
    ('RF07', 'Integracao com ferramentas externas', 'APIs RESTful e webhooks para sincronizar com Jira, Trello, Git e CI/CD.', 'funcional', 'baixa', 'rascunho'),
    ('RNF01', 'Seguranca e controle de acesso', 'Autenticacao SSO; autorizacao baseada em papeis; criptografia TLS; logs de auditoria.', 'nao_funcional', 'alta', 'aprovado'),
    ('RNF02', 'Disponibilidade e desempenho', 'Disponibilidade 99,9%; tempo de resposta menor que 2s; escalonamento automatico.', 'nao_funcional', 'alta', 'aprovado'),
    ('RNF03', 'Escalabilidade e resiliencia', 'Arquitetura microservicos com escalabilidade horizontal e failover automatico.', 'nao_funcional', 'media', 'em_revisao'),
]

for codigo, titulo, desc, tipo, prio, status in reqs:
    r, created = Requisito.objects.get_or_create(codigo=codigo, defaults={
        'titulo': titulo, 'descricao': desc, 'tipo': tipo,
        'prioridade': prio, 'status': status, 'criado_por': admin
    })
    if created:
        r.stakeholders.set(created_shs[:2])
    print(f"  {'Criado' if created else 'Ja existe'}: {codigo}")

print("\nDados prontos!")
print("Acesse: http://localhost:8000")
print("Login: admin / admin123")
