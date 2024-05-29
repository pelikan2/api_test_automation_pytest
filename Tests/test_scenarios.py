import time
from Utils import support_functions


def test_get_list_users():

    get_user_response = support_functions.get_list_users()
    get_user_response = get_user_response.json()

    support_functions.check_data_types(get_user_response, 1)
    assert get_user_response["data"][0]["last_name"] == "Lawson"
    assert get_user_response["data"][1]["last_name"] == "Ferguson"
    assert 'total' in get_user_response, "key is not in dictionary"
    assert get_user_response["total"] == 12
    assert (get_user_response["total"] == support_functions.count_key_items(get_user_response, "data")
            * get_user_response["page"])


def test_create_user():

    payload = support_functions.open_file()
    response_time_limit = 300
    start_time = time.time()
    create_user_response = support_functions.create_user(payload)
    end_time = time.time()
    response_time = (end_time - start_time) * 1000
    response = create_user_response.json()

    assert create_user_response.status_code == 201, "Wrong status code"
    assert 'id' in response, "id is missing in the response"
    assert type(response['id']) is str, "id data type isn't string"
    assert 'createdAt' in response, "createdAt missing in the response"
    assert support_functions.check_timestamp(response['createdAt']) is True, "this is not valid timestamp"
    assert response_time < response_time_limit, \
        "Response time is bigger than expected"
    support_functions.check_data_types(response, 2)
