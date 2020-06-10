import requests
from requests import Response

from app import BASE_URL


class EmployeeApi:
    def __init__(self):
        self.emp_url = BASE_URL + '/api/sys/user'

    def add_emp(self, username, mobile, headers):
        """
        添加员工
        :rtype: Response
        :param username: 请求体用户名
        :param mobile: 请求体手机号码
        :return:
        """
        # 根据外部传入的username和mobile拼接成要发送的请求体数据
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    def query_emp(self, emp_id, headers):
        """
        查询员工
        :rtype: Response
        :param emp_id: 员工id
        :param headers: 请求头
        :return:
        """
        quety_url = self.emp_url + '/' + emp_id
        return requests.get(url=quety_url, headers=headers)

    def modify_emp(self, emp_id, headers, jsonData):
        """
        修改员工
        :rtype: Response
        :param emp_id: 员工id
        :param headers: 请求头
        :param jsonData: 修改员工的数据
        :return:
        """
        modify_url = self.emp_url + '/' + emp_id
        return requests.put(url=modify_url, headers=headers, json=jsonData)

    def delete_emp(self, emp_id, headers):
        """
        删除员工
        :rtype: Response
        :param emp_id: 员工id
        :param headers: 请求头
        :return:
        """
        delete_url = self.emp_url + '/' + emp_id
        return requests.delete(url=delete_url, headers=headers)
