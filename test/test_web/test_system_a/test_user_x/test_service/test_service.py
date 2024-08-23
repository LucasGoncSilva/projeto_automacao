from time import sleep
from typing import Final

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from test import SYSTEM_A, SystemAColors, SystemAUsuarioXLoginPasswordTestCase
from . import constants


class ServicoUsuarioXLoginPasswordTestCase(SystemAUsuarioXLoginPasswordTestCase):
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
        return super().setUp()

    def test_0010_homepage_card_menu_service(self) -> None:
        ...

    def test_0020_service_page_new_request_text(self) -> None:
        ...

    def test_0030_service_page_listing_text(self) -> None:
        ...

    def test_0040_service_pricing_text(self) -> None:
        ...
