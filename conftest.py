from fixtures.browser_fixture import driver

import pytest


@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        driver.save_screenshot(
            f"screenshots/{item.name}.png"
        )