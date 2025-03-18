from django import forms
from .models import (
    Curso,
    Disciplina,
    Professor,
    Diario,
    Aluno,
    Avaliacao,
    Pergunta,
    ContextoAvaliacao,
    AvaliacaoPergunta,
    AlunoAvaliacao,
    RespostaAvaliacaoAluno,
)


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nome"]


class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = ["nome", "sigla", "tipo", "curso"]


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["nome", "registro_academico"]


class DiarioForm(forms.ModelForm):
    class Meta:
        model = Diario
        fields = ["codigo", "periodo"]


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome", "matricula", "situacao_academica"]


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ["data_inicio", "data_final", "professor", "disciplina"]


class ContextoAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = ContextoAvaliacao
        fields = ["descricao"]


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = ["enunciado", "contexto"]


class AvaliacaoPerguntaForm(forms.ModelForm):
    class Meta:
        model = AvaliacaoPergunta
        fields = ["avaliacao", "pergunta"]


class AlunoAvaliacaoForm(forms.ModelForm):
    class Meta:
        model = AlunoAvaliacao
        fields = ["aluno", "avaliacao", "data_realizacao"]


class RespostaAvaliacaoAlunoForm(forms.ModelForm):
    class Meta:
        model = RespostaAvaliacaoAluno
        fields = ["aluno_avaliacao", "pergunta", "resposta"]
