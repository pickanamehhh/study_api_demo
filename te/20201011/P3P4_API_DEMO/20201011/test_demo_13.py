#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_07.py
# @time: 2020/10/11 2:35 下午

import unittest
from test_demo_10 import TestDemo10
from test_demo_10 import TestDemo10_2
import test_demo_12

class TestDemo13_01(unittest.TestCase):
    def test_add_02(self):
        print('exec TestDemo13_01 test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_01(self):
        print('exec TestDemo13_01 test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_005(self):
        print('exec TestDemo13_01 test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息

class TestDemo13_02(unittest.TestCase):
    def test_add_02(self):
        print('exec TestDemo13_02 test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_01(self):
        print('exec TestDemo13_02 test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_005(self):
        print('exec TestDemo13_02 test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息

if __name__=='__main__':
    #方式三：
    # test_suite = unittest.TestLoader().loadTestsFromTestCase(TestDemo13_02) #类下的所有用例
    # test_suite = unittest.TestLoader().loadTestsFromModule(test_demo_12) #模块下的所有用例
    # loadTestsFromName() 通过字符串的方式引入用例 单个用例 单个类 单个模块
    # test_suite = unittest.TestLoader().loadTestsFromName('test_demo_12.TestDemo12_01.test_add_01')
    # test_suite = unittest.TestLoader().loadTestsFromName('test_demo_12.TestDemo12_01')
    # test_suite = unittest.TestLoader().loadTestsFromName('test_demo_12')

    test_suite = unittest.TestLoader().loadTestsFromName('test_demo_13.TestDemo13_02.test_add_01')
    unittest.main(defaultTest='test_suite')


