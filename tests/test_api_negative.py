import requests

from api.notes_api import NotesAPI

from utils.config_reader import read_config


def test_get_notes_invalid_token():

    config = read_config()

    url = (
        config["api_url"] + "/notes"
    )

    headers = {

        "x-auth-token": "invalid_token"
    }

    response = requests.get(
        url,
        headers=headers
    )

    assert response.status_code == 401


def test_get_notes_without_token():

    config = read_config()

    url = (
        config["api_url"] + "/notes"
    )

    response = requests.get(url)

    assert response.status_code == 401


def test_delete_note_invalid_id():

    config = read_config()

    api = NotesAPI(config)

    invalid_note_id = "123456789"

    response = api.delete_note(
        invalid_note_id
    )

    assert (
        response.status_code == 400
        or
        response.status_code == 404
    )


def test_delete_already_deleted_note():

    config = read_config()

    api = NotesAPI(config)

    notes_response = api.get_notes()

    notes = notes_response["data"]

    assert len(notes) > 0

    note_id = notes[0]["id"]

    # First delete
    api.delete_note(note_id)

    # Delete again
    response = api.delete_note(note_id)

    assert (
        response.status_code == 400
        or
        response.status_code == 404
    )