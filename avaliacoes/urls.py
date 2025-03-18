from django.urls import path
from . import views

urlpatterns = [
    path('adicionar_curso/', views.adicionar_curso, name='adicionar_curso'),
    path('adicionar_disciplina/', views.adicionar_disciplina, name='adicionar_disciplina'),
    path('adicionar_professor/', views.adicionar_professor, name='adicionar_professor'),
    path('adicionar_diario/', views.adicionar_diario, name='adicionar_diario'),
    path('adicionar_aluno/', views.adicionar_aluno, name='adicionar_aluno'),
    path('adicionar_avaliacao/', views.adicionar_avaliacao, name='adicionar_avaliacao'),
    path('adicionar_pergunta/', views.adicionar_pergunta, name='adicionar_pergunta'),
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('listar_disciplinas/', views.listar_disciplinas, name='listar_disciplinas'),
    path('listar_professores/', views.listar_professores, name='listar_professores'),
    path('listar_diarios/', views.listar_diarios, name='listar_diarios'),
    path('listar_alunos/', views.listar_alunos, name='listar_alunos'),
    path('listar_avaliacoes/', views.listar_avaliacoes, name='listar_avaliacoes'),
    path('listar_perguntas/', views.listar_perguntas, name='listar_perguntas'),
]