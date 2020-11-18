#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_07.py
# @time: 2020/10/11 2:35 下午

import unittest
from test_demo_10 import TestDemo10
from test_demo_10 import TestDemo10_2
import test_demo_12

if __name__=='__main__':
    #方式四：
    test_suite_01 = unittest.TestSuite(unittest.makeSuite(TestDemo10))
    test_suite_02 = unittest.TestLoader().loadTestsFromName('test_demo_12.TestDemo12_01')

    all_suite = unittest.TestSuite()
    all_suite.addTests(test_suite_01)
    all_suite.addTests(test_suite_02)

    unittest.main(defaultTest='all_suite')

