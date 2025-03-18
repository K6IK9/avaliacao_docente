from django import forms
from .models import Curso, Disciplina, Professor, Diario, Aluno, Avaliacao, Pergunta, ContextoAvaliacao, AvaliacaoPergunta, AlunoAvaliacao, RespostaAvaliacaoAluno
from django.contrib import admin


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome']


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ['nome', 'sigla', 'tipo', 'curso']


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'registro_academico', 'disciplinas']


class DiarioForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = ['codigo', 'periodo']


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'matricula', 'situacao_academica']


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['data_inicio', 'data_final', 'professor', 'disciplina']


class ContextoAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = ContextoAvaliacao
        fields = ['descricao']


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ['enunciado', 'contexto']


class AvaliacaoPerguntaForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoPergunta
        fields = ['avaliacao', 'pergunta']


class AlunoAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = AlunoAvaliacao
        fields = ['aluno', 'avaliacao', 'data_realizacao']


class RespostaAvaliacaoAlunoForm(forms.ModelForm):
    class Meta:
        model = RespostaAvaliacaoAluno
        fields = ['aluno_avaliacao', 'pergunta', 'resposta']


# Admin configurations
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'tipo', 'curso')
    list_filter = ('tipo', 'curso')
    search_fields = ('nome', 'sigla')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'registro_academico')
    filter_horizontal = ('disciplinas',)
    search_fields = ('nome', 'registro_academico')


@admin.register(Diario)
class DiarioAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'periodo')
    search_fields = ('codigo', 'periodo')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'situacao_academica')
    list_filter = ('situacao_academica',)
    search_fields = ('nome', 'matricula')


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('disciplina', 'professor', 'data_inicio', 'data_final')
    list_filter = ('disciplina', 'professor')
    search_fields = ('contexto',)


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'contexto')
    search_fields = ('enunciado',)


@admin.register(ContextoAvaliacao)
class ContextoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    search_fields = ('descricao',)


@admin.register(AvaliacaoPergunta)
class AvaliacaoPerguntaAdmin(admin.ModelAdmin):
    list_display = ('avaliacao', 'pergunta')


@admin.register(AlunoAvaliacao)
class AlunoAvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'avaliacao', 'data_realizacao')
    list_filter = ('data_realizacao',)


@admin.register(RespostaAvaliacaoAluno)
class RespostaAvaliacaoAlunoAdmin(admin.ModelAdmin):
    list_display = ('aluno_avaliacao', 'pergunta', 'resposta')
