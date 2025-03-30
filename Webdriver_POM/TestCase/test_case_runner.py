# -*- coding:utf-8 -*-

import unittest

from xiaomi_Test import  XiaoMiTest

def suite1():
	suite1 = unittest.TestSuite()
	suite1.addTest(XiaoMiTest('test_login'))
	return suite1



if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(suite1())
