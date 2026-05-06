import json

def read_config():

    with open("config/config.json") as config_file:
        return json.load(config_file)