from django.test import TestCase
from aluraflix.models import Programa


class PogramaModelTestCase(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo="Procurando Lemo",
            data_lancamento='2005-01-23'
        )

    def test_verifica_atributos_do_programa(self):
        """Teste que verifica os atributos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, "Procurando Lemo")
        self.assertEqual(self.programa.tipo, "F")
        self.assertEqual(self.programa.data_lancamento, "2005-01-23")
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)
