import unittest
import logging
from parameterized import parameterized

import app
from api.login_api import LoginApi
from utils import assert_common, read_login_data


class TestLoginParams(unittest.TestCase):

    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    @parameterized.expand(read_login_data(filepath=app.BASE_DIR + '/data/login_data.json'))
    def test_login(self, case_name, request_body, success, code, message, http_code):
        """登录接口"""
        response_login = self.login_api.login(request_body, {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('测试用例《{}》的结果为：{}'.format(case_name, response_login.json()))
        assert_common(self, http_code, success, code, message, response_login)
