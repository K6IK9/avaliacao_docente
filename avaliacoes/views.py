from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (
    CursoForm,
    DisciplinaForm,
    ProfessorForm,
    DiarioForm,
    AlunoForm,
    AvaliacaoForm,
    PerguntaForm,
)
from .models import Curso, Disciplina, Professor, Diario, Aluno, Avaliacao, Pergunta


# Função genérica para listagem de objetos
def listar_objetos(request, model, template_name, context_name):
    objetos = model.objects.all()
    return render(request, template_name, {context_name: objetos})


# Função genérica para adicionar objetos
def adicionar_objeto(request, form_class, template_name, redirect_url, success_message):
    if request.method == "POST":
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, success_message)
            return redirect(redirect_url)
        else:
            messages.error(request, "Erro ao salvar. Verifique os dados.")
    else:
        form = form_class()
    return render(request, template_name, {"form": form})


# dashboard
def index(request):
    context = {
        "total_cursos": Curso.objects.count(),
        "total_disciplinas": Disciplina.objects.count(),
        "total_professores": Professor.objects.count(),
        "total_diarios": Diario.objects.count(),
        "total_alunos": Aluno.objects.count(),
        "total_avaliacoes": Avaliacao.objects.count(),
        "total_perguntas": Pergunta.objects.count(),
        "avaliacoes_recentes": Avaliacao.objects.all().order_by("-data_inicio")[:5],
    }
    return render(request, "avaliacoes/dashboard.html", context)


# Listagens
def listar_cursos(request):
    return listar_objetos(
        request, Curso, "avaliacoes/listar/listar_cursos.html", "cursos"
    )


def listar_disciplinas(request):
    return listar_objetos(
        request, Disciplina, "avaliacoes/listar/listar_disciplinas.html", "disciplinas"
    )


def listar_professores(request):
    return listar_objetos(
        request, Professor, "avaliacoes/listar/listar_professores.html", "professores"
    )


def listar_diarios(request):
    return listar_objetos(
        request, Diario, "avaliacoes/listar/listar_diarios.html", "diarios"
    )


def listar_alunos(request):
    return listar_objetos(
        request, Aluno, "avaliacoes/listar/listar_alunos.html", "alunos"
    )


def listar_avaliacoes(request):
    return listar_objetos(
        request, Avaliacao, "avaliacoes/listar/listar_avaliacoes.html", "avaliacoes"
    )


def listar_perguntas(request):
    return listar_objetos(
        request, Pergunta, "avaliacoes/listar/listar_perguntas.html", "perguntas"
    )


# Adicionar
def adicionar_curso(request):
    return adicionar_objeto(
        request,
        CursoForm,
        "avaliacoes/adicionar/adicionar_curso.html",
        "listar_cursos",
        "Curso adicionado com sucesso!",
    )


def adicionar_disciplina(request):
    return adicionar_objeto(
        request,
        DisciplinaForm,
        "avaliacoes/adicionar/adicionar_disciplina.html",
        "listar_disciplinas",
        "Disciplina adicionada com sucesso!",
    )


def adicionar_professor(request):
    return adicionar_objeto(
        request,
        ProfessorForm,
        "avaliacoes/adicionar/adicionar_professor.html",
        "listar_professores",
        "Professor adicionado com sucesso!",
    )


def adicionar_diario(request):
    return adicionar_objeto(
        request,
        DiarioForm,
        "avaliacoes/adicionar/adicionar_diario.html",
        "listar_diarios",
        "Diário adicionado com sucesso!",
    )


def adicionar_aluno(request):
    return adicionar_objeto(
        request,
        AlunoForm,
        "avaliacoes/adicionar/adicionar_aluno.html",
        "listar_alunos",
        "Aluno adicionado com sucesso!",
    )


def adicionar_avaliacao(request):
    return adicionar_objeto(
        request,
        AvaliacaoForm,
        "avaliacoes/adicionar/adicionar_avaliacao.html",
        "listar_avaliacoes",
        "Avaliação adicionada com sucesso!",
    )


def adicionar_pergunta(request):
    return adicionar_objeto(
        request,
        PerguntaForm,
        "avaliacoes/adicionar/adicionar_pergunta.html",
        "listar_perguntas",
        "Pergunta adicionada com sucesso!",
    )
