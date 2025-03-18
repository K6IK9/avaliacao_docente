from django.db import models


class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    TIPO_DISCIPLINA_CHOICES = [
        ('OBR', 'Obrigatória'),
        ('OPT', 'Optativa'),
    ]
    tipo = models.CharField(max_length=3, choices=TIPO_DISCIPLINA_CHOICES)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    registro_academico = models.CharField(max_length=20, unique=True)
    disciplinas = models.ManyToManyField(Disciplina, through='DisciplinaProfessor', related_name='professores')

    def __str__(self):
        return self.nome


class DisciplinaProfessor(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professor} - {self.disciplina}"


class Diario(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    periodo = models.CharField(max_length=10)

    def __str__(self):
        return f"Diário {self.codigo} - {self.periodo}"


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    SITUACAO_ACADEMICA_CHOICES = [
        ('MAT', 'Matriculado'),
        ('TRA', 'Trancado'),
        ('FOR', 'Formado'),
    ]
    situacao_academica = models.CharField(max_length=3, choices=SITUACAO_ACADEMICA_CHOICES)

    def __str__(self):
        return self.nome


class DiarioDisciplinaProfessor(models.Model):
    diario = models.ForeignKey(Diario, on_delete=models.CASCADE)
    disciplina_professor = models.ForeignKey(DisciplinaProfessor, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.diario} - {self.disciplina_professor}"


class ContextoAvaliacao(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Avaliacao(models.Model):
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='avaliacoes')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='avaliacoes')

    def __str__(self):
        return f"Avaliação de {self.disciplina} por {self.professor}"


class Pergunta(models.Model):
    enunciado = models.TextField()
    contexto = models.ForeignKey(ContextoAvaliacao, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.enunciado


class AvaliacaoPergunta(models.Model):
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='avaliacao_perguntas')
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='avaliacao_perguntas')

    def __str__(self):
        return f"{self.pergunta} na {self.avaliacao}"


class AlunoAvaliacao(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='avaliacoes')
    avaliacao = models.ForeignKey(Avaliacao, on_delete=models.CASCADE, related_name='aluno_avaliacoes')
    data_realizacao = models.DateField()

    def __str__(self):
        return f"Avaliação de {self.aluno} em {self.avaliacao}"


class RespostaAvaliacaoAluno(models.Model):
    aluno_avaliacao = models.ForeignKey(AlunoAvaliacao, on_delete=models.CASCADE, related_name='respostas')
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, related_name='respostas')
    resposta = models.TextField()

    def __str__(self):
        return f"Resposta de {self.aluno_avaliacao.aluno} para {self.pergunta}"
