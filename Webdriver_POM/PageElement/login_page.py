# -*- coding:utf-8 -*-

from BasePage.BaseDriver import BaseDriver
from PageLoctors.login_page_loc import LoginPageLoc

class LoginPage(BaseDriver):


	def __init__(self,driver):
		BaseDriver.__init__(self,driver)

	def input_username(self, username):
		print self.get_element(*LoginPageLoc.user)
		self.get_element(*LoginPageLoc.user).send_keys(username)

	def input_password(self, password):
		self.get_element(*LoginPageLoc.password).send_keys(password)

	def click_login_button(self):
		self.get_element(*LoginPageLoc.loginbut).click()


