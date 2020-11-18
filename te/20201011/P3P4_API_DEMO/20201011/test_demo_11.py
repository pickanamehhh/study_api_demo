#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_07.py
# @time: 2020/10/11 2:35 下午

import unittest

class TestDemo11(unittest.TestCase):
    def setUp(self) -> int:   # -> None 表示函数可能的返回值（不强制） public int add()
        print('setup 测试初始化')
    def tearDown(self) -> None:
        print('tearDown 测试清理')
    @unittest.skip('就是不想执行') #无条件跳过
    def test_add_02(self):
        print('exec test_add02测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    @unittest.skipIf(True,'条件为真时跳过')
    def test_add_01(self):
        print('exec test_add01测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    @unittest.skipUnless(False,'条件为假跳过')
    def test_add_005(self):
        print('exec test_add005测试用例')
        self.assertEqual(1+3,4,'test_add用例执行失败')   # 自定义错误信息
    @unittest.expectedFailure  #不统计用例执行的失败结果
    def test_add_006(self):
        print('exec test_add005测试用例')
        self.assertEqual(1+3,5,'test_add用例执行失败')   # 自定义错误信息

if __name__=='__main__':
    unittest.main()

