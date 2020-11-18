#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_07.py
# @time: 2020/10/11 2:35 下午

import unittest
from test_demo_10 import TestDemo10
from test_demo_10 import TestDemo10_2

class TestDemo12_01(unittest.TestCase):
    def test_add_02(self):
        print('exec TestDemo12_01 test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_01(self):
        print('exec TestDemo12_01 test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_005(self):
        print('exec TestDemo12_01 test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息

class TestDemo12_02(unittest.TestCase):
    def test_add_02(self):
        print('exec TestDemo12_02 test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_01(self):
        print('exec TestDemo12_02 test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_005(self):
        print('exec TestDemo12_02 test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息

if __name__=='__main__':
    #方式一：
    # test_suite = unittest.TestSuite()
    # test_suite.addTest(TestDemo12_01('test_add_01')) # 模块下的类1
    # test_suite.addTest(TestDemo12_02('test_add_005')) # 模块下的类2
    # test_suite.addTest(TestDemo10_2('test_add_01')) # 其它模块下的类
    # unittest.main(defaultTest='test_suite')

    #方式二：
    test_suite = unittest.TestSuite(unittest.makeSuite(TestDemo12_02))
    unittest.main(defaultTest='test_suite')

