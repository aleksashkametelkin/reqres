import requests
from faker import Faker

fake = Faker()


TEST_ENDPOINT = "https://reqres.in"  # also docs located and available there


def register_new_user(username):
    return requests.post(TEST_ENDPOINT + f"/api/register", json=username)


def login_new_user(username):
    return requests.post(TEST_ENDPOINT + f"/api/login", json=username)


def create_user_name(payload):
    return requests.post(TEST_ENDPOINT + "/api/users", json=payload)


def get_user_by_id(user_id):
    return requests.get(TEST_ENDPOINT + f"/api/users/{user_id}")


def get_resource_list():
    return requests.get(TEST_ENDPOINT + f"/api/unknown")


def get_resource_by_id(resource_id):
    return requests.get(TEST_ENDPOINT + f"/api/unknown/{resource_id}")


def new_user_payload():
    return {
        "name": f"{fake.name()}",
        "job": f"{fake.job()}"
    }


def login_user_payload():
    # body must be hardcoded to receive hardcoded ID and Token in answer
    return {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }


def register_user_payload():
    # body must be hardcoded to receive hardcoded ID and Token in answer
    return {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
