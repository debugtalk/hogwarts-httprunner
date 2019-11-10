import re

import jsonpath
from requests import sessions

from hogwarts_httprunner.loader import load_yaml
from hogwarts_httprunner.validate import is_api, is_testcase

session = sessions.Session()
session_variables_mapping = {}

variable_regex_compile = re.compile(r".*\$(\w+).*")


def extract_json_field(resp, json_field):
    value = jsonpath.jsonpath(resp.json(), json_field)
    return value[0]


def replace_var(content, variables_mapping):
    # https://mubu.com/list?code=$code
    matched = variable_regex_compile.match(content)
    if not matched:
        return content

    var_name = matched[1]
    value = variables_mapping[var_name]
    replaced_content = content.replace("${}".format(var_name), str(value))
    return replaced_content


def parse_content(content, variables_mapping):

    if isinstance(content, dict):
        parsed_content = {}
        for key, value in content.items():
            parsed_value = parse_content(value, variables_mapping)
            parsed_content[key] = parsed_value

        return parsed_content

    elif isinstance(content, list):
        parsed_content = []
        for item in content:
            parsed_item = parse_content(item, variables_mapping)
            parsed_content.append(parsed_item)

        return parsed_content

    elif isinstance(content, str):
        return replace_var(content, variables_mapping)

    else:
        return content


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
    global session_variables_mapping
    parsed_request = parse_content(request, session_variables_mapping)

    method = parsed_request.pop("method")
    url = parsed_request.pop("url")
    resp = session.request(method, url, **parsed_request)

    validator_mapping = api_info["validate"]

    for key in validator_mapping:
        if "$" in key:
            # key = "$.code"
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)  # resp.key

        expected_value = validator_mapping[key]

        assert actual_value == expected_value

    extractor_mapping = api_info.get("extract", {})
    for var_name in extractor_mapping:
        var_expr = extractor_mapping[var_name]  # $.code
        var_value = extract_json_field(resp, var_expr)
        session_variables_mapping[var_name] = var_value

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
