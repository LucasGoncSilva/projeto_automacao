import logging

from zeep import Client

from test import BaseTestCase


class BaseAPITestCase(BaseTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    @classmethod
    def _get_client_path(cls, url: str, endpoint: str) -> Client:
        logging.getLogger("zeep").setLevel(logging.ERROR)
        return Client(url + endpoint)
