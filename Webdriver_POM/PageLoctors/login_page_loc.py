# -*- coding:utf-8 -*-


from selenium.webdriver.common.by import By

class LoginPageLoc(object):

	user = (By.ID, "username")
	password = (By.ID, "pwd")
	loginbut = (By.ID, "login-button")
