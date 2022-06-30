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

class Etc(testModule):

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

    # 구매후기 삭제됨
    def test_47_Product_DetailReview(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # TCFG.driver.close_app()
                # TCFG.driver.launch_app()
                # sleep(2)
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기
                # #검색
                # self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # # 인기검색어 선택
                # self.interact_by_xpath('//android.widget.TextView[@text="#스킨"]')
                # # 럭스 온 하이라이터 브러쉬 검색
                # self.interact_by_xpath('//android.widget.EditText', send_keys_msg="글라스 루즈 틴트")
                # # 검색 아이콘 클릭
                # self.interact_by_xpath('(//android.widget.Button)[2]')
                # # 상품뜰때까지
                # self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 글라스 루즈 틴트"]/android.widget.Image',click=False)
                # # 상품클릭
                # self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 글라스 루즈 틴트"]/android.widget.Image')
                # try:
                #     self.interact_by_id('closeBt')
                # except:
                #     pass
                # # 구매후기 클릭
                # scroll_xpath(self, '//android.widget.TextView[@text="구매후기"]', loc=TCFG.res[1]*0.9, y1=TCFG.res[0]*0.9, y2=TCFG.res[0]*0.5)
                # # self.interact_by_xpath('//android.widget.TextView[@text="구매후기"]')
                # sleep(5)
                # # 이미지 더보기 버튼 클릭
                # self.T_Act(TCFG.res[0]*0.8453703703703703, TCFG.res[1]*0.577027027027027, ratio=18, corr=['19'], wait_sec=5) # 913 1281
                # sleep(4)
                # # 아래로 스와이프
                # TCFG.driver.swipe(91, 600, 91, 200)
                # sleep(5)
                # # 위로 스와이프
                # TCFG.driver.swipe(91, 200, 91, 600)
                # sleep(4)
                # self.interact_by_xpath('//android.view.View[@text="갤러리"]', click=False) # 갤러리 노출 확인
            except:
                # if loop_count == (TCFG.check_loop_count-1):
                print("Error!")
                self.assertEqual(0, 78)
                break
            else:
                print("47 Passed")
                TCFG.is_passed = True
                break

    def test_48_Product_Detail(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                TCFG.driver.close_app()
                TCFG.driver.launch_app()
                sleep(2)
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기
                #검색
                self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # 인기검색어 선택
                self.interact_by_xpath('//android.widget.TextView[@text="#스킨"]')
                # 럭스 온 하이라이터 브러쉬 검색
                self.interact_by_xpath('//android.widget.EditText', send_keys_msg="글라스 루즈 틴트")
                # 검색 아이콘 클릭
                self.interact_by_xpath('(//android.widget.Button)[2]')
                # 상품뜰때까지
                self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 글라스 루즈 틴트"]/android.widget.Image',click=False)
                # 상품클릭
                self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 글라스 루즈 틴트"]/android.widget.Image')
                try:
                    self.interact_by_id('closeBt')
                except:
                    pass
                # 최하단으로 이동 클릭
                TCFG.driver.press_keycode(123)
                sleep(5)
                # 전성분/상세정보제공고 보기 버튼 클릭
                self.T_Act(TCFG.res[0]*0.10648148148148148, TCFG.res[1]*0.1900900900900901, ratio=18, corr=['19'], wait_sec=3) # 115 422
                # 아래로 스와이프
                TCFG.driver.swipe(91, 500, 91, 200)
                sleep(5)
                # 위로 스와이프
                TCFG.driver.swipe(91, 200, 91, 500)
                sleep(5)
                # self.interact_by_xpath('//android.view.View[@text="사용방법"]', click=False) # 사용방법 노출 확인
            except:
                # if loop_count == (TCFG.check_loop_count-1):
                print("Error!")
                self.assertEqual(0, 79)
                break
            else:
                print("48 Passed")
                TCFG.is_passed = True
                break

    def test_49_Product_delivery(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                TCFG.driver.close_app()
                TCFG.driver.launch_app()
                sleep(2)
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기
                #검색
                self.interact_by_xpath('//android.widget.Button[@text="검색"]')
                # 인기검색어 선택
                self.interact_by_xpath('//android.widget.TextView[@text="#스킨"]')
                # 럭스 온 하이라이터 브러쉬 검색
                self.interact_by_xpath('//android.widget.EditText', send_keys_msg="글라스 루즈 틴트")
                # 검색 아이콘 클릭
                self.interact_by_xpath('(//android.widget.Button)[2]')
                # 상품뜰때까지
                self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 글라스 루즈 틴트"]/android.widget.Image',click=False)
                # 상품클릭
                self.interact_by_xpath('//android.view.View[@content-desc="에뛰드 하우스 글라스 루즈 틴트"]/android.widget.Image')
                try:
                    self.interact_by_id('closeBt')
                except:
                    pass
                # 최하단으로 이동 클릭
                TCFG.driver.press_keycode(123)
                sleep(5)
                # 배송/교환/반품 안내 버튼 클릭
                self.T_Act(TCFG.res[0]*0.15648148148148147, TCFG.res[1]*0.23468468468468467, ratio=18, corr=['19'], wait_sec=3) # 169 521
                # 아래로 스와이프
                TCFG.driver.swipe(91, 500, 91, 200)
                sleep(5)
                # 위로 스와이프
                TCFG.driver.swipe(91, 200, 91, 500)
                sleep(5)
                # 잡히는 element가 없음
                # self.interact_by_xpath('//android.view.View[@text="※ 배송관련"]', click=False) # ※ 배송관련 노출 확인
            except:
                # if loop_count == (TCFG.check_loop_count-1):
                print("Error!")
                self.assertEqual(0, 80)
                TCFG.is_finished = True
                break
            else:
                print("49 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            # self.exception('home')
            # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False) # 에뛰드 로고 대기
            # # 카테고리 열기
            # self.interact_by_xpath('//android.widget.Button[@text="카테고리 열기"]')
            # # 마이에뛰드
            # self.interact_by_xpath('(//android.view.View[@content-desc="마이에뛰드"])[1]/android.view.View')
            # # 로그아웃
            # TCFG.driver.press_keycode(123)
            # sleep(3)
            # if TCFG.res[1] < 1500:
            #     self.T_Act(TCFG.res[0]*0.1486111111111111, TCFG.res[1]*0.4, ratio=18, low_corr=False, wait_sec=3) # 214 1410
            # else:
            #     self.T_Act(TCFG.res[0]*0.1486111111111111, TCFG.res[1]*0.47635135135135137, ratio=18, low_corr=False, wait_sec=3) # 214 1410
            # # ETUDEHOUSE
            # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False)
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Etc)
	unittest.TextTestRunner(verbosity=2).run(suite)
