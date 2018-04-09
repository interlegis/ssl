from django.conf.urls import url

from . import views

app_name = 'campanha'
urlpatterns = [
    url(
        regex=r'^upload/$',
        view=views.UploadExcelView.as_view(),
        name='upload_excel'
    ),
    url(
        regex=r'^create/$',
        view=views.CreateCampanhaView.as_view(),
        name='create_campanha'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.CampanhaRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^detail/(?P<pk>\d+)$',
        view=views.DetailCampanhaView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^edit/(?P<pk>\d+)$',
        view=views.UpdateCampanhaView.as_view(),
        name='update'
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)$',
        view=views.DeleteCampanhaView.as_view(),
        name='delete'
    ),
    url(
        regex=r'list/$',
        view=views.CampanhaListView.as_view(),
        name='list'
    ),
]
