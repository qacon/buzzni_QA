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
from appium.webdriver.common.touch_action import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

class Cart(testModule):

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

    def test_39_Single_Product(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.widget.TextView')
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
                #검색
                self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # self.T_Act(TCFG.res[0]*0.43796296296296294, TCFG.res[1]*0.11936936936936937, ratio=18, corr=['19'], wait_sec=3) # 473 265
                # self.interact_by_xpath('//android.widget.EditText')
                # 인기검색어 선택
                self.interact_by_xpath('//android.widget.TextView[@text="#스킨"]')
                # 럭스 온 하이라이터 브러쉬 검색
                self.interact_by_xpath('//android.widget.EditText', send_keys_msg="럭스 온 하이라이터 브러쉬")
                # 검색 클릭
                self.interact_by_xpath('(//android.widget.Button)[2]')
                # 상품 클릭
                self.interact_by_xpath('(//android.view.View[@content-desc="에뛰드 하우스 럭스 온 하이라이터 브러쉬"])[1]/android.widget.Image')
                try:
                    self.interact_by_id('closeBt')
                except:
                    pass
                # 가격 노출 확인
                self.interact_by_xpath('//android.widget.TextView[contains(@text,"원")]',click=False)
                # 구매하기
                self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
                # 장바구니 담기
                self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
                self.interact_by_xpath('//android.widget.Button[@text="확인"]')
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="장바구니"]/android.view.View', search_sec=6)
                except:
                    pass
                # 장바구니 타이틀 및 상품확인
                self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
                # 홈버튼
                TCFG.driver.close_app()
                TCFG.driver.launch_app()

            #     # self.interact_by_xpath('//android.widget.EditText') # 검색어 입력
            #     self.T_Act(TCFG.res[0]*0.46574074074074073, TCFG.res[1]*0.11891891891891893, ratio=18, corr=['19'], wait_sec=3) # 503 264
            #     self.interact_by_xpath('//*[contains(@text, "#")]')
            #     # 럭스 온 하이라이터 브러쉬 검색
            #     self.interact_by_xpath('//android.widget.EditText', send_keys_msg="럭스 온 하이라이터 브러쉬")
            #     # 검색 아이콘 클릭
            #     self.interact_by_xpath('(//android.widget.Button)[2]')
            #     # 상품뜰때까지
            #     self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 럭스 온 하이라이터 브러쉬"]/android.widget.Image',click=False)
            #     # 상품클릭
            #     self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 럭스 온 하이라이터 브러쉬"]/android.widget.Image')
            #     # 상품상세
            #     self.interact_by_xpath('//android.view.View[@resource-id="ap_container"]//android.widget.ListView',click=False)
            #     # 구매하기
            #     self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
            #     # 장바구니 담기
            #     self.interact_by_xpath( '//android.widget.Button[@text="장바구니 담기"]')
            #     self.interact_by_xpath( '//android.widget.Button[@text="확인"]')
            #     try:
            #         self.interact_by_xpath('//android.view.View[@content-desc="장바구니"]/android.view.View')
            #     except:
            #         pass
            #     # 장바구니 타이틀 및 상품확인
            #     self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
            #     self.interact_by_xpath('//android.widget.TextView[contains(@text,"럭스 온 하이라이터 브러쉬")]',click=False)
            #     # 홈버튼
            #     self.exception('home')
            #     # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.widget.TextView')
            #     # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.widget.TextView')
            #     # self.interact_by_xpath('//android.widget.Button[@text="이전페이지"]')
            #     # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 66)
                    break
                self.exception('home')
            else:
                print("39 Passed")
                TCFG.is_passed = True
                break

    def test_40_Option_Product(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:

                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
                #검색
                # self.T_Act(TCFG.res[0]*0.43796296296296294, TCFG.res[1]*0.11936936936936937, ratio=18, corr=['19'], wait_sec=3) # 473 265
                # self.interact_by_xpath('//android.widget.EditText')
                self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # 인기검색어 선택
                # self.interact_by_xpath('(//*[contains(@text, "#")])[2]')
                self.interact_by_xpath('//android.widget.TextView[@text="#스킨"]')
                # 매직프레스 검색
                self.interact_by_xpath('//android.widget.EditText', send_keys_msg="매직프레스")
                # 검색 클릭
                self.interact_by_xpath('(//android.widget.Button)[2]')
                # 상품 클릭
                self.interact_by_xpath('(//android.view.View[@content-desc="에뛰드 하우스 매직프레스"])[1]/android.widget.Image')
                try:
                    self.interact_by_id('closeBt')
                except:
                    pass
                # 상품상세
                self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
                # 구매하기
                self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
                # 상품 선택
                self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]')
                self.interact_by_xpath('//android.view.View[contains(@text,"18호")]') # 200813 26호가 품절나서 없어진듯함,,,
                # 장바구니 담기
                self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
                # 확인
                self.interact_by_xpath('//android.widget.Button[@text="확인"]')
                # //android.view.View[contains(@text,"선택하신 상품")]
                # 장바구니 타이틀 및 상품확인
                self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
                self.interact_by_xpath('//android.widget.TextView[contains(@text,"매직프레스")]',click=False)


                # sleep(2)
                # self.interact_by_xpath('//android.widget.EditText', type='presence') # 검색어 입력
                # self.interact_by_xpath('//*[contains(@text, "#")]', type='presence', click=False)
                # # 매직프레스 검색
                # self.interact_by_xpath('(//android.widget.EditText)[2]', send_keys_msg="매직프레스")
                # # 검색
                # self.interact_by_xpath('(//android.view.View[@text="검색"]/android.widget.Button)[3]')
                # # 상품이미지 노출확인 후 클릭
                # self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 매직프레스"]/android.widget.Image',click=False)
                # self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 매직프레스"]/android.widget.Image')
                # # 상품상세
                # self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
                # # 구매하기
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
                # # 상품 선택
                # self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]')
                # self.interact_by_xpath('//android.view.View[contains(@text,"26호")]')
                # # 장바구니 담기
                # self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
                # # 확인
                # self.interact_by_xpath('//android.widget.Button[@text="확인"]')
                # # //android.view.View[contains(@text,"선택하신 상품")]
                # # 장바구니 타이틀 및 상품확인
                # self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
                # self.interact_by_xpath('//android.widget.TextView[contains(@text,"매직프레스")]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 67)
                    break
                self.exception('home')
            else:
                print("40 Passed")
                TCFG.is_passed = True
                break

    def test_41_Cart_number(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
				# 상품수량 과 가격
                self.interact_by_xpath('//android.widget.EditText[@text="1"]',click=False)
                # self.interact_by_xpath('//*[@text="9,800"]',click=False)
				# 수량 증가
                self.interact_by_xpath('(//android.widget.Button[@text="제품 수량 증가"])[1]')
				# 상품수량 과 가격
                self.interact_by_xpath('//android.widget.EditText[@text="2"]',click=False)
                # self.interact_by_xpath('//*[@text="19,600"]',click=False)
				# 수량 증가
                self.interact_by_xpath('(//android.widget.Button[@text="제품 수량 감소"])[1]')
				# 상품수량 과 가격
                self.interact_by_xpath('//android.widget.EditText[@text="1"]',click=False)
                # self.interact_by_xpath('//*[@text="9,800"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 68)
                    break
                self.exception('home')
                self.interact_by_xpath('//android.view.View[contains(@content-desc, "장바구니")]/android.view.View')
                # 장바구니 타이틀
                self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
            else:
                print("41 Passed")
                TCFG.is_passed = True
                break

    def test_42_Change_Order(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
				# 옵션변경
                self.interact_by_xpath('//android.widget.Button[@text="옵션변경"]')
                # 옵션을 선택하세요.
                self.interact_by_xpath('//android.widget.Button[@text="옵션을 선택하세요."]')
				# 선택
                self.interact_by_xpath('//android.widget.Image[contains(@text,"17호")]')
				# 확인
                self.interact_by_xpath('//android.widget.Button[@text="확인"]')
				# 확인
                self.interact_by_xpath('//android.widget.Button[@text="확인"]')
				# 변경된 옵션
                self.interact_by_xpath('//android.view.View[contains(@text,"17호")]',click=False)
                # # 앱 재실행
                # TCFG.driver.close_app()
                # TCFG.driver.launch_app()
                # # # 홈버튼
                # # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.widget.TextView')
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 69)
                    break
                self.exception('home')
                self.interact_by_xpath('//android.view.View[contains(@content-desc, "장바구니")]/android.view.View')
                # 장바구니 타이틀
                self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
            else:
                print("42 Passed")
                TCFG.is_passed = True
                break

    # 수정필요 시나리오 수정 필요
    def test_43_Uncheck_Product(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                try:
                    # 장바구니
                    self.interact_by_xpath('//android.view.View[contains(@content-desc, "장바구니")]/android.view.View')
                except:
                    pass
                self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
                # 체크해제
                self.interact_by_xpath('//*[@text="장바구니에 담은 상품 ("]', wait_sec=5)
                # 체크
                self.interact_by_xpath('//*[@text="장바구니에 담은 상품 ("]')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 71)
                    break
                self.exception('home')
            else:
                print("43 Passed")
                TCFG.is_passed = True
                break

    # 수정필요 시나리오 수정 필요
    def test_44_Delete_Product(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//*[@text="더보기"]') # 아이템 목록 접기
                # 없애기
                self.interact_by_xpath('//android.widget.Button[@text="선택 삭제"]')
				# 확인
                self.interact_by_xpath('//android.widget.Button[@text="확인"]')
				# 확인
                self.interact_by_xpath('//android.widget.Button[@text="확인"]')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 72)
                    break
                self.exception('home')
                self.interact_by_xpath('//android.view.View[contains(@content-desc, "장바구니")]/android.view.View')
                # 장바구니 타이틀
                self.interact_by_xpath('//android.widget.Button[@text="없애기"]',click=False)
            else:
                print("44 Passed")
                TCFG.is_passed = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Cart)
	unittest.TextTestRunner(verbosity=2).run(suite)
