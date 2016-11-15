# -*- coding:utf-8 -*-

import unittest

from selenium import webdriver
from PageElement.login_page import  LoginPage

class XiaoMiTest(unittest.TestCase):
	

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("url....")
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)

		self.username = "*********"
		self.password = "*********"
	

	def test_login(self):
		loginPage = LoginPage(self.driver)
		loginPage.input_username(self.username)
		loginPage.input_password(self.password)
		loginPage.click_login_button()



	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
    unittest.main()