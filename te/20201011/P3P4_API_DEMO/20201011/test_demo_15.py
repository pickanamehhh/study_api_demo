#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_15.py
# @time: 2020/10/11 4:03 下午

import unittest
import os

case_path = os.path.join(os.path.dirname(__file__),'test_suite')

discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_demo*.py',
                                               top_level_dir=case_path)
all_suite = unittest.TestSuite()
all_suite.addTest( discover )

unittest.main(defaultTest='all_suite')