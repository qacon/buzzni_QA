#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Bootstrap import TEST_CONFIG as TCFG

class testModule(unittest.TestCase):

    def fs_id(self, name):
        return '%s' % (name)

    def presence(self, name):
        return EC.presence_of_element_located((By.ID, self.fs_id(name)))

    def clickable(self, name):
        return EC.element_to_be_clickable((By.ID, self.fs_id(name)))

    def visible(self, name):
        return EC.visibility_of_element_located((By.ID, self.fs_id(name)))

    def invisible(self, name):
        return EC.invisibility_of_element_located((By.ID, self.fs_id(name)))

    def interact_by_id(self, name, type='click', search_sec=30, wait_sec=2, click=True, send_keys_msg=None):
        if type == 'click':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.clickable(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.clickable(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.clickable(name)).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif type == 'presence':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.presence(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.presence(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.presence(name)).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif type == 'visible':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.visible(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.visible(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.visible(name)).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif type == 'invisible':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.invisible(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.invisible(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.invisible(name)).send_keys(send_keys_msg)
            sleep(wait_sec)

    def presence_xpath(self, name):
        return EC.presence_of_element_located((By.XPATH, name))

    def clickable_xpath(self, name):
        return EC.element_to_be_clickable((By.XPATH, name))

    def visible_xpath(self, name):
        return EC.visibility_of_element_located((By.XPATH, name))

    def invisble_xpath(self, name):
        return EC.invisibility_of_element_located((By.XPATH, name))

    def interact_by_xpath(self, name, type='click', search_sec=30, wait_sec=2, click=True, send_keys_msg=None):
        if type == 'click':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.clickable_xpath(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.clickable_xpath(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.clickable_xpath(name)).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif type == 'presence':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.presence_xpath(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.presence_xpath(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.presence_xpath(name)).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif type == 'visible':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.visible_xpath(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.visible_xpath(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.visible_xpath(name)).send_keys(send_keys_msg)
            sleep(wait_sec)
        elif type == 'invisible':
            if send_keys_msg == None:
                if click == True:
                    WebDriverWait(TCFG.driver, search_sec).until(self.invisble_xpath(name)).click()
                elif click == False:
                    WebDriverWait(TCFG.driver, search_sec).until(self.invisble_xpath(name))
            else:
                WebDriverWait(TCFG.driver, search_sec).until(self.invisble_xpath(name)).send_keys(send_keys_msg)
            sleep(wait_sec)

    def get_attri(self, name, att, strategy, ec='presence', search_sec=10, wait_sec=2):
        if ec == 'presence':
            a = WebDriverWait(TCFG.driver, search_sec).until(EC.presence_of_element_located((strategy, name)))
        elif ec == 'click':
            a = WebDriverWait(TCFG.driver, search_sec).until(EC.element_to_be_clickable((strategy, name)))
        sleep(wait_sec)
        return a.get_attribute(att)

    def get_loc(self, name, strategy, ec='presence', search_sec=10, wait_sec=2):
        if ec == 'presence':
            el = WebDriverWait(TCFG.driver, search_sec).until(EC.presence_of_element_located((strategy, name)))
        elif ec == 'click':
            el = WebDriverWait(TCFG.driver, search_sec).until(EC.element_to_be_clickable((strategy, name)))
        sleep(wait_sec)
        return el.location["x"], el.location["y"]

    def T_Act(self, x, y, ratio, corr=None, low_corr=True, count=1, wait_sec=2):
        if corr != None:
            if ratio == 19:
                if '18' in corr and TCFG.ratio == 18.5:
                    y = y * 0.9734749035
                if '16' in corr and TCFG.ratio == 16:
                    y = y * 1.0734749035
            elif ratio == 18:
                # galaxy s10
                if '19' in corr and TCFG.ratio == 19:
                    y = y * 1.1
                if '16' in corr and TCFG.ratio == 16:
                    y = y * 1.17
            elif ratio == 16:
                if '19' in corr and TCFG.ratio == 19:
                    dc
                if '18' in corr and TCFG.ratio == 18.5:
                    y = y * 0.85
        TouchAction(TCFG.driver).tap(None, x, y, count).perform()
        sleep(wait_sec)

    ###### logcat ######

    def extraction_log(self,sentence):
        cnt=0
        logs = self.driver.get_log('logcat')
        while True:
            sleep(0.5)
            if cnt == 200:
                 return None
            if sentence not in str(logs):
                logs = self.driver.get_log('logcat')
                cnt=cnt+1
            elif sentence in str(logs):
                print(sentence)
                return sentence
