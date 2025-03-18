from django.test import TestCase
from .models import Docente, Discente, Avaliacao

class AvaliacaoModelTest(TestCase):
    def test_criacao_avaliacao(self):
        docente = Docente.objects.create(nome="Prof. João", departamento="Matemática")
        discente = Discente.objects.create(nome="Aluno Maria", matricula="12345")
        avaliacao = Avaliacao.objects.create(docente=docente, discente=discente)
        self.assertEqual(avaliacao.docente.nome, "Prof. João")
        self.assertEqual(avaliacao.discente.nome, "Aluno Maria")