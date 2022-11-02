# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

class Category(testModule):

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
        print(3)
        TCFG.driver.close_app()
        sleep(2)
        TCFG.driver.launch_app()
        sleep(2)

    def test_01_Outlet(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_id('홈', search_sec=20, click=False) # 홈 버튼 노출 확인
                self.interact_by_xpath('//*[contains(@name, "아울렛")]', search_sec=20) # 아울렛 클릭
                self.interact_by_xpath('//*[contains(@name, "베스트")]', search_sec=20, click=False) # 베스트 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
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

    def test_02_MoaChart(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//*[contains(@name, "모아차트")]', search_sec=20) # 모아차트 클릭
                self.interact_by_xpath('//*[contains(@name, "전체")]', search_sec=20, click=False) # 전체 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("2 Passed")
                TCFG.is_passed = True
                break

    def test_03_ShoppingLive(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//*[contains(@name, "쇼핑라이브")]', search_sec=20) # 쇼핑라이브 클릭
                self.interact_by_xpath('//*[contains(@name, "지금 인기있는 방송들이에요!")]', search_sec=20, click=False) # 지금 인기있는 방송들이에요! 텍스트 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("3 Passed")
                TCFG.is_passed = True
                break

    def test_04_Category(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_id('홈', search_sec=20) # 홈쇼핑모아 로고 클릭
                self.interact_by_xpath('//*[contains(@name, "의류")]', search_sec=20) # 의류 카테고리 클릭
                self.interact_by_id('의류', search_sec=20, click=False) # 페이지 타이틀 노출 확인
                self.interact_by_xpath('//*[contains(@name, "추천순")]', search_sec=20, click=False) # 추천순 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
                self.interact_by_id('뒤로가기', search_sec=20) # 뒤로가기 버튼 클릭
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("4 Passed")
                TCFG.is_passed = True
                break

    def test_05_Search(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_id('홈', search_sec=20) # 홈쇼핑모아 로고 클릭
                self.interact_by_xpath('//*[contains(@name, "검색")]', search_sec=20) # 검색 클릭
                self.interact_by_id('search_edittext', search_sec=20, send_keys_msg="마스크", click=False) # 마스크 입력
                self.interact_by_id('search_btn', search_sec=20) # 검색
                self.interact_by_xpath('//*[contains(@name, "알람받기")]', search_sec=20, click=False) # 알람받기 버튼 노출 확인
                self.interact_by_xpath('//*[contains(@name, "전체")]', search_sec=20, click=False) # 전체 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
                self.interact_by_id('뒤로가기', search_sec=20) # 뒤로가기 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    TCFG.is_finished = True
                    self.assertEqual(0, 1)
                    break
            else:
                print("5 Passed")
                TCFG.is_finished = True
                TCFG.is_passed = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Category)
	unittest.TextTestRunner(verbosity=2).run(suite)
