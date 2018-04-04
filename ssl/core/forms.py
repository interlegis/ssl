from django import forms
from django.forms import ModelForm
from .models import ArquivoExcel


class UpdateExcelForm(ModelForm):
    class Meta:
        model = ArquivoExcel
        fields = ['arquivo']

    arquivo = forms.FileField()
