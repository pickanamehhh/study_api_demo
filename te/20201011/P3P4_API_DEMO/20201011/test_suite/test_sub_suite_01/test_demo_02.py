#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_07.py
# @time: 2020/10/11 2:35 下午

import unittest


class TestDemo02_01(unittest.TestCase):
    def test_add_02(self):
        print('exec t1 TestDemo02_01 test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_01(self):
        print('exec t1 TestDemo02_01 test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_005(self):
        print('exec t1 TestDemo02_01 test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息

class TestDemo02_02(unittest.TestCase):
    def test_add_02(self):
        print('exec t1 TestDemo02_02 test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_01(self):
        print('exec t1 TestDemo02_02 test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    def test_add_005(self):
        print('exec t1 TestDemo02_02 test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息

if __name__=='__main__':
    unittest.main()
