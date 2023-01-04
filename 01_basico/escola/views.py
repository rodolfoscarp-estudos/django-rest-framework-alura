from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
    AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer,
    ListaAlunosMatriculadosCursoSerializer)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewset(viewsets.ModelViewSet):
    """Exibindo todos os Alunos"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewset(viewsets.ModelViewSet):
    """Exibindo todos os Cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewset(viewsets.ModelViewSet):
    """Exibindo as Matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaMatriculaAluno(generics.ListAPIView):
    """Listando as mariculas de um aluno"""

    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno=self.kwargs['pk'])

        return queryset


class ListaAlunosMatriculados(generics.ListAPIView):
    """Lista os alunos matriculados em um curso"""

    serializer_class = ListaAlunosMatriculadosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso=self.kwargs['pk'])

        return queryset
