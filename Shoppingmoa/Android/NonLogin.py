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

class NonLogin(testModule):

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

    def test_45_Logout(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 마이에뛰드
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="마이에뛰드"]') # 마이에뛰드 탭
                except:
                    self.interact_by_xpath('//android.view.View[@text="마이에뛰드"]') # 마이에뛰드 탭
                # 개인정보 수정 클릭
                self.interact_by_xpath('//*[contains(@text,"개인정보 수정")]') # 개인정보 수정 탭
                sleep(1)
                # 본인확인 텍스트 노출
                self.interact_by_xpath('//*[contains(@text, "본인확인")]', click=False)
                # 스크롤내리기
                TCFG.driver.swipe(500,1300,500,200)
                sleep(2)
                TCFG.driver.swipe(500,1300,500,200)
                sleep(2)
                # 로그아웃 클릭
                self.interact_by_xpath('//*[contains(@text,"로그아웃")]')
                sleep(1)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 76)
                    break
                self.exception('home')
            else:
                print("45 Passed")
                TCFG.is_passed = True
                break

    def test_46_Nonmember_ShoppingCart(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기
                #검색
                # self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # self.interact_by_xpath('//*[contains(@text, "#")]')
                self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # 인기검색어 선택
                self.interact_by_xpath('//android.widget.TextView[@text="#스킨"]')
                # 순정 립 앤 아이 리무버 검색
                self.interact_by_xpath('//android.widget.EditText', send_keys_msg="순정 립 앤 아이 리무버")
                # 검색
                self.interact_by_xpath('(//android.widget.Button)[2]')
                # 상품이미지 노출확인 후 클릭
                self.interact_by_xpath('//*[contains(@content-desc,"순정 립 앤 아이 리무버 100ml")]/android.widget.Image',click=False)
                self.interact_by_xpath('//*[contains(@content-desc,"순정 립 앤 아이 리무버 100ml")]/android.widget.Image') # 상품 이미지
                try:
                    self.interact_by_id('closeBt')
                except:
                    pass
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="구매하기"]') # 구매하기
                    self.interact_by_xpath('//android.widget.Button[@text="바로구매"]') # 바로구매
                    self.interact_by_xpath('//android.widget.Button[@text="비회원 주문"]') # 비회원 주문
                    self.interact_by_xpath('//*[@text="모든 약관 동의"]') # 약관 동의
                    self.interact_by_xpath('//*[@text="동의함"]') # 동의함 탭
                    self.interact_by_xpath('//android.view.View[@text="결제하기"]') # 결제하기 타이틀
                    self.exception('home') # 홈으로
                    self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 메인 화면 노출 확인
                    TCFG.driver.close_app()
                    sleep(1)
                except:
                    TCFG.driver.back()
                    sleep(3)
                    self.interact_by_xpath('//android.widget.Button[@text="검색어 삭제"]') # 검색어 삭제
                    self.interact_by_xpath('//android.widget.EditText', send_keys_msg="로픈 바오밥 헤어 미스트")
                    # 검색
                    self.interact_by_xpath('(//android.widget.Button)[2]')

                    self.interact_by_xpath('//*[contains(@content-desc,"로픈 바오밥 로픈 바오밥 수분언덕 헤어 미스트 100g")]/android.widget.Image') # 상품 이미지
                    try:
                        self.interact_by_id('closeBt')
                    except:
                        pass
                    self.interact_by_xpath('//android.widget.Button[@text="구매하기"]') # 구매하기
                    self.interact_by_xpath('//android.widget.Button[@text="바로구매"]') # 바로구매
                    self.interact_by_xpath('//android.widget.Button[@text="비회원 주문"]') # 비회원 주문
                    self.interact_by_xpath('//*[@text="모든 약관 동의"]') # 약관 동의
                    self.interact_by_xpath('//*[@text="동의함"]') # 동의함 탭
                    self.interact_by_xpath('//android.view.View[@text="결제하기"]') # 결제하기 타이틀
                    self.exception('home') # 홈으로
                    self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 메인 화면 노출 확인
                    TCFG.driver.close_app()


                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False) # 메인 화면 노출 확인
                # self.interact_by_xpath('//android.widget.EditText', type='presence') # 검색어 입력
                # self.interact_by_xpath('//*[contains(@text, "#")]', type='presence', click=False)
                # self.interact_by_xpath('(//android.widget.EditText)[2]',send_keys_msg="순정 립 앤 아이 리무버") # 순정 립 앤 아이 리무버 검색
                # self.interact_by_xpath('(//android.view.View[@text="검색"]/android.widget.Button)[3]') # 검색
                # self.interact_by_xpath('//android.view.View[@content-desc="순정 립 앤 아이 리무버 100ml"]/android.widget.Image') # 상품 이미지
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]') # 구매하기
                # self.interact_by_xpath('//android.widget.Button[@text="바로구매"]') # 바로구매
                # self.interact_by_xpath('//android.widget.Button[@text="비회원 주문"]') # 비회원 주문
                # self.interact_by_xpath('//*[@text="모든 약관 동의"]') # 약관 동의
                # self.interact_by_xpath('//*[@text="동의함"]') # 동의함 탭
                # self.interact_by_xpath('//android.view.View[@text="결제하기"]') # 결제하기 타이틀
                # self.exception('home') # 홈으로
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 메인 화면 노출 확인
                # TCFG.driver.close_app()
                # sleep(1)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 77)
                    TCFG.is_finished = True
                    break
                self.exception('home')
            else:
                print("46 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(NonLogin)
	unittest.TextTestRunner(verbosity=2).run(suite)
