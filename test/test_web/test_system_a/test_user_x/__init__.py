from os import environ as env

from selenium.webdriver.common.by import By

from test import BaseSeleniumTestCase, SYSTEM_A


USUARIO_X_EMAIL = env.get("USUARIO_X_EMAIL")
USUARIO_X_PWRD = env.get("USUARIO_X_PWRD")


class SystemAUsuarioXLoginPasswordTestCase(BaseSeleniumTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass(new=True)
        cls.driver.get(f"{SYSTEM_A}/...")

        cls.driver.find_element(By.ID, "...").send_keys(str(USUARIO_X_EMAIL))
        cls.driver.find_element(By.ID, "...").send_keys(str(USUARIO_X_PWRD))
        cls.driver.find_element(By.ID, "...").click()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def setUp(self) -> None:
        return super().setUp()
