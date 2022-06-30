# -*- coding: utf-8 -*-
import sys
import io
import unittest
import os
import time, datetime
import random
import numpy as np
from Autoscroll_And import *
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

class Search(testModule):

    def initialize(self):
        TCFG.is_initialized = True
        argv = sys.argv[1]
        initialize_bp(self, argv)
        reso = TCFG.driver.get_window_size()
        TCFG.res.append(reso["width"])
        TCFG.res.append(reso["height"])

    def setUp(self):
        if not TCFG.is_passed and TCFG.is_initialized:
            self.exception('home')
        if not TCFG.is_initialized:
            self.initialize()
            TCFG.is_finished = False
        TCFG.is_passed = False

    def exception(self, menu):
        TCFG.driver.close_app()
        sleep(2)
        TCFG.driver.launch_app()
        sleep(2)
        self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기

    def test_36_Search_Icon(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False, wait_sec=7) # 에뛰드 로고 대기
                self.interact_by_xpath('//android.widget.EditText', type='presence') # 검색어 입력
                self.interact_by_xpath('//*[contains(@text, "#")]', type='presence', click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 63)
                    break
                self.exception('home')
            else:
                print("36 Passed")
                TCFG.is_passed = True
                break

    def test_37_Search_Lotion(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                TCFG.driver.close_app()
                sleep(2)
                TCFG.driver.launch_app()
                sleep(2)
                # 검색아이콘 클릭
                self.interact_by_xpath('//android.widget.Button[contains(@text,"검색")]')

                # # 만약 입력 창 없으면 검색 창 한번 더 누르기
                # try:
                #     self.interact_by_xpath('//android.widget.Button[contains(@text,"검색")]', search_sec=7)
                # except:
                #     pass
                # 해시태그 클릭
                self.interact_by_xpath('//*[contains(@text, "#")]')
                # 로션 입력
                self.interact_by_xpath('//android.widget.EditText[1]', send_keys_msg="로션", click=False)
                # 검색 클릭
                self.interact_by_xpath('(//android.widget.Button)[2]')
                # 상품리스트
                self.interact_by_xpath('//android.widget.Button[@text="상품"]',click=False)
                # 홈버튼
                self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
                self.interact_by_xpath('//android.view.View[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 64)
                    break
                self.exception('home')
                # 상단 검색 텍스트
                self.interact_by_xpath('//android.view.View[@text="검색"]')
            else:
                print("37 Passed")
                TCFG.is_passed = True
                break

    def test_38_Search_PopularItem(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.EditText', type='presence') # 검색어 입력
                self.interact_by_xpath('//*[@text="#섀도우"]') # 인기 검색어 하나 탭
                self.interact_by_xpath('//android.view.View[contains(@text,"개의 상품")]',click=False, wait_sec=5)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 65)
                    TCFG.is_finished = True
                    break
                self.exception('home')
            else:
                print("38 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Search)
	unittest.TextTestRunner(verbosity=2).run(suite)
