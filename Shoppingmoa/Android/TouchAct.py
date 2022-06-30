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

class TouchAct(testModule):

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
        self.interact_by_id('main_banner_img', click=False, wait_sec=3)
        if menu == 'chennel':
            self.interact_by_id('btn_channel')
            sleep(5)

    def test_01_BP_11_Brand_Product_Detail(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_id('main_banner_img', click=False, wait_sec=3)
                scroll_id(self, 'tv_home_brand', loc=TCFG.res[1]*0.99, y1=TCFG.res[1]*0.9, y2=TCFG.res[1]*0.3) # 브랜드 탭
                # self.interact_by_id('brand_name') # 임의 브랜드 탭
                self.T_Act_18(TCFG.res[0]*0.9388888888888889, TCFG.res[1]*0.463671875) # ㅎ 탭
                scroll_xpath(self, '//*[contains(@text, "헤라")]', loc=TCFG.res[1]*0.99, y1=TCFG.res[1]*0.9, y2=TCFG.res[1]*0.4) # 헤라 탐색 후 탭
                self.interact_by_xpath('//android.view.View[contains(@text, " 원")]') # 상품 하나 탭
                self.interact_by_xpath('//android.widget.Image', click=False) # 상품 이미지 대기
                self.interact_by_id('sub_webview_back_home') # 뒤로 가기
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("1 Passed")
                TCFG.is_passed = True
                break

    def test_02_BP_49_Survey_Ranking(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                TCFG.driver.launch_app()
                sleep(5)
                self.interact_by_id('btn_community', wait_sec=7)
                self.T_Act_18(TCFG.res[0]*0.7527777777777778, TCFG.res[1]*0.6891891891891891, corr=True, wait_sec=5) # 랭킹 탭
                # self.T_Act_16(TCFG.res[0]*0.7527777777777778, TCFG.res[1]*0.80859375, corr=True, wait_sec=5) # 랭킹 탭
                self.interact_by_xpath('//android.view.View[@text="일별랭킹"]', click=False) # 랭킹 화면 노출 확인
                self.interact_by_id('sub_webview_back_home') # 뒤로가기
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(1, 2)
                    TCFG.is_finished = True
                    break
                self.exception('home')
            else:
                print("2 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TouchAct)
	unittest.TextTestRunner(verbosity=2).run(suite)
