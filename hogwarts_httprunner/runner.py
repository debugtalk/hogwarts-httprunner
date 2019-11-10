import jsonpath
from requests import sessions

from hogwarts_httprunner.loader import load_yaml
from hogwarts_httprunner.validate import is_api, is_testcase

session = sessions.Session()


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def run_api(api_info):
    """
    :param api_info:
        {
            "request": {},
            "validate: {}
        }
    :return:
    """
    request = api_info["request"]

    method = request.pop("method")
    url = request.pop("url")
    resp = session.request(method, url, **request)

    validator_mapping = api_info["validate"]

    for key in validator_mapping:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)  # resp.key

        expected_value = validator_mapping[key]

        assert actual_value == expected_value

    return True


def run_yaml(yml_file):
    loaded_content = load_yaml(yml_file)
    result = []
    if is_api(loaded_content):
        success = run_api(loaded_content)
        result.append(success)
    elif is_testcase(loaded_content):
        for api_info in loaded_content:
            success = run_api(api_info)
            result.append(success)
    else:
        raise Exception("YAML format invalid: {}".format(yml_file))

    print("result: ", result)
    return result
