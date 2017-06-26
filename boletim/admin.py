from django.contrib import admin

from .models import Avaliacao, Disciplina, Matricula, Periodo, Professor

admin.site.register(Avaliacao)
admin.site.register(Disciplina)
admin.site.register(Matricula)
admin.site.register(Periodo)
admin.site.register(Professor)