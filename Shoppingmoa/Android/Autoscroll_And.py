# -*- coding: utf-8 -*-
from time import sleep
from Bootstrap import TEST_CONFIG as TCFG
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Bootstrap import TEST_CONFIG as TCFG

def scroll_xpath(self, xpath, loc, y1, y2, wait_sec=2, click=True, direction=0, ms=None):
	for loop_count in range(direction, 31):
		try:
			element = TCFG.driver.find_element_by_xpath(xpath)
			if element.location["y"] < loc:
				if click:
					element.click()
					sleep(wait_sec)
				else:
					sleep(wait_sec)
			else:
				TCFG.driver.find_element_by_xpath(fail)
		except:
			if loop_count < 16:
				TCFG.driver.swipe(TCFG.res[0]*0.5,y1,TCFG.res[0]*0.5,y2,ms)
				sleep(wait_sec)
			elif loop_count > 15 and loop_count < 30:
				TCFG.driver.swipe(TCFG.res[0]*0.5,y2,TCFG.res[0]*0.5,y1,ms)
				sleep(wait_sec)
			elif loop_count == 30:
				self.assertEqual(1, 30)
		else:
			break

def scroll_id(self, id, loc, y1, y2, wait_sec=2, click=True, direction=0, ms=None):
	for loop_count in range(direction, 31):
		try:
			element = TCFG.driver.find_element_by_id(id)
			if element.location["y"] < loc:
				if click:
					element.click()
					sleep(wait_sec)
				else:
					sleep(wait_sec)
			else:
				TCFG.driver.find_element_by_id(fail)
		except:
			if loop_count < 16:
				TCFG.driver.swipe(TCFG.res[0]*0.5,y1,TCFG.res[0]*0.5,y2,ms)
				sleep(wait_sec)
			elif loop_count > 15 and loop_count < 30:
				TCFG.driver.swipe(TCFG.res[0]*0.5,y2,TCFG.res[0]*0.5,y1,ms)
				sleep(wait_sec)
			elif loop_count == 30:
				self.assertEqual(1, 30)
		else:
			break

'''
def scroll_find(self, driver, id):
	a = 0
	while 1:
		try:
			el = driver.find_element_by_id(id)
			driver.execute_script('mobile: scroll', {"element" : el, "toVisible": True})
			sleep(1)
		except:
			a += 1
			if a == 10:
				self.assertEqual(1,30)
				break
			pass
		else:
			sleep(2)
			break

def scroll_find2(self, driver, str, adr, loc, y1, y2):
	a = 0
	while 1:
		try:
			el = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((str, adr)))
			if (el.location["y"] < loc):
				sleep(1)
				break
		except:
			if (a < 25 and a > 15) :
				driver.swipe(150,y2,150,y1,50)
			else:
				driver.swipe(150,y1,150,y2,50)
			sleep(2)
			a += 1
			if a == 30:
				self.assertEqual(1, 1000)
				break
			else:
				pass


def scroll_find_xpath(self, driver, xpath):
	a = 0
	while 1:
		try:
			el = driver.find_element_by_xpath(xpath)
			driver.execute_script('mobile: scroll', {"element" : el, "toVisible": True})
			sleep(1)
		except:
			a += 1
			if a == 10:
				self.assertEqual(1,30)
				break
			pass
		else:
			sleep(2)
			break

def scroll_click(self, driver, id):
    a = 0
    while 1:
        try:
            el = driver.find_element_by_id(id)
            driver.execute_script('mobile: scroll', {"element" : el, "toVisible": True})
            sleep(1)
        except:
        	a += 1
        	if a == 10:
        		self.assertEqual(1,30)
        		break
        	pass
        else:
        	el.click()
        	sleep(2)
        	break

def scroll_click2(self, driver, str, adr, loc, y1, y2):
	a = 0
	while 1:
		try:
			el = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((str, adr)))
			if (el.location["y"] < loc):
				el.click()
				sleep(2)
				break
			else:
				self.assertEqual(1,3)
				pass
		except:
			if (a < 25 and a > 15) :
				driver.swipe(150,y2,150,y1,50)
			else:
				driver.swipe(150,y1,150,y2,50)
			sleep(4)
			a += 1
			if a == 30:
				self.assertEqual(1, 1000)
				break
			else:
				pass

def scroll_click_xpath(self, driver, xpath):
	a = 0
	while 1:
		try:
			el = driver.find_element_by_xpath(xpath)
			driver.execute_script('mobile: scroll', {"element" : el, "toVisible": True})
			sleep(1)
		except:
			a += 1
			if a == 10:
				self.assertEqual(1,30)
				break
			pass
		else:
			el.click()
			sleep(2)
			break

def scroll_test(self, driver, xpath):
	a = 0
	while 1:
		try:
			element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
			sleep(1)
		except:
			if (a % 10) == 0:
				driver.press_keycode(122)
			else:
				driver.swipe(700,2000,700,1000)
			sleep(1)
			a += 1
			if a == 30:
				break
			pass
		else:
			sleep(1)
			break

def scroll_xpath_LR(self, driver, y_xpath, xpath, wait_sec=3, loc=1100, x1=300, x2=600, click=True, direction=0, ms=None):
	y_point = driver.find_element_by_xpath(y_xpath)
	y_point = y_point.location["y"]
	for loop_count in range(direction, 31):
		try:
			element = driver.find_element_by_xpath(xpath)
			if element.location["x"] < loc:
				if click:
					element.click()
					sleep(wait_sec)
				else:
					sleep(wait_sec)
			else:
				driver.find_element_by_xpath(fail)
		except:
			if loop_count < 16:
				driver.swipe(x2,y_point,x1,y_point,ms)
				sleep(wait_sec)
			elif loop_count > 15 and loop_count < 30:
				driver.swipe(x1,y_point,x2,y_point,ms)
				sleep(wait_sec)
			elif loop_count == 30:
				self.assertEqual(1, 30)
		else:
			break
'''
