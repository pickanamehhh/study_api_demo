#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_15.py
# @time: 2020/10/11 4:03 下午
#测试执行结果调试
import unittest
import os
import HTMLTestRunner

case_path = os.path.join(os.path.dirname(__file__),'test_suite')

discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_demo*.py',
                                               top_level_dir=case_path)
all_suite = unittest.TestSuite()
all_suite.addTest( discover )

# 初级报告 verbosity=2
unittest.main(defaultTest='all_suite',verbosity=2)

# TextTestRunner 报告 可以把报告保存到文件里面

# stream=None 表示测试结果在控制台显示
text_runner = unittest.TextTestRunner(stream=None,verbosity=2,descriptions=None)
text_runner.run( all_suite )

# 文本格式报告
report_file_path = os.path.join(os.path.dirname(__file__),'report','report.txt')
with open(report_file_path,'w',encoding='utf-8') as file:
    text_runner = unittest.TextTestRunner(stream=file, verbosity=2, descriptions='newdream')
    text_runner.run(all_suite)

# HTML格式报告
html_file_path = os.path.join(os.path.dirname(__file__),'report','report01.html')
html_file = open(html_file_path,'w+')
html_runner = HTMLTestRunner.HTMLTestRunner(stream=html_file,
                                            title='newdreamP3P4',
                                            description="测试实战")
html_runner.run(all_suite)

