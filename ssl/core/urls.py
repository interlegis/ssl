from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^upload/$',
        view=views.UploadExcelView.as_view(),
        name='upload_excel'
    ),
    url(
        regex=r'^campanha/$',
        view=views.CreateCampanhaView.as_view(),
        name='create_campanha'
    ),
]
