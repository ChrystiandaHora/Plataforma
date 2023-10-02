from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'tipo']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descricao'}),
            'valor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'tipo': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Tipo'}),
        }
