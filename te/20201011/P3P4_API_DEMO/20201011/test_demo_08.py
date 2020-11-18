#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_07.py
# @time: 2020/10/11 2:35 下午

import unittest

class TestDemo07(unittest.TestCase):
    def setUp(self) -> int:
        print('setup 测试初始化')
    def tearDown(self) -> None:
        print('tearDown 测试清理')
    def test_add_01(self):
        print('exec test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
        self.assertTrue(1==1)
        a = None
        self.assertIsNone(a)
        self.assertIn('abc','abcdef')


if __name__=='__main__':
    unittest.main()

