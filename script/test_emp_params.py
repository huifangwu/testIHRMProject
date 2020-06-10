import logging
import unittest
from parameterized import parameterized
from api.employee_api import EmployeeApi
from api.login_api import LoginApi
import app
from utils import assert_common, read_emp_data


class TestEmpParams(unittest.TestCase):
    """参数化员工管理模块"""

    def setUp(self):
        self.login_api = LoginApi()
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    def test01_login_success(self):
        """登录成功接口"""
        jsonData = {'mobile': '13800000002', 'password': '123456'}
        response = self.login_api.login(jsonData, {'Content-Type': 'application/json'})
        logging.info('登录成功的结果为：{}'.format(response.json()))
        # 提取登录返回的令牌
        token = 'Bearer ' + response.json().get('data')
        # 把令牌拼接成 HEADERS并保存到全局变量 HEADERS
        app.HEADERS = {'Content-Type': 'application/json', 'Authorization': token}
        logging.info('保存到全局变量中的请求头为：{}'.format(app.HEADERS))
        assert_common(self, 200, True, 10000, '操作成功', response)

    # 定义员工模块的文件路径
    emp_file_path = app.BASE_DIR + '/data/emp_data.json'

    @parameterized.expand(read_emp_data(emp_file_path, 'add_emp'))
    def test02_add_emp(self, username, password, http_code, success, code, message):
        """添加员工接口"""
        response = self.emp_api.add_emp(username, password, app.HEADERS)
        logging.info('添加员工的结果为：{}'.format(response.json()))
        # 提取员工中的令牌并把员工令牌保存到全局变量中
        app.EMP_ID = response.json().get('data').get('id')
        # 打印保存的员工ID
        logging.info('保存到全局变量中的员工id为：{}'.format(app.EMP_ID))
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_emp_data(emp_file_path, 'query_emp'))
    def test03_query_emp(self, http_code, success, code, message):
        """查询员工接口"""
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info('查询员工的结果为：{}'.format(response.json()))
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_emp_data(emp_file_path, 'modify_emp'))
    def test04_modify_emp(self, modify_data, http_code, success, code, message):
        """修改员工接口"""
        response = self.emp_api.modify_emp(app.EMP_ID, app.HEADERS, modify_data)
        logging.info('修改员工的结果为：{}'.format(response.json()))
        assert_common(self, http_code, success, code, message, response)

    @parameterized.expand(read_emp_data(emp_file_path, 'delete_emp'))
    def test05_delete_emp(self, http_code, success, code, message):
        """删除员工接口"""
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info('删除员工的结果为：{}'.format(response.json()))
        assert_common(self, http_code, success, code, message, response)
