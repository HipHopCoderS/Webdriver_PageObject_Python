# -*- coding:utf-8 -*-
__author__ = 'SunXinLei'


# webdriver page object 基础公用方法

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver(object):

	def __init__(self, driver):
		self.driver = driver

	# 打开指定url
	def open_url(self, url, pagetitle):
		self.driver.get(self.url)
		self.driver.maximize_window()
		print self.driver.title
		assert self.pagetitle in self.driver.title

	# 根据传入坐标,返回元素
	def get_element(self, *loc):
		element = self.driver.find_element(*loc)
		return element

	# 根据传入坐标,返回所有匹配的元素,返回list
	def get_elements(self, *loc):
		elementlist  = self.driver.find_elements(*loc)
		return elementlist
			

	# webdriver 调用selenium 的方法,判断元素是否存
	def is_element_exist(self, *loc):
		try:
			self.driver.find_element(*loc)
			self.driver.find_elements(*loc)
			return  True
		except:
			return False

	# webdriver 调用selenium 的方法,判断元素是否存
	def is_element_display(self, *loc):
		try:
			if self.driver.find_element(*loc).is_displayed() or self.driver.find_elements(*loc).is_displayed():
				return  True
			else:
				return False
		except:
			return False

	# 判断元素是否显示
	def wait_element_display(self, time, *loc):
		try:
			WebDriverWait(self.driver, time).until(
				EC.presence_of_element_located(*loc))
			return  True
		except:
			return  False

	# 判断元素是否可视
	def wait_element_visible(self, time, *loc):
		try:
			WebDriverWait(self.driver, time).until(
				EC.visibility_of_element_located(*loc))
			return  True
		except:
			return False

	# 执行js 脚本
	def exec_js(self, script):
		self.driver.execute_script(script)

	# 刷新网页
	def refresh_page(self):
		self.driver.refresh()



