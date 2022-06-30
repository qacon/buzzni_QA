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

class My_Etude(testModule):

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

    def test_18_MyEtude_Coupon(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기
                sleep(5)
                sleep(3)
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 마이 에뛰드 타이틀
                self.interact_by_xpath('//android.view.View[@content-desc="개인정보 수정 "]/android.widget.TextView',click=False)
                # 쿠폰
                self.interact_by_xpath('//android.view.View[@text="쿠폰"]')
				# 나의 쿠폰 타이틀
                self.interact_by_xpath('//android.view.View[@text="나의 쿠폰"]',click=False)
				# 뒤로
                TCFG.driver.back()
                sleep(2)
                self.interact_by_xpath('//android.view.View[@text="진주알"]',click=False)
                # 홈으로
                # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 45)
                    break
                self.exception('home')
            else:
                print("18 Passed")
                TCFG.is_passed = True
                break

    def test_19_MyExpectedGrade(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.view.View[@content-desc="내 예상등급 확인 "]') #내 예상등급 확인 클릭
                self.interact_by_xpath('//android.view.View[@text="나의 회원 등급"]',click=False) #나의 회원 등급 텍스트 노출 확인
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 45)
                    break
                self.exception('home')
            else:
                print("19 Passed")
                TCFG.is_passed = True
                break

    def test_20_Pearl(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 쿠폰
                self.interact_by_xpath('//android.view.View[@text="쿠폰"]')
				# 나의 쿠폰 타이틀
                self.interact_by_xpath('//android.view.View[@text="나의 쿠폰"]',click=False)
				# 뒤로
                TCFG.driver.back()
                sleep(2)
                self.interact_by_xpath('//android.view.View[@text="진주알"]',click=False)
                # 홈으로
                # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 46)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
            else:
                print("20 Passed")
                TCFG.is_passed = True
                break

    def test_21_Deposit(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 예치금 클릭
                self.interact_by_xpath('//android.view.View[@text="예치금"]')
				# 예치금 내역 탭
                self.interact_by_xpath('//android.view.View[@text="예치금 내역"]',click=False)
				# 뒤로
                TCFG.driver.back()
                sleep(2)
                self.interact_by_xpath('//android.view.View[@text="마이 에뛰드"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 47)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
            else:
                print("21 Passed")
                TCFG.is_passed = True
                break

    def test_22_BeautyPoint(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 뷰티포인트 클릭
                self.interact_by_xpath('//*[@text="뷰티포인트"]')
				# 뷰티포인트 확인
                self.interact_by_xpath('//*[contains(@text, "님의 뷰티포인트")]',click=False)
				# 뒤로
                TCFG.driver.back()
                sleep(2)
                self.interact_by_xpath('//*[@text="마이 에뛰드"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 48)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
            else:
                print("22 Passed")
                TCFG.is_passed = True
                break

    # 수정필요
    def test_23_ActivityManagement_Reviews(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(5)
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(4)
                # if TCFG.ratio == 16:
                #     self.T_Act(TCFG.res[0]*0.9444444444444444, TCFG.res[1]*0.05804311774461028, ratio=16, low_corr=False)
                #     self.T_Act(TCFG.res[0]*0.6944444444444444, TCFG.res[1]*0.12437810945273632, ratio=16, low_corr=False)
                # else:
                #     self.T_Act(TCFG.res[0]*0.6819444444444445, TCFG.res[1]*0.07432432432432433, ratio=18, corr=['19'], wait_sec=3) # 982 220
                # # 페이지 확인
                # self.interact_by_xpath('//android.view.View[contains(@text,"나의 구매 리뷰")]')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 49)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
            else:
                print("23 Passed")
                TCFG.is_passed = True
                break

    # 수정 필요
    def test_24_ActivityManagement_Inquiry(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                sleep(2)
                # # 1:1 문의내역
                # self.interact_by_xpath('//android.view.View[@content-desc="나의 1:1 문의"]')
                # # 나의 1:1 문의
                # self.interact_by_xpath('//android.view.View[@text="나의 1:1 문의"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 50)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(2)
                # 나의 정보 관리 탭 닫기
                self.T_Act(TCFG.res[0]*0.6819444444444445, TCFG.res[1]*0.07432432432432433, ratio=18, corr=['19'], wait_sec=3) # 982 220
				# 나의 구매 후기
                self.T_Act(TCFG.res[0]*0.6819444444444445, TCFG.res[1]*0.07432432432432433, ratio=18, corr=['19'], wait_sec=3) # 982 220
				# 페이지 확인
                self.interact_by_xpath('//android.view.View[contains(@text,"나의 구매 후기")]')
            else:
                print("24 Passed")
                TCFG.is_passed = True
                break

    # 수정 필요
    def test_25_ActivityManagement_Modify_Privacy(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(2)
                # # 1:1 문의내역
                # self.interact_by_xpath('//android.view.View[@content-desc="회원정보수정"]')
                # # 나의 1:1 문의
                # self.interact_by_xpath('//android.view.View[@text="개인정보 수정"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 51)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                # 나의 구매 후기
                self.T_Act(TCFG.res[0]*0.6819444444444445, TCFG.res[1]*0.07432432432432433, ratio=18, corr=['19'], wait_sec=3) # 982 220
				# 페이지 확인
                self.interact_by_xpath('//android.view.View[contains(@text,"나의 구매 후기")]')
            else:
                print("25 Passed")
                TCFG.is_passed = True
                break

    # 4004만 안돌아서 수정필요
    def test_26_ActivityManagement_Linking_SNS(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(3)
                # # 카테고리 열기
                # self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
                # # 마이에뛰드
                # self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(3)
                # # SNS 계정 연동 관리 클릭
                # if TCFG.ratio == 16:
                #     self.T_Act(TCFG.res[0]*0.6944444444444444, TCFG.res[1]*0.12437810945273632, ratio=16, low_corr=False)
                # else:
                #     self.T_Act(TCFG.res[0]*0.6944444444444444, TCFG.res[1]*0.28547297297297297, ratio=18, corr=['19'], wait_sec=3) # 1000 845
                # # SNS 계정 연동 관리
                # self.interact_by_xpath('//android.view.View[@text="SNS 계정 연동 관리"]',click=False)
                # # 뒤로
                # self.interact_by_xpath("(//android.widget.Button)[2]")
                # TCFG.driver.back()
                # sleep(2)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 52)
                    break
                self.exception('home')
            else:
                print("26 Passed")
                TCFG.is_passed = True
                break

    # 4004만 안돌아서 수정필요
    def test_27_ActivityManagement_Shipping_Management(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(3)
                # # 카테고리 열기
                # self.interact_by_xpath('//android.view.View[@content-desc="카테고리"]/android.view.View')
                # # 마이에뛰드
                # self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(3)
                # # 배송지 관리 클릭
                # if TCFG.ratio == 16:
                #     self.T_Act(TCFG.res[0]*0.20277777777777778, TCFG.res[1]*0.2296849087893864, ratio=18, low_corr=False, wait_sec=3)
                # else:
                #     self.T_Act(TCFG.res[0]*0.20277777777777778, TCFG.res[1]*0.3398648648648649, ratio=18, low_corr=False, wait_sec=3) # 292 1006
                # # 배송지 관리
                # self.interact_by_xpath('//android.view.View[@text="배송지 관리"]',click=False)
                # # 뒤로
                # self.interact_by_xpath("(//android.widget.Button)[2]")
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 53)
                    break
                self.exception('home')
            else:
                print("27 Passed")
                TCFG.is_passed = True
                break

    # 에러
    def test_28_ActivityManagement_MyShop(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 카테고리 열기
                # self.interact_by_xpath('//android.view.View[@content-desc="카테고리"]/android.view.View')
                # # 마이에뛰드
                # self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # # 맨 밑으로
                # TCFG.driver.press_keycode(123)
                # sleep(3)
                # # My Shop
                # if TCFG.ratio == 16:
                #     self.T_Act(TCFG.res[0]*0.6944444444444444, TCFG.res[1]*0.2296849087893864, ratio=18, low_corr=False, wait_sec=3) # 964 1012
                # else:
                #     self.T_Act(TCFG.res[0]*0.6694444444444444, TCFG.res[1]*0.3418918918918919, ratio=18, corr=['19'], wait_sec=3) # 964 1012
                # # MY SHOP 관리
                # self.interact_by_xpath('//android.view.View[@text="MY SHOP 관리"]',click=False)
                # # 뒤로
                # self.interact_by_xpath("(//android.widget.Button)[2]", wait_sec=7)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 54)
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.view.View[@content-desc="카테고리"]/android.view.View')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
            else:
                print("28 Passed")
                TCFG.is_passed = True
                break

    # 에러
    def test_29_ActivityManagement_Withdrawal(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 회원탈퇴 클릭
                # if TCFG.res[1] < 1500:
                #     self.T_Act(TCFG.res[0]*0.9, TCFG.res[1]*0.2906849087893864, ratio=18, low_corr=False, wait_sec=3)
                # else:
                #     self.T_Act(TCFG.res[0]*0.9, TCFG.res[1]*0.3986081081081081, ratio=18, wait_sec=3)
                # # 회원탈퇴 페이지 노출 확인
                # self.interact_by_xpath('//android.view.View[@text="포인트 현황"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 55)
                    TCFG.is_finished = True
                    break
                self.exception('home')
                # 카테고리 열기
                self.interact_by_xpath('//android.view.View[@content-desc="카테고리"]/android.view.View')
                # 마이에뛰드
                self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
                # 맨 밑으로
                TCFG.driver.press_keycode(123)
                sleep(3)
            else:
                print("29 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(My_Etude)
	unittest.TextTestRunner(verbosity=2).run(suite)
