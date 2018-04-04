from django.forms import ModelForm
from core.models import ArquivoExcel


class UpdateExcelForm(ModelForm):
    class Meta:
        model = ArquivoExcel
        fields = ['arquivo']
