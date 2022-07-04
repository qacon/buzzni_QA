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

class Purchase(testModule):

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

    # 수정필요
    def test_64_Payment_KCP(self):
        # currentTime0 = Matching.makeTS(self)
        # detectImagePath0 = "scutImage/payment.png"
        # currentTime1 = Matching.makeTS(self)
        # detectImagePath1 = "scutImage/next.png"
        # currentTime2 = Matching.makeTS(self)
        # detectImagePath2 = "scutImage/cancel.png"
        # currentTime3 = Matching.makeTS(self)
        # detectImagePath3 = "scutImage/check.png"
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 검색 아이콘 클릭
                # self.interact_by_xpath('//android.widget.EditText', type='presence')
                # self.interact_by_xpath('//android.view.View[@text="#섀도우"]')
                # # 마이뷰티툴 브러쉬 316 검색
                # self.interact_by_xpath('//android.widget.EditText',click=False,send_keys_msg="마이뷰티툴 브러쉬 316")
                # # 검색 아이콘 클릭
                # self.interact_by_xpath('(//android.widget.Button)[2]')
                # # 상품뜰때까지
                # self.interact_by_xpath('//android.view.View[contains(@text,"316 섀도우")]',click=False)
                # # 상품클릭
                # self.interact_by_xpath('//android.view.View[contains(@text,"316 섀도우")]')
                # # 상품상세
                # self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
                # # 구매하기
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
                # # 바로구매
                # self.interact_by_xpath('//android.widget.Button[@text="바로구매"]')

                # 배송지등록 #
                # # 이름
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[1]'))).send_keys("아모레")
                # # 휴대폰번호
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[2]'))).send_keys("01077778888")
                # # 주소지
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[3]'))).send_keys("서초대로51길 29")
                # # 찾기
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="찾기"]'))).click()
                # # 우편번호?
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[contains(@text,"06605")]'))).click()
                # # 키보드 내리기
                # driver.back()
                # sleep(2)
                # # 나머지 주소
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[3]'))).send_keys("헤라스빌딩 7층")
                # sleep(2)
                # # 배송요청 사항
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Spinner[contains(@text,"배송시 요청사항")]'))).click()
                # # 배송전 연락 바랍니다 선택
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckedTextView[contains(@text,"배송 전 연락")]'))).click()
                # # 키보드 내리기
                # driver.back()
                # sleep(2)

                # 결제하기 타이틀
                # self.interact_by_xpath('//android.view.View[@text="결제하기"]',click=False)


                ############################ 여기서 부터 결제하기 ############################
                # # 필수까지
                # scroll_find_xpath(self,driver,'//android.view.View[contains(@text,"(필수)")]')
                # # 이메일
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[2]'))).send_keys("amore@naver.com")
                # # # 신용카드 선택
                # # #scroll_click_xpath(self,driver,'//*[contains(@text,"신용카드")]')
                # # driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.7,TCFG.res[0]*0.5,TCFG.res[1]*0.4)
                # # sleep(3)
                # # driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime1)
                # # center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime1,detectImagePath1)
                # # driver.tap([center])
                # # sleep(5)
                # #
                # # driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.7,TCFG.res[0]*0.5,TCFG.res[1]*0.4)
                # # sleep(3)
                # #
                # #
                # #
                # # # 오픈시비
                # #
                # # # 카드선택
                # # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckedTextView[@text="신한카드"]'))).click()
                #
                # driver.press_keycode(123)
                # sleep(3)
                # # 전체동의
                # sleep(2)
                # TouchAction(driver).tap(None, 80, 910, 1).perform()
                # sleep(2)
                # # 결제하기
                # driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime0)
                # center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime0,detectImagePath0)
                # driver.tap([center])
                # sleep(3)
                #
                # # 전체동의
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="전체동의"]'))).click()
                # sleep(2)
                # # 다음
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="다음"]'))).click()
                # sleep(2)
                # # 다른결제 ARS결제
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[contains(@text,"다른결제 ARS결제")]'))).click()
                # sleep(2)
                # # 결제하기
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.view.View[@text="결제하기"])[2]'))).click()
                # sleep(2)
                # # 확인
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="확인"]'))).click()
                # sleep(2)
                # # 카드번호1
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[1]'))).send_keys("5211")
                # sleep(2)
                # # 카드번호2
                # TouchAction(driver).tap(None, 540, 550, 1).perform()
                # sleep(3)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[12]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[13]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[14]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[14]/android.widget.Image'))).click()
                # sleep(1)
                #
                # # 카드번호3
                # TouchAction(driver).tap(None, 680, 550, 1).perform()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[14]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[5]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[9]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[11]/android.widget.Image'))).click()
                # sleep(1)
                #
                # # 카드번호4
                # wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[4]'))).send_keys("2914")
                # sleep(5)
                # # cvc
                # TouchAction(driver).tap(None, 460, 670, 1).perform()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[8]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[6]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[14]/android.widget.Image'))).click()
                # sleep(1)
                # # 입력완료
                # TouchAction(driver).tap(None, 735, 1260, 1).perform()
                # sleep(3)
                # # 확인
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="확인"]'))).click()
                # sleep(5)
                #
                # # 일반결제비밀번호
                # TouchAction(driver).tap(None, 580, 670, 1).perform()
                # sleep(3)
                #
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[34]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[35]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[36]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[38]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[39]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[42]/android.widget.Image'))).click()
                # sleep(1)
                # wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.webkit.WebView[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[27]/android.widget.Image'))).click()
                # sleep(1)
                #
                # # 입력완료
                # TouchAction(driver).tap(None, 925, 1355, 1).perform()
                # sleep(3)
                #
                # # 확인
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="확인"]'))).click()
                # sleep(5)
                #
                # # 주문이 완료되었습니다 까지
                # wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"주문이 완료")]')))
                # # 배송/주문조회
                # scroll_click_xpath(self,driver,'//android.widget.Button[contains(@text,"배송/주문조회")]')
                # # 주문취소
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="주문취소"]'))).click()
                # sleep(5)
                # # 전체선택
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="전체 선택"]'))).click()
                # sleep(5)
                # # 다음
                # driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.9,TCFG.res[0]*0.5,TCFG.res[1]*0.1)
                # sleep(3)
                # driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime1)
                # center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime1,detectImagePath1)
                # driver.tap([center])
                # sleep(3)
                #
                # # 결제완료
                # wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="결제완료"]')))
                # # 취소신청
                # driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.9,TCFG.res[0]*0.5,TCFG.res[1]*0.1)
                # sleep(3)
                # driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime2)
                # center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime2,detectImagePath2)
                # driver.tap([center])
                # sleep(3)
                # # 확인
                # driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime3)
                # center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime3,detectImagePath3)
                # driver.tap([center])
                # sleep(3)
                # # 취소완료
                # wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="취소완료"]')))
                # 홈으로
                # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
                # self.T_Act(TCFG.res[0]*0.1527777777777778, TCFG.res[1]*0.062162162162162166, ratio=18, corr=['19'], wait_sec=3) # 220 184
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 74)
                    break
                self.exception('home')
            else:
                print("64 Passed")
                TCFG.is_passed = True
                break

    # 수정필요
    def test_65_Payment_Passbook(self):
        # currentTime0 = Matching.makeTS(self)
        # detectImagePath0 = "scutImage/Passbook.png"
        # currentTime1 = Matching.makeTS(self)
        # detectImagePath1 = "scutImage/next.png"
        # currentTime2 = Matching.makeTS(self)
        # detectImagePath2 = "scutImage/cancel.png"
        # currentTime3 = Matching.makeTS(self)
        # detectImagePath3 = "scutImage/check.png"
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 검색 아이콘 클릭
                # self.interact_by_xpath('//android.widget.EditText', type='presence')
                # self.interact_by_xpath('//android.view.View[@text="#섀도우"]')
                # # 매직프레스 검색
                # self.interact_by_xpath('//android.widget.EditText',click=False,send_keys_msg="매직프레스")
                # # 검색
                # self.interact_by_xpath('(//android.widget.Button)[2]')
                # # 상품이미지 노출확인 후 클릭
                # self.interact_by_xpath('//android.view.View[@text="매직프레스"]',click=False)
                # self.interact_by_xpath('//android.view.View[@text="매직프레스"]')
                # # 상품상세
                # self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
                # # 구매하기
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
                # # 상품 선택
                # self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]', type='presence')
                # self.interact_by_xpath('//android.view.View[contains(@text,"브이프렌치")]')
                # # 바로구매
                # self.interact_by_xpath('//android.widget.Button[@text="바로구매"]')
				# 배송지등록 #
				# # 이름
				# wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[1]'))).send_keys("아모레")
				# # 휴대폰번호
				# wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[2]'))).send_keys("01077778888")
				# # 주소지
				# wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[3]'))).send_keys("서초대로51길 29")
				# # 찾기
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="찾기"]'))).click()
				# # 우편번호?
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[contains(@text,"06605")]'))).click()
				# # 키보드 내리기
				# driver.back()
				# sleep(2)
				# # 나머지 주소
				# wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[3]'))).send_keys("헤라스빌딩 7층")
				# sleep(2)
				# # 배송요청 사항
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Spinner[contains(@text,"배송시 요청사항")]'))).click()
				# # 배송전 연락 바랍니다 선택
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckedTextView[contains(@text,"배송 전 연락")]'))).click()
				# # 키보드 내리기
				# driver.back()
				# sleep(2)

				# 결제하기 타이틀
                # self.interact_by_xpath('//android.view.View[@text="결제하기"]',click=False)


				############################ 여기서 부터 결제하기 ############################
				############################ 여기서 부터 결제하기 ############################
				# # 배송지등록 #
				# # 필수까지
				# scroll_find_xpath(self,driver,'//android.view.View[contains(@text,"(필수)")]')
				# # 이메일
				# wait.until(EC.element_to_be_clickable((By.XPATH, '(//android.widget.EditText)[2]'))).send_keys("amore@naver.com")
				# sleep(2)
				#
				# # 무통장 선택
				# driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.95,TCFG.res[0]*0.5,TCFG.res[1]*0.1)
				# sleep(3)
				# driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime0)
				# center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime0,detectImagePath0)
				# driver.tap([center])
				# sleep(3)
				#
				# driver.press_keycode(123)
				# sleep(3)
				# # 전체동의
				# TouchAction(driver).tap(None, 75, 240, 1).perform()
				# sleep(2)
				# # 결제하기
				# TouchAction(driver).tap(None, 550, 820, 1).perform()
				# sleep(2)
				# # 전체동의
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="전체동의"]'))).click()
				# sleep(2)
				# # 은행선택
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Spinner[@text="은행선택"]'))).click()
				# sleep(2)
				# # 신한은행
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.CheckedTextView[@text="신한은행"]'))).click()
				# sleep(2)
				# # 다음
				# scroll_click_xpath(self,driver,'//android.view.View[@text="다음"]')
				#
				# # 주문이 완료되었습니다 까지
				# wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[contains(@text,"주문이 완료")]')))
				# # 배송/주문조회
				# scroll_click_xpath(self,driver,'//android.widget.Button[contains(@text,"배송/주문조회")]')
				# # 주문취소
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="주문취소"]'))).click()
				# sleep(5)
				# # 전체선택
				# wait.until(EC.element_to_be_clickable((By.XPATH, '//android.view.View[@text="전체 선택"]'))).click()
				# sleep(5)
				# # 다음
				# driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.9,TCFG.res[0]*0.5,TCFG.res[1]*0.1)
				# sleep(3)
				# driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime1)
				# center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime1,detectImagePath1)
				# driver.tap([center])
				# sleep(3)
				#
				# # 결제완료
				# wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="결제완료"]')))
				# # 취소신청
				# driver.swipe(TCFG.res[0]*0.5,TCFG.res[1]*0.9,TCFG.res[0]*0.5,TCFG.res[1]*0.1)
				# sleep(3)
				# driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime2)
				# center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime2,detectImagePath2)
				# driver.tap([center])
				# sleep(3)
				# # 확인
				# driver.save_screenshot('Screenshots/%s-screenshot.png'%currentTime3)
				# center=matching.detectimage('Screenshots/%s-screenshot.png'%currentTime3,detectImagePath3)
				# driver.tap([center])
				# sleep(3)
				# # 취소완료
				# wait.until(EC.presence_of_element_located((By.XPATH, '//android.view.View[@text="취소완료"]')))
				# # 홈으로
                # self.T_Act(TCFG.res[0]*0.1527777777777778, TCFG.res[1]*0.062162162162162166, ratio=18, corr=['19'], wait_sec=3) # 220 184
                # # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 75)
                    TCFG.is_finished = True
                    break
                self.exception('home')
            else:
                print("65 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Purchase)
	unittest.TextTestRunner(verbosity=2).run(suite)
