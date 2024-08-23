from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.remote.webelement import WebElement

from test import BaseTestCase


class BaseSeleniumTestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls, new: bool = False) -> None:
        if new:
            options: FirefoxOptions = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")

            cls.driver: Firefox = Firefox(options=options)
            cls.driver.implicitly_wait(30)
            cls.driver.maximize_window()

        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        return super().tearDownClass()

    @classmethod
    def firefox_scroll(cls, e: WebElement) -> None:
        x: int = e.location["x"]
        y: int = e.location["y"]
        scroll_by_coord: str = f"window.scrollTo({x}, {y});"
        scroll_nav_out_of_way: str = "window.scrollBy(0, -120);"
        cls.driver.execute_script(scroll_by_coord)
        cls.driver.execute_script(scroll_nav_out_of_way)

    @classmethod
    def export_driver(cls) -> Firefox:
        cls.setUpClass(True)
        return cls.driver
