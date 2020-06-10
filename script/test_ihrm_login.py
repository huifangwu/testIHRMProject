import unittest
import logging
from api.login_api import LoginApi
from utils import assert_common


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    def test01_login_success(self):
        """登录成功"""
        response_login = self.login_api.login({'mobile': '13800000002', 'password': '123456'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('登录成功的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, True, 10000, '操作成功', response_login)

    def test02_mobile_is_empty(self):
        """手机号码为空"""
        response_login = self.login_api.login({'mobile': '', 'password': 'error'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('手机号码为空的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test03_password_is_empty(self):
        """密码为空"""
        response_login = self.login_api.login({'mobile': '13800000002', 'password': ''},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('密码为空的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test04_mobile_is_not_exists(self):
        """手机号码不存在"""
        response_login = self.login_api.login({'mobile': '15018848443', 'password': '123456'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('手机号码不存在的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test05_password_error(self):
        """密码错误"""
        response_login = self.login_api.login({'mobile': '13800000002', 'password': '1234567'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('密码错误的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test06_params_is_none(self):
        """无参"""
        response_login = self.login_api.login({}, {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('无参的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test07_params_is_null(self):
        """参数传入null"""
        response_login = self.login_api.login(None, {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('参数传入None的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 99999, '抱歉，系统繁忙，请稍后重试', response_login)

    def test08_more_params(self):
        """参数传入null"""
        response_login = self.login_api.login({"mobile": "13800000002", "password": "123456", "extras_params": "1"},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('参数传入None的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, True, 10000, '操作成功', response_login)

    def test09_less_params_mobile(self):
        """少参-缺少mobile"""
        response_login = self.login_api.login({'password': '1234567'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('少参-缺少mobile的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test10_less_params_password(self):
        """少参-缺少password"""
        response_login = self.login_api.login({'mobile': '13800000002'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('少参-缺少password的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)

    def test11_error_params(self):
        """错误参数"""
        response_login = self.login_api.login({'moblie': '13800000002', 'password': '123456'},
                                              {'Content-Type': 'application/json'})
        # 打印日志
        logging.info('错误参数的结果为：{}'.format(response_login.json()))
        assert_common(self, 200, False, 20001, '用户名或密码错误', response_login)
