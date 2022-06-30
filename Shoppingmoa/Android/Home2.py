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

class Home2(testModule):

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

    # def test_40_Coupon_Benefits(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             # 쿠폰/혜택 탭 진입
    #             self.interact_by_xpath('//android.view.View[@content-desc="쿠폰/혜택"]')
	# 			# 내쿠폰 탭
    #             self.interact_by_xpath('//android.widget.Button[@text="내 쿠폰"]',click=False)
    #         except:
    #             if loop_count == (TCFG.check_loop_count-1):
    #                 print("Error!")
    #                 self.assertEqual(0, 41)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("41 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # # 수정필요 (element 안잡힘)
    # def test_41_Coupon_MyBenefits(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             # 쿠폰/혜택 탭 진입
    #             self.interact_by_xpath('//android.widget.Button[@text="나만의 혜택"]')
	# 			# 내쿠폰 탭 (element 안잡힘)
    #             # self.interact_by_xpath('//android.view.View[@text="회원 혜택 알아보기"]',click=False)
    #         except:
    #             if loop_count == (TCFG.check_loop_count-1):
    #                 print("Error!")
    #                 self.assertEqual(0, 42)
    #                 break
    #             self.exception('home')
    #             # 쿠폰/혜택 탭 진입
    #             self.interact_by_xpath('//android.view.View[@text="쿠폰/혜택"]')
	# 			# 내쿠폰 탭
    #             self.interact_by_xpath('//android.widget.Button[@text="내 쿠폰"]')
    #         else:
    #             print("42 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # # 수정필요 (element 안잡힘)
    # def test_42_Coupon_MemberBenefits(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             sleep(2)
    #             # # 회원 혜택 알아보기 (element 안잡힘)
    #             # self.interact_by_xpath('//android.view.View[@text="회원 혜택 알아보기"]')
    #             # # 핑크 멤버쉽 확인
    #             # self.interact_by_xpath('//android.view.View[@text="Pink Membership"]')
    #             # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
    #         except:
    #             if loop_count == (TCFG.check_loop_count-1):
    #                 print("Error!")
    #                 self.assertEqual(0, 43)
    #                 break
    #             self.exception('home')
    #             # 쿠폰/혜택 탭 진입
    #             self.interact_by_xpath('//android.view.View[@text="쿠폰/혜택"]')
	# 			# 내쿠폰 탭
    #             self.interact_by_xpath('//android.widget.Button[@text="내 쿠폰"]')
    #             # 쿠폰/혜택 탭 진입
    #             self.interact_by_xpath('//android.widget.Button[@text="나만의 혜택"]')
	# 			# 내쿠폰 탭
    #             self.interact_by_xpath('//android.view.View[@text="회원 혜택 알아보기"]',click=False)
    #         else:
    #             print("43 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_43_ColorFactory(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             if TCFG.res[1] < 1500:
    #                 self.T_Swipe(x1=TCFG.res[0]*0.5, y1=TCFG.res[1]*0.85, x2=TCFG.res[0]*0.5, y2=TCFG.res[1]*0.6, ratio=16, low_corr=False)
    #             # 회원 혜택 알아보기
    #             self.interact_by_xpath('//android.view.View[@content-desc="컬러팩토리"]')
    #             # 핑크 멤버쉽 확인
    #             self.interact_by_xpath('//android.view.View[@content-desc="컬러 팩토리 안내"]/android.widget.TextView',click=False)
    #             # 뒤로
    #             TCFG.driver.back()
    #             sleep(2)
    #             self.interact_by_xpath('//android.view.View[@content-desc="컬러팩토리"]',click=False)
    #         except:
    #             if loop_count == (TCFG.check_loop_count-1):
    #                 print("Error!")
    #                 self.assertEqual(0, 44)
    #                 break
    #             self.exception('home')
    #
    #         else:
    #             print("44 Passed")
    #             TCFG.is_passed = True
    #             break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Home2)
	unittest.TextTestRunner(verbosity=2).run(suite)
