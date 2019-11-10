import requests


def test_get_homepage():

    url = "https://mubu.com/"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, verify=False)
    assert resp.status_code == 200


def test_get_login():

    url = "https://mubu.com/login"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, verify=False)
    assert resp.status_code == 200


def test_get_login_password():

    url = "https://mubu.com/login/password"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
    }
    resp = requests.get(url, headers=headers, verify=False)
    assert resp.status_code == 200


def test_post_login():

    url = "https://mubu.com/api/login/submit"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    data = "phone=18613143458&password=3AnZNk%26iTteM2PYl1T%24h&remember=true"
    resp = requests.post(url, headers=headers, data=data, verify=False)
    assert resp.status_code == 200
    resp_json = resp.json()
    assert resp_json["code"] == 0


if __name__ == '__main__':
    test_get_homepage()
    test_get_login()
    test_get_login_password()
    test_post_login()
