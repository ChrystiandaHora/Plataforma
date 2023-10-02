from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'tipo']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descricao'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor', 'step': '0.01'}),
            'tipo': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Tipo'}),
        }
