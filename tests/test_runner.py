import os
import unittest

from hogwarts_httprunner.runner import replace_var


class TestHogRunner(unittest.TestCase):

    def test_replace_var_no_var(self):
        raw_str = "https://mubu.com/list?code=123"
        variables_mapping = {
            "code": 0
        }
        replace_str = replace_var(raw_str, variables_mapping)
        self.assertEqual(replace_str, "https://mubu.com/list?code=123")

    def test_replace_var(self):
        raw_str = "https://mubu.com/list?code=$code"
        variables_mapping = {
            "code": 0
        }
        replace_str = replace_var(raw_str, variables_mapping)
        self.assertEqual(replace_str, "https://mubu.com/list?code=0")
