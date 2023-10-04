from django import forms
from .models import Transacao


class TransacaoForm(forms.ModelForm):
    parcela = forms.IntegerField(
        label='Parcelas', required=False,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Número de Parcelas'})
    )

    class Meta:
        model = Transacao
        fields = ['descricao', 'valor', 'tipo', 'parcela']
        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Descricao'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor', 'step': '0.01'}),
            'tipo': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Tipo'}),
        }
