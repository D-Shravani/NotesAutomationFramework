import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.notes_page import NotesPage

from utils.config_reader import read_config


def test_create_multiple_notes(driver):

    config = read_config()

    driver.get(
        config["base_url"] + "/login"
    )

    # LOGIN
    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        config["password"]
    )

    time.sleep(3)

    # WAIT FOR DASHBOARD
    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "body")
        )
    )

    # NOTES PAGE OBJECT
    notes_page = NotesPage(driver)

    # MULTIPLE NOTES DATA
    notes_data = [

        {
            "title": "Work Meeting",
            "description": "Client discussion at 5 PM",
            "category": "Work"
        },

        {
            "title": "Personal Reminder",
            "description": "Buy groceries and fruits",
            "category": "Personal"
        },

        {
            "title": "Home Tasks",
            "description": "Clean room and arrange books",
            "category": "Home"
        }

    ]

    # CREATE MULTIPLE NOTES
    for note in notes_data:

        notes_page.create_note(

            title=note["title"],

            description=note["description"],

            category=note["category"]
        )

        time.sleep(2)

    # VALIDATION
    for note in notes_data:

        assert note["title"] in driver.page_source