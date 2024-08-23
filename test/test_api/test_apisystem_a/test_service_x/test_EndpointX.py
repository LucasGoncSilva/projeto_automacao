from typing import Final
from decimal import Decimal
from random import randint

from zeep.exceptions import Fault, ValidationError

from test import (
    APISystemATestCase,
    ServiceAPISystemATestCase,
    APISYSTEM_A,
    save_protocol,
)


class ServiceAPISystemAMetodoTestCase(
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

    def setUp(self) -> None:
        super().setUp()
        self.request: dict = {
            "...": APISystemATestCase.hash,
            "...": "...",
            "...": "...",
            "...": "...",
            "...": "...",
            "...": "...",
        }

    def test_0010_empty_request(self) -> None:
        ...

    def test_0020_empty_Hash_field(self) -> None:
        ...

    def test_0030_empty_IDCartorio_field(self) -> None:
        ...

    def test_0040_wrong_data_type_for_IDCartorio_field(self) -> None:
        ...

    def test_0050_invalid_IDCartorio_field(self) -> None:
        ...

    def test_0060_missing_IDCartorio_field(self) -> None:
        ...

    def test_0070_empty_Matricula_field(self) -> None:
        ...

    def test_0080_wrong_data_type_for_Matricula_field(self) -> None:
        ...

    def test_0090_invalid_Matricula_field(self) -> None:
        ...

    def test_0100_missing_Matricula_field(self) -> None:
        ...

    def test_0110_empty_NomeRequerente_field(self) -> None:
        ...

    def test_0120_missing_NomeRequerente_field(self) -> None:
        ...

    def test_0130_empty_EmailRequerente_field(self) -> None:
        ...

    def test_0140_invalid_EmailRequerente_field(self) -> None:
        ...

    def test_0150_missing_EmailRequerente_field(self) -> None:
        ...

    def test_0160_empty_CPFRequerente_field(self) -> None:
        ...
