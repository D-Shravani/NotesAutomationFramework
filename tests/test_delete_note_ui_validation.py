import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from api.notes_api import NotesAPI

from pages.login_page import LoginPage

from utils.config_reader import read_config


def test_delete_specific_note(driver):

    config = read_config()

    # API PART
    api = NotesAPI(config)

    notes_response = api.get_notes()

    notes = notes_response["data"]

    assert len(notes) > 0

    # TARGET NOTE
    target_title = "Personal Reminder"

    target_category = "Personal"

    note_id = None

    # FIND SPECIFIC NOTE
    for note in notes:

        if (
            note["title"] == target_title
            and
            note["category"] == target_category
        ):

            note_id = note["id"]

            break

    # VALIDATE NOTE FOUND
    assert note_id is not None

    # DELETE SPECIFIC NOTE
    delete_response = api.delete_note(
        note_id
    )

    assert delete_response.status_code == 200

    # UI PART
    driver.get(
        config["base_url"] + "/login"
    )

    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        config["password"]
    )

    time.sleep(3)

    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "body")
        )
    )

    # GET ALL VISIBLE NOTES
    notes_elements = driver.find_elements(
        By.CLASS_NAME,
        "card-title"
    )

    visible_notes = []

    for note in notes_elements:

        visible_notes.append(
            note.text
        )

    # VERIFY DELETED NOTE NOT VISIBLE
    assert target_title not in visible_notes