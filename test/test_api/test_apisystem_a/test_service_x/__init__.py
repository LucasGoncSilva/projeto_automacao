from zeep import Client

from test import APISystemATestCase


class ServiceAPISystemATestCase(APISystemATestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c: Client = APISystemATestCase._get_client("/...")
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()
