import uuid
import requests

TEST_ENDPOINT = "https://reqres.in"


def test_call_endpoint():
    response = requests.get(TEST_ENDPOINT + "/api/users?page=2")
    assert response.status_code == 200


def test_create_new_user():
    payload = new_user_payload()
    create_new_user = create_request(payload)
    assert create_new_user.status_code == 201
    data = create_new_user.json()

    user_id = data["id"]


def create_request(payload):
    return requests.post(TEST_ENDPOINT + "/api/users", json=payload)


def new_user_payload():
    user_name = f"test_user{uuid.uuid4().hex}"
    job_title = f"test_job_title{uuid.uuid4().hex}"

    return {
        "name": user_name,
        "job": job_title,
    }
