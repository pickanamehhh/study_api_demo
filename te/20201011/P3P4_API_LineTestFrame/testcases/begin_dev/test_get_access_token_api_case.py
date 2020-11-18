#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_get_access_token_api_case.py
# @time: 2020/10/11 5:19 下午

import requests
import unittest

class TestGetaccesstokenApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
    def tearDown(self) -> None:
        self.session.close()

    def test_get_accesstoken_success(self):
        self._testMethodName = 'case01'
        self._testMethodDoc = '验证get_access_token接口能否成功调用'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wx55614004f367f8ca",
            "secret": "65515b46dd758dfdb09420bb7db2c67f"
        }
        response = self.session.get( url='https://api.weixin.qq.com/cgi-bin/token',
                         params=get_param_dict)
        actual_result = response.status_code
        self.assertEqual(actual_result,200,'case01 验证get_access_token接口能否成功调用')

if __name__=='__main__':
    unittest.main()