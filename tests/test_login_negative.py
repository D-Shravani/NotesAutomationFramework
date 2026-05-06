import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

from utils.config_reader import read_config


def test_login_without_email(driver):

    config = read_config()

    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "",
        config["password"]
    )

    time.sleep(2)

    assert "email" in driver.page_source.lower()


def test_login_without_password(driver):

    config = read_config()

    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        ""
    )

    time.sleep(2)

    assert "password" in driver.page_source.lower()


def test_login_invalid_credentials(driver):

    config = read_config()

    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        "wrong@gmail.com",
        "wrong123"
    )

    time.sleep(2)

    assert (
        "incorrect email address or password"
        in driver.page_source.lower()
    )