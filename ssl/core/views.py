from django.views.generic import (CreateView, DetailView, DeleteView,
                                    ListView, UpdateView, RedirectView)
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UpdateExcelForm, CampanhaDoacaoForm
from .models import ArquivoExcel, CampanhaDoacao
from .utils import read_excel

class UploadExcelView(CreateView):
    template_name = "core/upload_excel.html"
    form_class = UpdateExcelForm
    model = ArquivoExcel

    def upload_file(request):
        if request.method == 'POST':
            form = UpdateExcelForm(request.POST, request.FILES)
            if form.is_valid():
                read_excel(request.FILES['file'])
                return HttpResponseRedirect('')
        else:
            form = UpdateExcelForm()
        return render(request, 'upload_excel.html', {'form': form})

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass

    # def post(self, request, *args, **kwargs):
    #     form_class = self.get_form_class()
    #     form = self.get_form(form_class)
    #     import ipdb; ipdb.set_trace()
    #     files = request.FILES.getlist('file')
    #     if form.is_valid():
    #
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class CreateCampanhaView(CreateView):
    template_name = "core/create_campanha.html"
    model = CampanhaDoacao
    form_class = CampanhaDoacaoForm


class UpdateCampanhaView(UpdateView):
    template_name = "core/update_campanha.html"
    template_name_suffix = '_update'
    model = CampanhaDoacao
    fields = ['data_inicio', 'data_fim']

    def get_success_url(self):
        return reverse('campanha:detail',
                       kwargs={'pk': self.object.id})

    def get_object(self):
        return CampanhaDoacao.objects.get(pk=
                                          self.kwargs['pk'])


class DeleteCampanhaView(DeleteView):
    template_name = "core/delete_campanha.html"
    model = CampanhaDoacao
    fields = ['data_inicio', 'data_fim']

    def get_success_url(self):
        return reverse('campanha:list')

    def get_object(self):
        return CampanhaDoacao.objects.get(pk=
                                          self.kwargs['pk'])


class DetailCampanhaView(DetailView):
    model = CampanhaDoacao
    template_name = "core/detail_campanha.html"


class CampanhaRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('campanha:detail',
                       kwargs={'pk': self.pk})


class CampanhaListView(ListView):
    model = CampanhaDoacao
    paginate_by = 10
    template_name = "core/list_campanha.html"


