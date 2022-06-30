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

class Home(testModule):

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
        self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False, type='presence') # 에뛰드 로고 대기

    def test_04_Home(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False, type='presence') # 에뛰드 로고 대기
				# # 홈으로
                # self.interact_by_xpath('//android.view.View[@content-desc="홈으로"]/android.view.View')
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False, type='presence') # 에뛰드 로고 대기
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 14)
                    break
                self.exception('home')
            else:
                print("4 Passed")
                TCFG.is_passed = True
                break

    # 수정필요
    def test_05_New_Arrivals(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                try:
                    # 신상품
                    self.interact_by_xpath('//android.view.View[@content-desc="신상품"]')
                except:
                    self.interact_by_xpath('//android.view.View[@text="신상품"]')
				# 첫번째 신상품 이미지
                self.interact_by_xpath('//android.widget.ListView//android.widget.Image',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 17)
                    break
                self.exception('home')
            else:
                print("5 Passed")
                TCFG.is_passed = True
                break

    # 수정필요
    def test_06_NewProduct_Detailed(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
				# # 첫번째 신상품 이미지
                # self.interact_by_xpath('(//android.widget.Image)[2]')
				# # 구매후기
                # self.interact_by_xpath('//android.view.View[contains(@content-desc, "구매후기")]')
				# # 상품리뷰작성까지
                # self.T_Act(TCFG.res[0]*0.4875, TCFG.res[1]*0.12060810810810811, ratio=18, corr=['19'], wait_sec=10) # 702 357
                # # 닫기버튼 클릭
                # self.T_Act(TCFG.res[0]*0.9465277777777777, TCFG.res[1]*0.05439189189189189, ratio=18, corr=['19'], wait_sec=3) # 1363 161
                # # 구매하기
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 18)
                    break
                self.exception('home')
                try:
                    # 신상품
                    self.interact_by_xpath('//android.view.View[@content-desc="신상품"]')
                except:
                    self.interact_by_xpath('//android.view.View[@text="신상품"]')
                # 첫번째 신상품
                self.interact_by_xpath('//android.view.View[@text="신상품"]',click=False)
            else:
                print("6 Passed")
                TCFG.is_passed = True
                break

    # 수정필요
    def test_07_NewProduct_Cart(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 구매하기
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
            except: # 상품 없는 경우
                print("7 Passed")
                self.exception('home')
                TCFG.is_passed = True
                break
            else:
                try:
                    sleep(2)
                #     try: # 상품 옵션있는경우
                #         self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]', search_sec=5)
                #         self.T_Act(TCFG.res[0]*0.31805555555555554, TCFG.res[1]*0.4966216216216216, ratio=18, corr=['19'], wait_sec=3) # 458, 1470
                #     except:
                #         pass
    			# 	# 장바구니 담기
                #     self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
    			# 	# 장바구니로 이동하시겠습니까?
                #     self.interact_by_xpath('//android.view.View[contains(@text,"장바구니로 이동하시겠습니까?")]')
    			# 	#  레이어닫기
                #     self.interact_by_xpath('//android.widget.Button[@text="레이어 닫기"]')
    			# 	# 홈으로
                #     self.T_Act(TCFG.res[0]*0.1527777777777778, TCFG.res[1]*0.062162162162162166, ratio=18, corr=['19'], wait_sec=10) # 220 184
                #     self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',click=False)
                except:
                    if loop_count == (TCFG.check_loop_count-1):
                        print("Error!")
                        self.assertEqual(0, 19)
                        break
                    self.exception('home')
                    try:
                        # 신상품
                        self.interact_by_xpath('//android.view.View[@content-desc="신상품"]')
                    except:
                        self.interact_by_xpath('//android.view.View[@text="신상품"]')
                    try:
                        # 신상품
                        self.interact_by_xpath('//android.view.View[@text="신상품"]')
                    except:
                        self.interact_by_xpath('//android.view.View[@content-desc="신상품"]')
                    # 상품상세
                    self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
                else:
                    print("19 Passed")
                    TCFG.is_passed = True
                    break

    def test_08_Best(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                try:
                    # 베스트
                    self.interact_by_xpath('//android.view.View[@content-desc=" 베스트 "]/android.widget.TextView')
                except:
                    self.interact_by_xpath('//android.view.View[@content-desc="베스트"]/android.widget.TextView')
				# 첫번째 상품
                self.interact_by_xpath('(//android.widget.Image)[2]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 20)
                    break
                self.exception('home')
            else:
                print("8 Passed")
                TCFG.is_passed = True
                break

    def test_09_Best_Cart(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 첫번째 상품
                # self.interact_by_xpath('//android.widget.Button[@text="구매하기"]')
                # # 상품 옵션있는경우
                # try:
                #     self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]', search_sec=5)
                #     self.T_Act(TCFG.res[0]*0.3509259259259259, TCFG.res[1]*0.8108108108108109, ratio=18, corr=['19'], wait_sec=3) # 379, 1800
                # except:
                # 	pass
                # # 장바구니 담기
                # self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
                # # 장바구니로 이동하시겠습니까?
                # self.interact_by_xpath('//android.view.View[contains(@text,"장바구니로 이동하시겠습니까?")]', click=False)
                # #  레이어닫기
                # self.interact_by_xpath('//android.widget.Button[@text="레이어 닫기"]')
                # TCFG.driver.swipe(TCFG.res[0]*0.5, TCFG.res[1]*0.5, TCFG.res[0]*0.5, TCFG.res[1]*0.9)
                # sleep(2)
                # # 홈으로
                # self.exception('home')
                # self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]',type='presence', click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 22)
                    break
                self.exception('home')
                try:
                    # 베스트
                    self.interact_by_xpath('//android.view.View[@content-desc=" 베스트 "]/android.widget.TextView')
                except:
                    self.interact_by_xpath('//android.view.View[@content-desc="베스트"]/android.widget.TextView')
                # 첫번째 상품
                self.interact_by_xpath('(//android.widget.Image)[2]')
                # 상품상세
                self.interact_by_xpath('//android.view.View[@text="상품상세"]', click=False)
            else:
                print("9 Passed")
                TCFG.is_passed = True
                break

    def test_10_Event(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                try:
                    # Event 클릭
                    self.interact_by_xpath('//android.view.View[@content-desc=" 이벤트 "]/android.widget.TextView')
                except:
                    self.interact_by_xpath('//android.view.View[@content-desc="이벤트"]/android.widget.TextView')
                # 첫번째 이벤트 창까지
                self.interact_by_xpath('//*[contains(@text,"발표")]',click=False)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 25)
                    break
                self.exception('home')
            else:
                print("10 Passed")
                TCFG.is_passed = True
                break

    def test_11_Event_Sharing(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//*[contains(@text,"발표")]',click=False)
                # 첫번째 이벤트창 클릭
                self.T_Act(TCFG.res[0]*0.4824074074074074, TCFG.res[1]*0.3954954954954955, ratio=18, low_corr=False, wait_sec=3) # 521 878
                # 이벤트 상세까지
                self.interact_by_xpath('//android.view.View[@text="이벤트 상세"]',click=False)
                # 공유하기 아이콘
                self.interact_by_xpath('//*[contains(@text,"공유")]')
                # 레이어닫기
                self.interact_by_xpath('//android.widget.Button[@text="레이어 닫기"]')
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 26)
                    break
                self.exception('home')
                try:
                    # Event 클릭
                    self.interact_by_xpath('//android.view.View[@content-desc="이벤트"]')
                except:
                    self.interact_by_xpath('//android.view.View[@text="이벤트"]')
                # 첫번쨰 이벤트 창까지
                self.interact_by_xpath('//*[@resource-id="ap_container"]/android.widget.ListView/android.view.View',click=False)
            else:
                print("11 Passed")
                TCFG.is_passed = True
                break

    def test_12_SelectShop(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                TCFG.driver.close_app()
                sleep(2)
                TCFG.driver.launch_app()
                sleep(2)
                self.interact_by_xpath('//android.widget.Image[@text="ETUDEHOUSE"]', click=False, type='presence') # 에뛰드 로고 대기
                try:
                    # 베스트
                    self.interact_by_xpath('//android.view.View[@content-desc=" 베스트 "]/android.widget.TextView')
                except:
                    self.interact_by_xpath('//android.view.View[@content-desc="베스트"]/android.widget.TextView')
                # 셀렉샵
                self.interact_by_xpath('//android.view.View[@content-desc="셀렉샵"]/android.widget.TextView')
                # 셀렉샵 이미지 확인
                self.interact_by_xpath('//android.view.View[@text="다양한 브랜드를 만나는 감성 셀렉샵"]',click=False)
                # # 임의의 카테고리 선택(#디자인팬시)
                # self.interact_by_xpath('//android.view.View[@text="#디자인팬시"]')
                # # 정렬 선택
                # self.interact_by_xpath('//android.widget.Spinner[@text="신상품순"]')
                # self.interact_by_xpath('//android.widget.CheckedTextView[@text="판매순"]')
                # # 임의 상품 선택
                # prdtName1 = self.get_attri('(//android.widget.Image)[11]', ec='click', strategy=By.XPATH, att='text')
                # print(prdtName1)
                # self.interact_by_xpath('(//android.widget.Image)[11]')
                # # 뒤로가기 선택
                # TCFG.driver.back()
                # sleep(2)
                # # 위와 같은 위치의 상품의 텍스트 추출
                # prdtName2 = self.get_attri('(//android.widget.Image)[11]', ec='click', strategy=By.XPATH, att='text')
                # print(prdtName2)
                # # 선택한 카테고리 확인
                # if prdtName1 == prdtName2:
                #     pass
                # else:
                #     print("Error!")
                #     self.assertEqual(0, 29)
                #     break
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 29)
                    break
                self.exception('home')
            else:
                print("12 Passed")
                TCFG.is_passed = True
                break

    def test_13_SelectShop_NoEventProducts(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 상품보기 변경
                # self.interact_by_xpath('//android.widget.Button[@text="상품보기변경"]')
                self.interact_by_xpath('//android.view.View[@content-desc="키스뉴욕"]') #키스뉴욕 탭 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="행사상품"]') #행사상품 버튼 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@text="상품이 존재하지 않습니다."]',click=False) #상품이 존재하지 않습니다 텍스트 노출 확인
                except:
                    self.interact_by_xpath('//android.widget.TextView[@text="원"]',click=False) #첫 번째 상품 노출 확인

                TCFG.driver.back()
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 30)
                    break
                self.exception('home')
                #쿠폰/혜택 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="쿠폰/혜택"]/android.widget.TextView')
                # 셀렉샵
                self.interact_by_xpath('//android.view.View[@content-desc="셀렉샵"]/android.widget.TextView')
                # 셀렉샵 이미지 확인
                self.interact_by_xpath('//android.view.View[@text="다양한 브랜드를 만나는 감성 셀렉샵"]',click=False)
            else:
                print("13 Passed")
                TCFG.is_passed = True
                break

    def test_14_SelectShop_EventProducts(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                self.interact_by_xpath('//android.view.View[@content-desc="보다나"]') #VODANA 탭 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="행사상품"]') #행사상품 버튼 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@text="상품이 존재하지 않습니다."]',click=False) #상품이 존재하지 않습니다 텍스트 노출 확인
                except:
                    self.interact_by_xpath('//android.widget.TextView[@text="원"]',click=False) #첫 번째 상품 노출 확인
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 31)
                    break
                self.exception('home')
                #쿠폰/혜택 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="쿠폰/혜택"]/android.widget.TextView')
                # 셀렉샵
                self.interact_by_xpath('//android.view.View[@content-desc="셀렉샵"]/android.widget.TextView')
                self.interact_by_xpath('//android.view.View[@text="다양한 브랜드를 만나는 감성 셀렉샵"]',click=False)
            else:
                print("14 Passed")
                TCFG.is_passed = True
                break

    def test_15_SelectShop_ChangeView(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 구매하기
                # # self.T_Act(TCFG.res[0]*0.4625, TCFG.res[1]*0.9510135135135135, ratio=18, corr=['19'], wait_sec=3) # 666 2815
                # self.interact_by_xpath('//*[@text="구매하기"]')
                # # 상품 옵션있는경우
                # try:
                #     self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]', search_sec=5)
                #     self.T_Act(TCFG.res[0]*0.31805555555555554, TCFG.res[1]*0.4966216216216216, ratio=18, low_corr=False, wait_sec=3) # 458, 1470
                # except:
                # 	pass
                # # 장바구니 담기
                # self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
                # # 장바구니로 이동하시겠습니까?
                # self.interact_by_xpath('//android.view.View[contains(@text,"장바구니로 이동하시겠습니까?")]', click=False)
                # # 취소
                # self.interact_by_xpath('//android.widget.Button[@text="취소"]')
                # TCFG.driver.close_app()
                # TCFG.driver.launch_app()
                # sleep(2)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 32)
                    TCFG.is_finished = True
                    break
                self.exception('home')
                #쿠폰/혜택 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="쿠폰/혜택"]/android.widget.TextView')
                # 셀렉샵
                self.interact_by_xpath('//android.view.View[@content-desc="셀렉샵"]/android.widget.TextView')
                self.interact_by_xpath('//android.view.View[@text="다양한 브랜드를 만나는 감성 셀렉샵"]',click=False)
                self.T_Swipe(x1=TCFG.res[0]*0.5, y1=TCFG.res[1]*0.9, x2=TCFG.res[0]*0.5, y2=TCFG.res[1]*0.8, ratio=16, low_corr=False)
                self.interact_by_xpath('//android.widget.Image[contains(@text, "[")]')
                self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
            else:
                print("15 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def test_16_SelectShop_Cart(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                sleep(2)
                # # 구매하기
                # # self.T_Act(TCFG.res[0]*0.4625, TCFG.res[1]*0.9510135135135135, ratio=18, corr=['19'], wait_sec=3) # 666 2815
                # self.interact_by_xpath('//*[@text="구매하기"]')
                # # 상품 옵션있는경우
                # try:
                #     self.interact_by_xpath('//android.widget.Button[@text="상품 선택"]', search_sec=5)
                #     self.T_Act(TCFG.res[0]*0.31805555555555554, TCFG.res[1]*0.4966216216216216, ratio=18, low_corr=False, wait_sec=3) # 458, 1470
                # except:
                # 	pass
                # # 장바구니 담기
                # self.interact_by_xpath('//android.widget.Button[@text="장바구니 담기"]')
                # # 장바구니로 이동하시겠습니까?
                # self.interact_by_xpath('//android.view.View[contains(@text,"장바구니로 이동하시겠습니까?")]', click=False)
                # # 취소
                # self.interact_by_xpath('//android.widget.Button[@text="취소"]')
                # TCFG.driver.close_app()
                # TCFG.driver.launch_app()
                # sleep(2)
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 32)
                    TCFG.is_finished = True
                    break
                self.exception('home')
                #쿠폰/혜택 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="쿠폰/혜택"]/android.widget.TextView')
                # 셀렉샵
                self.interact_by_xpath('//android.view.View[@content-desc="셀렉샵"]/android.widget.TextView')
                self.interact_by_xpath('//android.view.View[@text="다양한 브랜드를 만나는 감성 셀렉샵"]',click=False)
                self.T_Swipe(x1=TCFG.res[0]*0.5, y1=TCFG.res[1]*0.9, x2=TCFG.res[0]*0.5, y2=TCFG.res[1]*0.8, ratio=16, low_corr=False)
                self.interact_by_xpath('//android.widget.Image[contains(@text, "[")]')
                self.interact_by_xpath('//android.view.View[@text="상품상세"]',click=False)
            else:
                print("16 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break

    def test_17_History(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                TCFG.driver.close_app()
                sleep(2)
                TCFG.driver.launch_app()
                sleep(2)

                self.interact_by_xpath('//android.view.View[@content-desc="히스토리"]') #히스토리 탭 클릭
                sleep(2)
                self.interact_by_xpath('//android.view.View[@text="쇼핑 히스토리"]',click=False) #쇼핑 히스토리 텍스트 노출 확인
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 32)
                    TCFG.is_finished = True
                    break
                self.exception('home')
            else:
                print("17 Passed")
                TCFG.is_passed = True
                TCFG.is_finished = True
                break


    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Home)
	unittest.TextTestRunner(verbosity=2).run(suite)
