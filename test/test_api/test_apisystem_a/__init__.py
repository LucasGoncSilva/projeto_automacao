from hashlib import sha256

from zeep import Client

from test import APISYSTEM_A, BaseAPITestCase, ClassProperty


class APISystemATestCase(BaseAPITestCase):
    hashlist: list[str] = []

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    @classmethod
    def _get_client(cls, endpoint: str) -> Client:
        return super()._get_client_path(APISYSTEM_A, endpoint)

    @classmethod
    def __get_tokens(cls) -> list[str]:
        r: dict = cls._get_client(
            "/..."
        ).service.SomeService(
            oRequest={
                "...": "...",
                "...": "...",
                "...": "...",
                "...": "...",
                "...": "...",
                "...": "...",
            }
        )

        return list(r["..."]["..."])

    @classmethod
    def __digest(cls) -> None:
        temp: list[str] = []
        for token in cls.__get_tokens():
            params = (
                "..."
                + token
            )
            _hash = sha256(bytes(params, "utf-8")).hexdigest().upper()
            temp.append(_hash)
        cls.hashlist = temp.copy()

    @ClassProperty
    def hash(cls) -> str:
        if not len(cls.hashlist):
            cls.__digest()

        return cls.hashlist.pop()
