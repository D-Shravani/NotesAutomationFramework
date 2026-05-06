from pages.login_page import LoginPage
from utils.config_reader import read_config
from utils.logger import get_logger
from utils.timer import Timer
import pytest

@pytest.mark.smoke

@pytest.mark.ui

def test_login(driver):

    timer = Timer()

    timer.start()

    logger = get_logger()

    logger.info("Starting login test")

    config = read_config()

    logger.info("Opening login page")

    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    logger.info("Entering credentials")

    login_page.login(
        config["email"],
        config["password"]
    )

    logger.info("Login submitted")

    assert "notes" in driver.current_url.lower()

    logger.info("Login test passed successfully")

    execution_time = timer.stop()

    print(
        f"\nExecution Time: {execution_time} seconds"
    )