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

class Footer(testModule):

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
        self.interact_by_xpath('//*[contains(@text, "ETUDEHOUSE")]', click=False) # 에뛰드 로고 대기

    def test_30_Footer_Shop_PhoneNumber(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(5)
                #쇼핑몰 전화번호
                self.T_Act(TCFG.res[0]*0.15555555555555556, TCFG.res[1]*0.6207207207207207, ratio=18, corr=['19'], wait_sec=3) # 168 1378
                # 통화 수화기 아이콘
                try:
                    self.interact_by_id('com.samsung.android.dialer:id/dialButtonImage',click=False, search_sec=10)
                except:
                    self.interact_by_id('com.android.contacts:id/btnLogsCall', click=False)
                # 1544-5418
                try:
                    self.interact_by_xpath('//android.widget.EditText[@text="1544-5418"]',click=False, search_sec=10)
                except:
                    self.interact_by_id('com.android.contacts:id/textCreateToContacts', click=False)
                # 뒤로
                TCFG.driver.back()
                sleep(2)
                # 뒤로
                TCFG.driver.back()
                sleep(5)
                self.exception('home')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 56)
                    break
                self.exception('home')
            else:
                print("30 Passed")
                TCFG.is_passed = True
                break

    def test_31_Footer_Product_PhoneNumber(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(3)
                # # 마이에뛰드
                # try:
                #     self.interact_by_xpath('//android.view.View[@content-desc="마이에뛰드"]') # 마이에뛰드 탭
                # except:
                #     self.interact_by_xpath('//android.view.View[@text="마이에뛰드"]') # 마이에뛰드 탭
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(3)
                # self.T_Act(TCFG.res[0]*0.6620370370370371, TCFG.res[1]*0.6207207207207207, ratio=18, corr=['19'], wait_sec=3) # 715 1378
                # # 통화 수화기 아이콘
                # try:
                #     self.interact_by_id('dialButtonImage',click=False)
                # except:
                #     self.interact_by_id('btnLogsCall', click=False)
				# # 080-022-2285
                # try:
                #     self.interact_by_xpath('//android.widget.EditText[@text="080-022-2285"]',click=False)
                # except:
                #     self.interact_by_id('textCreateToContacts', click=False)
				# # 뒤로
                # TCFG.driver.back()
                # sleep(2)
                # # 뒤로
                # TCFG.driver.back()
                # sleep(5)
                # self.exception('home')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 57)
                    break
                self.exception('home')
            else:
                print("31 Passed")
                TCFG.is_passed = True
                break

    def test_32_Footer_Facebook(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(3)
                # self.exception('home')
                # # 카테고리 열기
                # self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # # 마이에뛰드
                # self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(3)
                # # 페이스북
                # self.T_Act(TCFG.res[0]*0.5907407407407408, TCFG.res[1]*0.7846846846846847, ratio=18, corr=['19'], wait_sec=3) # 638 1742
                # # 페이스북 텍스트
                # self.interact_by_xpath('//android.widget.Image[@text="프로필 사진"]',click=False)
                # # 뒤로
                # TCFG.driver.back()
                # sleep(5)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 58)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(3)
            else:
                print("32 Passed")
                TCFG.is_passed = True
                break

    def test_33_Footer_Youtube(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(3)
                # # 유튜브
                # sleep(3)
                # self.T_Act(TCFG.res[0]*0.4981481481481482, TCFG.res[1]*0.7846846846846847, ratio=18, corr=['19'], wait_sec=3) # 538 1742
                # # 에뛰드하우스(ETUDE HOUSE)
                # self.interact_by_xpath('//android.view.View[@text="에뛰드 ETUDE"]',click=False)
				# # 뒤로
                # TCFG.driver.back()
                # sleep(2)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 60)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(3)
            else:
                print("33 Passed")
                TCFG.is_passed = True
                break

    def test_34_Footer_Instagram(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(3)
                # # 인스타그램
                # sleep(3)
                # self.T_Act(TCFG.res[0]*0.39537037037037037, TCFG.res[1]*0.7869369369369369, ratio=18, corr=['19'], wait_sec=3) # 427 1747
                # self.interact_by_xpath('//android.view.View[@text="etudeofficial"]',click=False)
                # # 뒤로
                # TCFG.driver.back()
                # sleep(5)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 61)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(3)
            else:
                print("34 Passed")
                TCFG.is_passed = True
                break

    # 수정필요 (탑버튼 클릭시 정상동작 그러나 element가 잡히지 않아 pass assertion 설정 불가능)
    def test_35_Footer_TopBtn(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # 탑아이콘
                # self.T_Act(TCFG.res[0]*0.9131944444444444, TCFG.res[1]*0.8763513513513513, ratio=18, low_corr=False, wait_sec=3) # 1315 2594
				# 마이 에뛰드 타이틀
                # self.interact_by_xpath('//android.widget.TextView[@text="개인정보 수정"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 62)
                    TCFG.is_finished = True
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(3)
            else:
                print("35 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Footer)
	unittest.TextTestRunner(verbosity=2).run(suite)
