# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import requests
import json
from flask import Flask, request, jsonify
import os 

app = Flask(__name__)
port = int(os.environ.get('PORT', 33507))
print(port)



class Test1(unittest.TestCase):
	@app.route('/', methods=['POST'])
	def main1():
		unittest.main()
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.base_url = "https://www.katalon.com/"
		self.verificationErrors = []
		self.accept_next_alert = True
	
	def test_1(self):
		driver = self.driver
		driver.get("https://www.cleartrip.com/")
		driver.find_element_by_id("FromTag").clear()
		driver.find_element_by_id("FromTag").send_keys("Delhi")
		driver.find_element_by_id("ToTag").clear()
		driver.find_element_by_id("ToTag").send_keys("Lucknow")
		driver.find_element_by_id("DepartDate").clear()
		driver.find_element_by_id("DepartDate").send_keys("13/05/2018")
		driver.find_element_by_id("Adults").click()
		Select(driver.find_element_by_id("Adults")).select_by_visible_text("3")
		driver.find_element_by_id("Childrens").click()
		driver.find_element_by_xpath("//section[@id='PaxBlock']/div[2]/dl/dd/small").click()
		driver.find_element_by_id("SearchBtn").click()

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True
	
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True
	
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True
	
	def tearDown(self):
		#self.driver.quit()
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	app.run(port=port, host="0.0.0.0")	 