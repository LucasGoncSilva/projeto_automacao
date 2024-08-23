from test import BaseSeleniumTestCase


class SystemAColors:
    WHITE = "rgb(255, 255, 255)"
    ORANGE = "rgb(255, 133, 0)"
    DARK_BLUE = "rgb(9, 35, 91)"
    DARK_BLUE = "rgb(9, 35, 91)"
    GRAY = "rgb(135, 135, 135)"


class SystemANotLoggedTestCase(BaseSeleniumTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass(new=True)

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def setUp(self) -> None:
        return super().setUp()
