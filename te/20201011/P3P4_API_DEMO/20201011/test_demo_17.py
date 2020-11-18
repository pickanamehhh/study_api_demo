#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: test_demo_15.py
# @time: 2020/10/11 4:03 下午
#测试执行结果调试
import unittest
import os
import HTMLTestReportCN

case_path = os.path.join(os.path.dirname(__file__),'test_suite')

discover = unittest.defaultTestLoader.discover(start_dir=case_path,
                                               pattern='test_demo*.py',
                                               top_level_dir=case_path)
all_suite = unittest.TestSuite()
all_suite.addTest( discover )

report_path = os.path.join(os.path.dirname(__file__),'report/')
report_dir = HTMLTestReportCN.ReportDirectory(report_path) #创建一个测试报告路径对象
report_dir.create_dir('API_TEST') #调用创建目录的方法
report_html_path = HTMLTestReportCN.GlobalMsg.get_value('report_path') #获取测试报告文件的路径
report_html_file = open( report_html_path,'wb' )
html_runner = HTMLTestReportCN.HTMLTestRunner(stream=report_html_file,
                                              title='接口测试报告',
                                              description='实战使用',
                                              tester='P3P4')
html_runner.run(all_suite)

