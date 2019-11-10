import requests
import unittest


class TestMubuLogin(unittest.TestCase):

    def test_get_homepage(self):

        url = "https://mubu.com/"
        method = "GET"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200

    def test_get_login(self):

        url = "https://mubu.com/login"
        method = "GET"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200

    def test_get_login_password(self):

        url = "https://mubu.com/login/password"
        method = "GET"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
        }
        kwargs = {
            "headers": headers,
            "verify": False
        }
        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200

    def test_post_login(self):

        url = "https://mubu.com/api/login/submit"
        method = "POST"
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        data = "phone=18613143458&password=3AnZNk%26iTteM2PYl1T%24h&remember=true"
        kwargs = {
            "headers": headers,
            "data": data,
            "verify": False
        }

        resp = requests.request(method, url, **kwargs)
        assert resp.status_code == 200
        resp_json = resp.json()
        assert resp_json["code"] == 0
