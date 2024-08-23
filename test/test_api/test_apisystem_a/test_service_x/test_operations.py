from typing import Final

from test import ServiceAPISystemATestCase


class ServiceAPISystemAOperationsTestCase(
    ServiceAPISystemATestCase
):
    # Nome do Teste como deve ser escrito no relatório final
    READABLE: Final[str] = "Nome Legível - Human Readable"

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_0010_(self) -> None:
        self.assertListEqual(
            [
                "VisualizarMatricula",
                "VisualizarMatricula_v2",
                "VisualizarMatricula_v3",
                "VisualizarMatricula_App",
                "VisualizarMatriculaPedido",
            ],
            list(self.c.service._operations.keys()),
        )
