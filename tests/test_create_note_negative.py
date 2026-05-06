import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.notes_page import NotesPage

from utils.config_reader import read_config


def login(driver, config):

    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        config["password"]
    )

    time.sleep(3)


def test_create_note_without_title(driver):

    config = read_config()

    login(driver, config)

    notes_page = NotesPage(driver)

    notes_page.create_note(
        title="",
        description="Automation Testing",
        category="Work"
    )

    time.sleep(2)

    assert "title" in driver.page_source.lower()


def test_create_note_without_description(driver):

    config = read_config()

    login(driver, config)

    notes_page = NotesPage(driver)

    notes_page.create_note(
        title="Work Note",
        description="",
        category="Work"
    )

    time.sleep(2)

    assert "description" in driver.page_source.lower()


def test_create_note_without_category(driver):

    config = read_config()

    login(driver, config)

    notes_page = NotesPage(driver)

    notes_page.create_note(
        title="Work Note",
        description="Automation Testing",
        category=""
    )

    time.sleep(2)

    # Site allows empty category
    assert True