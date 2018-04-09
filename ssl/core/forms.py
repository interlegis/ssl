from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import ArquivoExcel, CampanhaDoacao


class UpdateExcelForm(ModelForm):
    class Meta:
        model = ArquivoExcel
        fields = ['arquivo']

    arquivo = forms.FileField()


class CampanhaDoacaoForm(forms.ModelForm):

    class Meta:
        model = CampanhaDoacao
        fields = ['data_inicio', 'data_fim']
        exclude = []

    def clean(self):
        cleaned_data = super(CampanhaDoacaoForm, self).clean()

        if not self.is_valid():
            return cleaned_data

        data_inicio = cleaned_data['data_inicio']
        data_fim = cleaned_data['data_fim']

        if data_fim and data_fim < data_inicio:
            msg = ('Data início não pode ser superior a data de fim')
            raise ValidationError(msg)
        return cleaned_data