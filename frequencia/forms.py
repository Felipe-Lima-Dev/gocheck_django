from django import forms
from .models import Excursao, Passageiro

class ExcursaoForm(forms.ModelForm):
    class Meta:
        model = Excursao
        fields = [
            'nome', 'descricao', 'cidade_inicio', 'cidade_termino', 
            'data_inicio', 'data_termino', 'horario_saida', 'horario_chegada'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Excursão de Sete Cidades'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Escreva aqui a descrição da viagem, com pontos turísticos e de parada'}),
            'cidade_inicio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui a cidade de início'}),
            'cidade_termino': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escreva aqui a cidade de término'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_termino': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'horario_saida': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'horario_chegada': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

class PassageiroForm(forms.ModelForm):
    class Meta:
        model = Passageiro
        fields = ['excursao', 'nome_completo', 'documento', 'contato_emergencia', 'status']
        widgets = {
            'excursao': forms.Select(attrs={'class': 'form-control'}),
            'nome_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo do passageiro'}),
            'documento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RG ou Documento'}),
            'contato_emergencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefone de contato'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }