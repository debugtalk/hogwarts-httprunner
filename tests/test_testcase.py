import os
import unittest

from hogwarts_httprunner.loader import load_yaml
from hogwarts_httprunner.runner import run_yaml


class TestSingleTestcase(unittest.TestCase):

    def test_loader_single_testcase(self):
        """ 加载出的用例内容与原始信息一致
        """
        single_testcase_yaml = os.path.join(
            os.path.dirname(__file__), "testcase", "mubu_login.yml")
        loaded_json = load_yaml(single_testcase_yaml)
        self.assertIsInstance(loaded_json, list)
        self.assertEqual(len(loaded_json), 3)

    def test_run_testcase_yml(self):
        single_testcase_yaml = os.path.join(
            os.path.dirname(__file__), "testcase", "mubu_login.yml")
        result = run_yaml(single_testcase_yaml)
        self.assertEqual(len(result), 3)
        # self.assertEqual(result, True)
