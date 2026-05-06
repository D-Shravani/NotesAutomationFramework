import requests


class NotesAPI:

    def __init__(self, config):

        self.base_url = config["api_url"]

        self.email = config["email"]

        self.password = config["password"]

        self.token = self.get_token()

    def get_token(self):

        url = self.base_url + "/users/login"

        payload = {

            "email": self.email,

            "password": self.password
        }

        response = requests.post(
            url,
            json=payload
        )

        data = response.json()

        return data["data"]["token"]

    def get_headers(self):

        return {

            "x-auth-token": self.token
        }

    def get_notes(self):

        url = self.base_url + "/notes"

        response = requests.get(
            url,
            headers=self.get_headers()
        )

        return response.json()

    def delete_note(self, note_id):

        url = self.base_url + f"/notes/{note_id}"

        response = requests.delete(
            url,
            headers=self.get_headers()
        )

        return response