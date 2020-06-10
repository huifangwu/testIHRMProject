import requests
from app import BASE_URL
from requests import Response


class LoginApi:
    def __init__(self):
        self.login_url = BASE_URL + '/api/sys/login'

    def login(self, login_data, headers):
        """
        登录接口
        :rtype: Response
        :param login_data: 登录请求体数据
        :param headers: 登录请求头
        :return: 
        """
        return requests.post(url=self.login_url, json=login_data, headers=headers)