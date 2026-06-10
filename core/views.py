from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from stakeholders.models import Stakeholder
from requisitos.models import Requisito

@login_required
def dashboard(request):
    total_stakeholders = Stakeholder.objects.count()
    total_requisitos = Requisito.objects.count()
    total_funcionais = Requisito.objects.filter(tipo='funcional').count()
    total_nao_funcionais = Requisito.objects.filter(tipo='nao_funcional').count()

    aprovados = Requisito.objects.filter(status='aprovado').count()
    em_revisao = Requisito.objects.filter(status='em_revisao').count()
    rascunho = Requisito.objects.filter(status='rascunho').count()

    ultimos_requisitos = Requisito.objects.order_by('-criado_em')[:5]
    ultimos_stakeholders = Stakeholder.objects.order_by('-criado_em')[:5]

    context = {
        'total_stakeholders': total_stakeholders,
        'total_requisitos': total_requisitos,
        'total_funcionais': total_funcionais,
        'total_nao_funcionais': total_nao_funcionais,
        'aprovados': aprovados,
        'em_revisao': em_revisao,
        'rascunho': rascunho,
        'ultimos_requisitos': ultimos_requisitos,
        'ultimos_stakeholders': ultimos_stakeholders,
    }
    return render(request, 'core/dashboard.html', context)
