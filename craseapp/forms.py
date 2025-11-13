from django import forms
from .models import TermoRegente, TermoRegido


class ConsultaCraseForm(forms.Form):
    """Formulário para o usuário selecionar o Termo Regente e o Termo Regido."""

    regente = forms.ModelChoiceField(
        queryset=TermoRegente.objects.all().order_by('termo'),
        label="Termo Regente",
        empty_label="Selecione o termo regente"
    )

    regido = forms.ModelChoiceField(
        queryset=TermoRegido.objects.all().order_by('termo'),
        label="Termo Regido",
        empty_label="Selecione o termo regido"
    )