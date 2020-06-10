import json
import logging
import app
from logging.handlers import TimedRotatingFileHandler


def init_logging():
    """打印日志"""
    # 日志器、处理器、格式化器
    rizhiqi = logging.getLogger()

    kongzhitai = logging.StreamHandler()
    wenjian = TimedRotatingFileHandler(filename=app.BASE_DIR + '/log/ihrm.log',
                                       when='midnight',
                                       interval=1,
                                       backupCount=3,
                                       encoding='utf-8')

    geshihua = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] %(message)s')

    # 设置日志器等级
    rizhiqi.setLevel(logging.INFO)

    # 处理器设置格式化器
    kongzhitai.setFormatter(geshihua)
    wenjian.setFormatter(geshihua)

    # 日志器添加处理器
    rizhiqi.addHandler(kongzhitai)
    rizhiqi.addHandler(wenjian)


def assert_common(self, http_code, success, code, message, response):
    """断言"""
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get('success'))
    self.assertEqual(code, response.json().get('code'))
    self.assertIn(message, response.json().get('message'))


def read_login_data(filepath):
    """读取登录数据"""
    with open(filepath, 'r', encoding='utf-8')as f:
        # 使用json加载数据文件为json格式
        jsonData = json.load(f)
        # 遍历json格式的数据文件，并把数据处理成列表元组形式([(),(),()])
        result_list = list()
        for login_data in jsonData:  # type:dict
            # 把每一组登录数据的所有values转化为元组形式，并添加到列表中
            result_list.append(tuple(login_data.values()))
    return result_list


def read_emp_data(filepath, interface_name):
    with open(filepath, 'r', encoding='utf-8')as f:
        jsonData = json.load(f)  # type:dict
        emp_data = jsonData.get(interface_name)  # type:dict
        result_list = list()
        result_list.append(tuple(emp_data.values()))
        return result_list


if __name__ == '__main__':
    # 调用read_login_data函数
    # 定义数据文件的目录（注意这个路径指向数据文件一定需要存在）
    login_file_path = app.BASE_DIR + '/data/login_data.json'
    # 读取路径中数据，并接受返回结果
    result_login_list = read_login_data(login_file_path)
    # 打印返回的结果
    print('查看读取的登录数据为：', result_login_list)

    # 调用read_emp_data函数
    emp_file_path = app.BASE_DIR + '/data/emp_data.json'
    print('添加员工数据为：', read_emp_data(emp_file_path, 'add_emp'))
    print('查询员工数据为：', read_emp_data(emp_file_path, 'query_emp'))
    print('修改员工数据为：', read_emp_data(emp_file_path, 'modify_emp'))
    print('删除员工数据为：', read_emp_data(emp_file_path, 'delete_emp'))
