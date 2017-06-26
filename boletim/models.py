from django.db import models
from decimal import *


class Disciplina(models.Model):
	nome = models.CharField(max_length=200)
	creditos = models.IntegerField("créditos")
	periodo_ideal = models.IntegerField("período ideal")

	def __str__(self):
		return self.nome

	class Meta:
		ordering = ['nome']


class Periodo(models.Model):
	ano = models.IntegerField()
	semestre = models.IntegerField()

	def __str__(self):
		return '{}.{}'.format(self.ano, self.semestre)

	def calcula_cr_periodo(self):
		notas = 0
		pesos = 0
		for matricula in Matricula.objects.filter(periodo_id=self.id):
			if matricula.nota_final:
				notas += matricula.nota_final * matricula.disciplina.creditos
				pesos += matricula.disciplina.creditos
			else:
				if matricula.calcula_nota_final() is not None:
					notas += matricula.calcula_nota_final() * matricula.disciplina.creditos
					pesos += matricula.disciplina.creditos
		if pesos == 0:
			return None
		else:
			return round(notas / pesos, 2)

	class Meta:
		verbose_name = "período"


class Professor(models.Model):
	nome_completo = models.CharField(max_length=200, null=True, blank=True)
	nome_exibicao = models.CharField("nome de exibição", max_length=200)
	email = models.EmailField("e-mail", null=True, blank=True)

	def __str__(self):
		return self.nome_exibicao

	class Meta:
		verbose_name_plural = "professores"
		ordering = ['nome_exibicao']


class Matricula(models.Model):
	CURSANDO = 'C'
	APROVADO = 'A'
	REPROVADO = 'R'
	TRANCAMENTO = 'T'
	SITUACAO_CHOICES = (
		(CURSANDO, 'cursando'),
		(APROVADO, 'aprovado'),
		(REPROVADO, 'reprovado'),
		(TRANCAMENTO, 'trancamento'),
	)
	disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
	periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="período")
	nota_final = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
	situacao = models.CharField("situação", max_length=1, choices=SITUACAO_CHOICES, default=CURSANDO)
	professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)

	def __str__(self):
		return '{} ({})'.format(self.disciplina, self.periodo)

	def calcula_nota_final(self):
		notas = 0
		pesos = 0
		for avaliacao in Avaliacao.objects.filter(matricula_id=self.id):
			notas += avaliacao.nota / avaliacao.nota_maxima * avaliacao.peso
			pesos += avaliacao.peso
		if pesos == 0:
			return None
		else:
			return Decimal(notas / pesos * 10).quantize(Decimal('.1'), rounding=ROUND_HALF_UP)

	@staticmethod
	def calcula_cr_geral():
		notas = 0
		pesos = 0
		for matricula in Matricula.objects.all():
			if matricula.nota_final:
				notas += matricula.nota_final * matricula.disciplina.creditos
				pesos += matricula.disciplina.creditos
			else:
				if matricula.calcula_nota_final() is not None:
					notas += matricula.calcula_nota_final() * matricula.disciplina.creditos
					pesos += matricula.disciplina.creditos
		return round(notas / pesos, 2)

	@staticmethod
	def calcula_creditos():
		aprovados = 0
		cursando = 0
		total = 0
		for matricula in Matricula.objects.all():
			if matricula.disciplina.periodo_ideal != 0:
				if matricula.situacao == 'A':
					aprovados += matricula.disciplina.creditos
				elif matricula.situacao == 'C':
					cursando += matricula.disciplina.creditos
		for disciplina in Disciplina.objects.all():
			if disciplina.periodo_ideal != 0:
				total += disciplina.creditos
		porcentagem_aprovados = aprovados * 100 / total
		porcentagem_cursando = cursando * 100 / total
		return (aprovados, cursando, total, porcentagem_aprovados, porcentagem_cursando)

	class Meta:
		verbose_name = "matrícula"
		ordering = ['periodo', 'disciplina']


class Avaliacao(models.Model):
	matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, verbose_name="matrícula")
	titulo = models.CharField("título", max_length=200)
	data = models.DateField(null=True, blank=True)
	peso = models.DecimalField(max_digits=5, decimal_places=2)
	nota = models.DecimalField(max_digits=3, decimal_places=1)
	nota_maxima = models.DecimalField("nota máxima", max_digits=3, decimal_places=1)

	def __str__(self):
		return '{} – {}'.format(self.titulo, self.matricula)

	class Meta:
		verbose_name = "avaliação"
		verbose_name_plural = "avaliações"
		ordering = ['matricula', 'data', 'titulo']