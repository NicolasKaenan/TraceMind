from django import forms
from .models import Requisito, MensagemChat

class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisito
        fields = ['codigo', 'titulo', 'descricao', 'tipo', 'prioridade', 'status', 'stakeholders']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: RF01'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'stakeholders': forms.CheckboxSelectMultiple(),
        }

class MensagemChatForm(forms.ModelForm):
    class Meta:
        model = MensagemChat
        fields = ['mensagem']
        widgets = {
            'mensagem': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua mensagem...',
                'autocomplete': 'off',
            })
        }
