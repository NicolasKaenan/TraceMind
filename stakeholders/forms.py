from django import forms
from .models import Stakeholder

class StakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = ['nome', 'email', 'papel', 'contato', 'responsabilidade', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'papel': forms.Select(attrs={'class': 'form-select'}),
            'contato': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(48) 99999-9999'}),
            'responsabilidade': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
