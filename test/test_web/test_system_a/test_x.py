from typing import Final, Literal
from time import sleep

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from test import Environment, SystemANotLoggedTestCase, everything_else
from . import constants


class ServiceNotLoggedTestCase(SystemANotLoggedTestCase):
    # Nome do Teste como deve ser escrito no relatório final
    READABLE: Final[str] = "Nome Legível - Human Readable"

    # Tempo de execução deste mesmo teste seguindo as mesmas validações, caso fosse realizado manualmente (em minutos)
    MANUAL_EXEC: Final[int] = ...

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def setUp(self) -> None:
        ...

    def test_0010_(self) -> None:
        ...

    def test_0020_(self) -> None:
        ...

    def test_0030_(self) -> None:
        ...

    def test_0040_(self) -> None:
        ...


class ServiceNotLoggedTestCase(SystemANotLoggedTestCase):
    # Nome do Teste como deve ser escrito no relatório final
    READABLE: Final[str] = "Nome Legível - Human Readable"

    # Tempo de execução deste mesmo teste seguindo as mesmas validações, caso fosse realizado manualmente (em minutos)
    MANUAL_EXEC: Final[int] = ...

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_0010_(self) -> None:
        ...


class ServiceNotLoggedTestCase(SystemANotLoggedTestCase):
    # Nome do Teste como deve ser escrito no relatório final
    READABLE: Final[str] = "Nome Legível - Human Readable"

    # Tempo de execução deste mesmo teste seguindo as mesmas validações, caso fosse realizado manualmente (em minutos)
    MANUAL_EXEC: Final[int] = ...

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_0010_(self) -> None:
        ...


class ServiceNotLoggedTestCase(SystemANotLoggedTestCase):
    # Nome do Teste como deve ser escrito no relatório final
    READABLE: Final[str] = "Nome Legível - Human Readable"

    # Tempo de execução deste mesmo teste seguindo as mesmas validações, caso fosse realizado manualmente (em minutos)
    MANUAL_EXEC: Final[int] = ...

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_0010_(self) -> None:
        ...

...
