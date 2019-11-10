import requests

from hogwarts_httprunner.loader import load_yaml


def run_yaml(yml_file):
    load_json = load_yaml(yml_file)

    request = load_json["request"]

    method = request.pop("method")
    url = request.pop("url")
    resp = requests.request(method, url, **request)

    validator_mapping = load_json["validate"]

    for key in validator_mapping:
        actual_value = getattr(resp, key)  # resp.key
        expected_value = validator_mapping[key]

        assert actual_value == expected_value

    return True
