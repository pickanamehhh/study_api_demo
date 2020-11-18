#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_create_tag_api_case.py
# @time: 2020/10/14 9:23 下午

import requests
import unittest
from common.config_utils import config

class TestCreatetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_create_tag(self):
        self._testMethodName = 'case04'
        self._testMethodDoc = '验证create_tag接口能否成功调用'
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wx55614004f367f8ca",
            "secret": "65515b46dd758dfdb09420bb7db2c67f"
        }
        response = self.session.get(url='https://%s/cgi-bin/token' % self.HOSTS,
                                    params=get_param_dict)
        token_id = response.json()['access_token']

        post_data = {   "tag" : {     "name" : "newdreamP3P4"   } }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     json=post_data)
        actual_result = response.json()['tag']['name']
        self.assertEqual(actual_result,'newdreamP3P4','case04 验证create_tag接口能否成功调用')

if __name__=='__main__':
    unittest.main(verbosity=2)