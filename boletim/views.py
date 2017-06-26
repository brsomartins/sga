from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Avaliacao, Disciplina, Matricula, Periodo, Professor


def index(request):
	quantidade_disciplinas = Disciplina.objects.count()
	quantidade_matriculas = Matricula.objects.count()
	matriculas_cursando = Matricula.objects.filter(situacao='C').count()
	matriculas_aprovadas = Matricula.objects.filter(situacao='A').count()
	matriculas_reprovadas = Matricula.objects.filter(situacao='R').count()
	matriculas_trancadas = Matricula.objects.filter(situacao='T').count()
	quantidade_professores = Professor.objects.count()
	creditos_aprovados, creditos_cursando, total_creditos, porcentagem_aprovados, porcentagem_cursando = Matricula.calcula_creditos()
	context = {
		'quantidade_disciplinas': quantidade_disciplinas,
		'quantidade_matriculas': quantidade_matriculas,
		'matriculas_cursando': matriculas_cursando,
		'matriculas_aprovadas': matriculas_aprovadas,
		'matriculas_reprovadas': matriculas_reprovadas,
		'matriculas_trancadas': matriculas_trancadas,
		'quantidade_professores': quantidade_professores,
		'creditos_aprovados': creditos_aprovados,
		'creditos_cursando': creditos_cursando,
		'total_creditos': total_creditos,
		'porcentagem_aprovados': porcentagem_aprovados,
		'porcentagem_cursando': porcentagem_cursando,
		'origem': 'index'
		}
	return render(request, 'boletim/index.html', context)

def disciplinas(request):
	context = {'origem': 'disciplinas'}
	return render(request, 'boletim/disciplinas.html', context)

def disciplina(request, id):
	disciplina = get_object_or_404(Disciplina, id=id)
	context = {
		'disciplina': disciplina,
		'origem': 'disciplinas'
	}
	return render(request, 'boletim/disciplina.html', context)

def periodos(request):
	lista_periodos = Periodo.objects.all().order_by('-ano', '-semestre')
	context = {
		'lista_periodos': lista_periodos,
		'origem': 'periodos'
	}
	return render(request, 'boletim/periodos.html', context)

def periodo(request, ano, semestre):
	periodo = get_object_or_404(Periodo, ano=ano, semestre=semestre)
	lista_matriculas = Matricula.objects.filter(periodo=periodo).order_by('disciplina__nome')
	cr_geral = Matricula.calcula_cr_geral()
	context = {
		'periodo': periodo,
		'lista_matriculas': lista_matriculas,
		'cr_geral': cr_geral,
		'origem': 'periodos'
	}
	return render(request, 'boletim/periodo.html', context)

def matriculas(request):
	context = {'origem': 'matriculas'}
	return render(request, 'boletim/matriculas.html', context)

def matricula(request, id):
	matricula = get_object_or_404(Matricula, id=id)
	lista_avaliacoes = Avaliacao.objects.filter(matricula=matricula)
	context = {
		'matricula': matricula,
		'lista_avaliacoes': lista_avaliacoes,
		'origem': 'matriculas'
	}
	return render(request, 'boletim/matricula.html', context)

def professores(request):
	context = {'origem': 'professores'}
	return render(request, 'boletim/professores.html', context)