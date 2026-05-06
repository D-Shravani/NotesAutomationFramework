import pytest

from pages.login_page import LoginPage

from utils.config_reader import read_config


@pytest.mark.parametrize(

    "email,password",

    [

        (
            "wrong@gmail.com",
            "wrong123"
        ),

        (
            "",
            "password123"
        ),

        (
            "abc@gmail.com",
            ""
        )

    ]
)

def test_login_negative_datadriven(
    driver,
    email,
    password
):

    config = read_config()

    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        email,
        password
    )

    assert "login" in driver.current_url.lower()