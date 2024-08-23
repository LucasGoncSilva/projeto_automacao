from typing import Final, Literal

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from test import (
    SYSTEM_A,
    SystemAColors,
    SystemAUsuarioXLoginPasswordTestCase,
    Environment,
    remove_digits,
)
from . import constants


class HomepageUsuarioXLoginPasswordTestCase(SystemAUsuarioXLoginPasswordTestCase):
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
        self.driver.get(f"{SYSTEM_A}/...")
        return super().setUp()

    def test_0010_(self) -> None:
        ...

    def test_0020_(self) -> None:
        ...

    def test_0030_(self) -> None:
        ...
