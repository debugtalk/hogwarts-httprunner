
def is_api(content):
    if not isinstance(content, dict):
        return False

    if "request" not in content:
        return False

    if "validate" not in content:
        return False

    return True


def is_testcase(content):
    if not isinstance(content, list):
        return False

    for item in content:
        if not is_api(item):
            return False

    return True
