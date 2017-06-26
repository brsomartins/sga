from django.conf.urls import url

from . import views

app_name = 'boletim'
urlpatterns = [
    # ex: /boletim/
    url(r'^$', views.index, name='index'),
    # ex: /boletim/disciplinas/
    url(r'^disciplinas/$', views.disciplinas, name='disciplinas'),
    # ex: /boletim/disciplinas/1
    url(r'^disciplinas/(?P<id>[0-9]+)/$', views.disciplina, name='disciplina'),
    # ex: /boletim/periodos/
    url(r'^periodos/$', views.periodos, name='periodos'),
    # ex: /boletim/periodos/2016.2
    url(r'^periodos/(?P<ano>[0-9]{4}).(?P<semestre>[1-2]{1})/$', views.periodo, name='periodo'),
    # ex: /boletim/matriculas/
    url(r'^matriculas/$', views.matriculas, name='matriculas'),
    # ex: /boletim/matriculas/1
    url(r'^matriculas/(?P<id>[0-9]+)/$', views.matricula, name='matricula'),
    # ex: /boletim/professores/
    url(r'^professores/$', views.professores, name='professores'),
]