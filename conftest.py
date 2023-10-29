import random
from typing import Callable, Any

import pytest
from _pytest.python import Function
from _pytest.reports import TestReport
from _pytest.runner import CallInfo

from config import (
    RUN_TEST_WITH_IDS,
    RUN_TEST_WITH_NAME,
    EXTEND_LOGGING,
    EXPORT_RESULTS,
)

pytest_plugins = [
    "plugins.hello_world_plugin",
    "plugins.export_result_plugin",
    "plugins.logger_plugin",
]
_EXPORT_RESULT = []


def pytest_collection_modifyitems():
    if RUN_TEST_WITH_IDS:
        print(f"Executing tests with ids {RUN_TEST_WITH_IDS}")
    elif RUN_TEST_WITH_NAME:
        print(f"Executing tests with name {RUN_TEST_WITH_NAME}")


@pytest.fixture(autouse=True)
def write_case_id(record_property: Callable[[str, Any], None]):
    if EXPORT_RESULTS:
        rand = random.randint(1, 1000)
        record_property("case_id", f"my_cool_id_{rand}")


def pytest_runtest_setup(item: Function):
    if EXTEND_LOGGING:
        total_tests = len(item.session.items)
        current_index = item.session.items.index(item) + 1
        text = f"Running test {item.name} ({current_index} of {total_tests})"
        print("\n" + text.center(80, "="))


def pytest_runtest_makereport(call: CallInfo):
    if EXTEND_LOGGING:
        print(f"Stage '{call.when}' has finished")


def pytest_report_teststatus(report: TestReport):
    if EXPORT_RESULTS and report.when == "teardown":
        case_id = [
            data[1] for data in report.user_properties if data[0] == "case_id"
        ]
        if case_id:
            _EXPORT_RESULT.append({"id": case_id, "result": report.outcome})


def pytest_sessionfinish():
    if EXPORT_RESULTS:
        print("Results to export:")
        print(_EXPORT_RESULT)

    if EXTEND_LOGGING:
        print("Test session finished!")
