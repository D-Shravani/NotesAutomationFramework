from api.notes_api import NotesAPI

from utils.config_reader import read_config


def test_get_notes_api():

    config = read_config()

    api = NotesAPI(config)

    response = api.get_notes()

    notes = response["data"]

    assert len(notes) > 0

    print(notes)