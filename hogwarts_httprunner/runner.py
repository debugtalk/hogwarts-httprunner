import jsonpath
import requests

from hogwarts_httprunner.loader import load_yaml


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def run_yaml(yml_file):
    load_json = load_yaml(yml_file)

    request = load_json["request"]

    method = request.pop("method")
    url = request.pop("url")
    resp = requests.request(method, url, **request)

    validator_mapping = load_json["validate"]

    for key in validator_mapping:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)  # resp.key

        expected_value = validator_mapping[key]

        assert actual_value == expected_value

    return True
