import time
import unittest
import app
from HTMLTestRunner_PY3 import HTMLTestRunner
from script.test_emp_params import TestEmpParams
from script.test_login_params import TestLoginParams

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLoginParams))
suite.addTest(unittest.makeSuite(TestEmpParams))

file = app.BASE_DIR + '/report/ihrm_login_{}.html'.format(time.strftime('%Y%m%d%H%M%S'))

with open(file, 'wb')as f:
    HTMLTestRunner(stream=f, title='ihrm登录接口、操作员工接口的测试报告', description='谷歌执行').run(suite)
