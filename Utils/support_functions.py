import os
import json
import requests
from datetime import datetime


ENDPOINT = "https://reqres.in/api/"


def open_file():

    file_path = 'payload.json'
    with open(os.path.abspath(file_path), 'r') as file:
        data = json.load(file)
    return data


def get_list_users():

    return requests.get(ENDPOINT + "users?page=2")


def create_user(payload):

    return requests.post(ENDPOINT + "users", json=payload)


def count_key_items(d, key):

    if key in d:
        return len(d[key])


def check_data_types(d, source):

    file_path_list = 'expected_response_get_list.json'
    file_path_create = 'expected_response_create_user.json'

    if source == 1:
        for key, value in d.items():
            if source == 1:
                with open(os.path.abspath(file_path_list), 'r') as file:
                    data = json.load(file)
                if key in data:
                     assert type(data[key]) is type(value), \
                        f"actual data type: '{type(value)}', expected data type: '{data[key]}'"
            elif source == 2:
                with open(os.path.abspath(file_path_create), 'r') as file:
                    data = json.load(file)
                if key in data:
                     assert type(data[key]) is type(value), \
                        f"actual data type: '{type(value)}', expected data type: '{data[key]}'"


def check_timestamp(time):

    if datetime.fromisoformat(time.replace("Z", "+00:00")):
        return time
