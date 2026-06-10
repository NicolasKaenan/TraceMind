from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Stakeholder
from .forms import StakeholderForm

@login_required
def lista(request):
    stakeholders = Stakeholder.objects.all()
    return render(request, 'stakeholders/lista.html', {'stakeholders': stakeholders})

@login_required
def criar(request):
    if request.method == 'POST':
        form = StakeholderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stakeholder cadastrado com sucesso!')
            return redirect('stakeholders:lista')
    else:
        form = StakeholderForm()
    return render(request, 'stakeholders/form.html', {'form': form, 'titulo': 'Novo Stakeholder'})

@login_required
def editar(request, pk):
    stakeholder = get_object_or_404(Stakeholder, pk=pk)
    if request.method == 'POST':
        form = StakeholderForm(request.POST, instance=stakeholder)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stakeholder atualizado com sucesso!')
            return redirect('stakeholders:lista')
    else:
        form = StakeholderForm(instance=stakeholder)
    return render(request, 'stakeholders/form.html', {'form': form, 'titulo': 'Editar Stakeholder', 'obj': stakeholder})

@login_required
def excluir(request, pk):
    stakeholder = get_object_or_404(Stakeholder, pk=pk)
    if request.method == 'POST':
        stakeholder.delete()
        messages.success(request, 'Stakeholder removido.')
        return redirect('stakeholders:lista')
    return render(request, 'stakeholders/confirmar_exclusao.html', {'obj': stakeholder})
