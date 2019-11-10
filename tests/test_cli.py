import os
import unittest
import subprocess


class TestCli(unittest.TestCase):

    def test_hogrun_single_yaml(self):
        # TODO
        pass
        # single_api_yaml = os.path.join(
        #     os.path.dirname(__file__), "api", "api_login_submit.yml")
        # project_root_dir = os.path.dirname(os.path.dirname(__file__))
        # subprocess.run(
        #     "python -m hogwarts_httprunner.cli {}".format(single_api_yaml),
        #     cwd=project_root_dir)
