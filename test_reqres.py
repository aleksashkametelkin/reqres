import random
import requests

import utils as u


def test_call_endpoint():
    response = requests.get(u.TEST_ENDPOINT + "/api/users")
    assert response.status_code == 200


def test_register_new_user():
    # successful registration a new user
    username = u.register_user_payload()
    reg = u.register_new_user(username)
    assert reg.status_code == 200

    # unsuccessful registration a new user
    reg = u.register_new_user("email" == "rfdskn@fdsk.com")
    assert reg.status_code == 400


def test_login_new_user():
    # successful registration a new user
    username = u.login_user_payload()
    reg = u.login_new_user(username)
    assert reg.status_code == 200

    # unsuccessful registration a new user
    reg = u.register_new_user("email" == "rfdskn@fdsk.com")
    assert reg.status_code == 400


def test_create_new_user():
    # create new user
    payload = u.new_user_payload()
    create_new_user = u.create_user_name(payload)
    assert create_new_user.status_code == 201

    # we don't need to save user id because API can respond only first 12 hardcoded user ID's
    # check that first 12 user ID's work correctly
    for _ in range(1, 13):
        get_user = u.get_user_by_id(_)
        assert get_user.status_code == 200

    # check that any ID from 13 to 1000 respond 404
    get_unavailable_user = u.get_user_by_id(random.randrange(13, 1000))
    assert get_unavailable_user.status_code == 404


def test_resource():
    # get resource list
    resource_list = u.get_resource_list()
    assert resource_list.status_code == 200

    # get resource by id. Only 12 ID available to get 200 status code
    for _ in range(1, 13):
        single_resource = u.get_resource_by_id(_)
        assert single_resource.status_code == 200

    # check that any ID from 13 to 1000 respond 404
    get_unavailable_resource = u.get_user_by_id(random.randrange(13, 1000))
    assert get_unavailable_resource.status_code == 404
