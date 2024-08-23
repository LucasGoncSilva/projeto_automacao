# ruff: noqa: E402

from functools import partial
import unittest
from csv import writer
from os import environ as env, path
from re import compile, fullmatch
from typing import Callable, Final, Pattern, Literal
from time import perf_counter
from inspect import getfile
from datetime import datetime


ENVIRONMENT: Final[str | None] = env.get("ENVIRONMENT")
if ENVIRONMENT not in ["PRE", "PROD"]:
    raise ValueError(
        f'"ENVIRONMENT" variable must be a Literal["PRE", "PROD"] but was actually "{ENVIRONMENT}"'
    )

REGEX_EMAIL: Final[Pattern[str]] = compile(
    r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
)
REGEX_CPF_CNPJ: Final[Pattern[str]] = compile(
    r"([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})"
)

GENERATE_REPORT: Final[bool | None] = (
    True if env.get("GENERATE_REPORT") == "True" else False
)
REPORT_FILE_GENERAL_CASES_PATH: Final[str] = "report/resource.csv"
CREATE_REPORT_GENERAL_CASES_HEADER: bool = True
REPORT_FILE_TESTS_CASES_PATH: Final[str] = "report/test_cases.txt"
CREATE_REPORT_TESTS_CASES: bool = True


class ClassProperty:
    def __init__(self, func):
        self.fget = func

    def __get__(self, instance, owner):
        return self.fget(owner)


class Environment:
    PRE_SYSTEM_A: Final[str] = "..."
    PRE_API_SYSTEM_A: Final[str] = "..."
    PRE_API_SYSTEM_B: Final[str] = "..."

    PROD_SYSTEM_A: Final[str] = "..."
    PROD_API_SYSTEM_A: Final[str] = "..."
    PROD_API_SYSTEM_B: Final[str] = "..."

    @ClassProperty
    def SYSTEM_A(cls) -> str:
        return cls.PRE_SYSTEM_A if ENVIRONMENT == "PRE" else cls.PROD_SYSTEM_A

    @ClassProperty
    def APISYSTEM_B(cls) -> str:
        return cls.PRE_API_SYSTEM_B if ENVIRONMENT == "PRE" else cls.PROD_API_SYSTEM_B

    @ClassProperty
    def APISYSTEM_A(cls) -> str:
        return cls.PRE_API_SYSTEM_A if ENVIRONMENT == "PRE" else cls.PROD_API_SYSTEM_A


class BaseTestCase(unittest.TestCase):
    READABLE = ""
    MANUAL_EXEC = 0

    @classmethod
    def setUpClass(cls) -> None:
        if GENERATE_REPORT:
            cls.create_tests_cases_report_case(cls.__name__)

            if CREATE_REPORT_GENERAL_CASES_HEADER:
                create_csv_general_cases_report()
            cls.__start: float = perf_counter()

    @classmethod
    def tearDownClass(cls) -> None:
        if GENERATE_REPORT:
            cls.__end: float = perf_counter()
            __exec_time: Final[float] = round((cls.__end - cls.__start), 3)

            __test_name: Final[str] = cls.__name__

            __script_path: Final[str] = path.abspath(getfile(cls))
            __test_path: Final[str] = ".".join(
                (
                    path.splitext(path.relpath(__script_path, start="test"))[0].replace(
                        path.sep, "."
                    )
                    + f".{__test_name}"
                ).split(".")[:-1]
            )

            __methods_count: Final[int] = len(
                [i for i in dir(cls) if i.startswith("test_")]
            )

            __test_type: Final[Literal["API", "WEB"]] = (
                "WEB" if __test_path.startswith("test_web") else "API"
            )

            test_name: Final[str] = __test_name
            test_type: Final[Literal["API", "WEB"]] = __test_type
            test_path: Final[str] = __test_path
            methods_count: Final[int] = __methods_count
            duration: Final[float] = __exec_time
            readable: Final[str] = cls.READABLE
            manual_exec: Final[int] = (
                ((3 + 3 * __methods_count) * 60)
                if __test_type == "API"
                else cls.MANUAL_EXEC * 60
            )  # Explicação a seguir

            """
            Configs para calculo de execução manual de cada teste API

            3' validação das operações possíveis para cada caso
            1' configuração e execução de cada request de cada cenário
            1' validação de cada retorno (macro=response e micro=tags)
            1' validação de cada retorno (macro=response e micro=tags)

            TOTAL = (3 + {NUM_TESTES} * 3) * 60
            """

            create_csv_general_cases_report(
                name=test_name,
                _type=test_type,
                path=test_path,
                methods_count=methods_count,
                duration=duration,
                readable=readable,
                manual_exec=manual_exec,
            )

    def setUp(self) -> None:
        self.create_tests_cases_report_test(self._testMethodName)

    @classmethod
    def skipTest(cls, reason: str) -> Callable:
        return unittest.skip(reason)

    @classmethod
    def create_tests_cases_report_case(cls, case_arg: str) -> None:
        return partial(create_tests_cases_report, case=case_arg)()

    def create_tests_cases_report_test(self, test_arg: str) -> None:
        return partial(create_tests_cases_report, test=test_arg)()


def create_tests_cases_report(case: str | None = None, test: str | None = None) -> None:
    if not GENERATE_REPORT:
        return

    if all([case, test]) or not any([case, test]):
        raise TypeError(
            f"Expected any case or test to be None, got both same type:\n\t{type(case) = }\n\t{type(test)}"
        )

    global CREATE_REPORT_TESTS_CASES
    mode: Literal["a", "w"] = "w" if CREATE_REPORT_TESTS_CASES else "a"
    with open(REPORT_FILE_TESTS_CASES_PATH, mode=mode) as file:
        if case:
            file.write(f"{case.removesuffix('TestCase')}:\n")
        elif test:
            file.write(f"\t\t{test[10:]}\n")

    CREATE_REPORT_TESTS_CASES = False


# Regex testing ('v' stands for 'validate')
def v_CPF_CNPJ(token: str) -> bool:
    return bool(fullmatch(REGEX_CPF_CNPJ, token))


def v_email(token: str) -> bool:
    return bool(fullmatch(REGEX_EMAIL, token))


def remove_digits(text: str) -> str:
    temp: list[str] = list(text)
    for i, c in enumerate(text):
        if c.isdigit():
            temp[i] = "|"
    return "".join(temp)


def create_csv_general_cases_report(
    name: str = "",
    _type: Literal["WEB", "API"] = "WEB",
    path: str = "",
    methods_count: int = 0,
    duration: float = 0.0,
    readable: str = "",
    manual_exec: int = 0,
) -> None:
    if not GENERATE_REPORT:
        return

    global CREATE_REPORT_GENERAL_CASES_HEADER
    mode: Literal["a", "w"] = "w" if CREATE_REPORT_GENERAL_CASES_HEADER else "a"
    data: list[bool | str | int | float] = (
        ["name", "type", "path", "methods_count", "duration", "readable", "manual_exec"]
        if CREATE_REPORT_GENERAL_CASES_HEADER
        else [name, _type, path, methods_count, duration, readable, manual_exec]
    )
    with open(
        REPORT_FILE_GENERAL_CASES_PATH, mode=mode, encoding="utf-8", newline=""
    ) as file:
        cursor = writer(file)
        cursor.writerow(data)
    CREATE_REPORT_GENERAL_CASES_HEADER = False


def save_protocol(protocol: str, func_name: str) -> None:
    PROTOCOL_FILE_PATH: Final[str] = "protocols/history.txt"

    try:
        with open(PROTOCOL_FILE_PATH, "a") as f:
            f.write(
                f"{protocol}\t\t\t{ENVIRONMENT}\t\t\t{func_name}\t\t\t{datetime.now()}\n"
            )
    except FileNotFoundError:
        with open(PROTOCOL_FILE_PATH, "w") as f:
            f.write(
                f"{protocol}\t\t\t{ENVIRONMENT}\t\t\t{func_name}\t\t\t{datetime.now()}\n"
            )


SYSTEM_A: Final[str] = Environment.SYSTEM_A
APISYSTEM_A: Final[str] = Environment.APISYSTEM_A


from .test_web import BaseSeleniumTestCase

from .test_web.test_system_a import SystemANotLoggedTestCase, SystemAColors
from .test_web.test_system_a.test_user_x import SystemAUsuarioXLoginPasswordTestCase


from .test_api import BaseAPITestCase

from .test_api.test_apisystem_a import APISystemATestCase
from .test_api.test_apisystem_a.test_service_x import ServiceAPISystemATestCase

# Importações de demais arquivos __init__.py
...

__all__ = [
    "BaseSeleniumTestCase",
    "SystemANotLoggedTestCase",
    "SystemAColors",
    "SystemAUsuarioXLoginPasswordTestCase",
    "BaseAPITestCase",
    "APISystemATestCase",
    "ServiceAPISystemATestCase",
    ...
]
