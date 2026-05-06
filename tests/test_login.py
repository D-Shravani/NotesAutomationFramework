from pages.login_page import LoginPage
from utils.config_reader import read_config

def test_login(driver):

    config = read_config()

    driver.get(config["base_url"] + "/login")

    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        config["password"]
    )

    assert "notes" in driver.current_url.lower()