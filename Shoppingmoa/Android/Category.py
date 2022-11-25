# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

# 테스트 소요시간 : 약 20분
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
        sleep(2)
        TCFG.driver.close_app()
        # TCFG.driver.terminate_app('com.buzzni.android.subapp.shoppingmoa')
        sleep(1)
        TCFG.driver.launch_app()
        sleep(1)
        try:
            self.interact_by_id('mid_popup_activity_stop_today_btn', search_sec=5) # 오늘은 그만보기 클릭
        except:
            pass
        try:
            self.interact_by_id('timeline_floating_banner_close_btn', search_sec=5) # 플로팅 배너 닫기 클릭
        except:
            pass

    def test_01_Best(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                try:
                    self.interact_by_id('mid_popup_activity_stop_today_btn', search_sec=30) # 오늘은 그만보기 클릭
                except:
                    pass
                try:
                    self.interact_by_id('timeline_floating_banner_close_btn', search_sec=20) # 플로팅 배너 닫기 클릭
                except:
                    pass
                self.interact_by_xpath('//android.widget.TextView[@text="베스트"]', search_sec=30, wait_sec=20)  # 베스트 클릭
                self.interact_by_xpath('//android.widget.Button[@text="전체"]', search_sec=20, click=False)  # 전체 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.widget.ListView/android.view.View[1]/android.view.View', search_sec=10, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
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

    def test_02_Outlet(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="아울렛"]', search_sec=20) # 아울렛 클릭
                self.interact_by_xpath('//android.widget.Button[@text="베스트"]', search_sec=20, click=False) # 베스트 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=10, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
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

    # def test_03_kimjang_daejeon(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_xpath('//android.widget.TextView[@text="김장대전"]', search_sec=20) # 아울렛 클릭
    #             self.interact_by_xpath('//android.widget.TextView[@text="김장대전 BEST"]', search_sec=20, click=False) # 김장대전 BEST 텍스트 노출 확인
    #             self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ListView/android.view.View[1]', search_sec=10, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #         except:
    #             if loop_count == (TCFG.check_loop_count-1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("3 Passed")
    #             TCFG.is_passed = True
    #             break

    def test_03_New(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="신상품"]', search_sec=30) # 신상품 클릭
                self.interact_by_xpath('//android.widget.Button[@text="전체"]', search_sec=20, click=False) # 전체 버튼 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]/android.widget.ListView/android.view.View[1]/android.view.View', search_sec=10, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
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

    def test_04_ShoppingLive(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="쇼핑라이브"]', search_sec=30, wait_sec=10) # 쇼핑라이브 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="지금 인기있는 방송들이에요!"]', search_sec=60, click=False) # 지금 인기있는 방송들이에요! 텍스트 노출 확인
                self.interact_by_xpath('//android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View', search_sec=10, click=False) # 방송영역 전체 노출 확인
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

    def test_05_Nov_Sale(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_xpath('//android.widget.TextView[@text="쇼핑라이브"]', search_sec=30, wait_sec=10) # 쇼핑라이브 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="11월의 할인"]', search_sec=30) # 11월의 할인 클릭
                self.interact_by_id('com.buzzni.android.subapp.shoppingmoa:id/top_tob_item_swipe_refresh', search_sec=10, click=False) # 11월의 할인 이미지 영역 노출 확인
                self.interact_by_xpath('//android.view.View[@resource-id="KakaoShare"]', search_sec=20, click=False) # 카카오톡 공유 버튼 노출 확인
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("5 Passed")
                TCFG.is_passed = True
                break

    def test_06_Category(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
                self.interact_by_id('main_timeline_short_cut_item_image', search_sec=20) # 첫번째 카테고리 클릭
                self.interact_by_id('default_header_title', search_sec=20, click=False) # 페이지 타이틀 노출 확인
                self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
                self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
                self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
            except:
                if loop_count == (TCFG.check_loop_count-1):
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("6 Passed")
                TCFG.is_passed = True
                break

    def test_07_Search(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭+
                self.interact_by_xpath('//android.widget.TextView[@text="검색"]', search_sec=20, wait_sec=10) # 검색 클릭
                self.interact_by_id('search_edittext', search_sec=20, send_keys_msg="마스크", click=False) # 마스크 입력
                self.interact_by_id('search_btn', search_sec=20) # 검색
                self.interact_by_xpath('//android.widget.Button[contains(@text,"알람받기")]', search_sec=20, click=False) # 알람받기 버튼 노출 확인
                self.interact_by_xpath('//android.widget.Button[contains(@text,"전체")]', search_sec=20, click=False) # 전체 버튼 노출 확인
                self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View[1]', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
            except:
                if loop_count == 0:
                    print("Error!")
                    TCFG.is_finished = True
                    self.assertEqual(0, 1)
                    break
            else:
                print("7 Passed")
                TCFG.is_finished = True
                TCFG.is_passed = True
                break







    # def test_05_Food(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=10) # 홈쇼핑모아 로고 클릭
    #             self.interact_by_xpath('//android.widget.TextView[@text="식품"]', search_sec=20, wait_sec=10) # 식품 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 식품 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("5 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_06_Home_Appliances(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             self.interact_by_xpath('//android.widget.TextView[@text="가전"]', search_sec=20, wait_sec=10) # 가전 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 가전 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("6 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_07_Beauty(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             self.interact_by_xpath('//android.widget.TextView[@text="뷰티"]', search_sec=20, wait_sec=10) # 뷰티 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 뷰티 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("7 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_08_Goods(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             self.interact_by_xpath('//android.widget.TextView[@text="잡화"]', search_sec=20, wait_sec=10) # 잡화 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 잡화 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("8 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_09_Daily_Necessity(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             self.interact_by_xpath('//android.widget.TextView[@text="생필품"]', search_sec=20, wait_sec=10) # 생필품 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 생필품 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("9 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_10_Sports(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=10) # 홈쇼핑모아 로고 클릭
    #             TCFG.driver.swipe(1173, 1399, 64, 1399, 10)  # 우측으로 스와이프
    #             sleep(2)
    #             self.interact_by_xpath('//android.widget.TextView[@text="스포츠"]', search_sec=20, wait_sec=10) # 스포츠 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 스포츠 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("10 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_11_Furniture(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             TCFG.driver.swipe(1173, 1399, 64, 1399, 10)  # 우측으로 스와이프
    #             sleep(2)
    #             self.interact_by_xpath('//android.widget.TextView[@text="가구"]', search_sec=20, wait_sec=10) # 가구 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 가구 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("11 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_12_Health(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             TCFG.driver.swipe(1173, 1399, 64, 1399, 10) # 우측으로 스와이프
    #             sleep(2)
    #             self.interact_by_xpath('//android.widget.TextView[@text="건강"]', search_sec=20, wait_sec=10) # 건강 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 건강 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("12 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_13_Travel(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             TCFG.driver.swipe(1173, 1399, 64, 1399, 10) # 우측으로 스와이프
    #             sleep(2)
    #             self.interact_by_xpath('//android.widget.TextView[@text="여행"]', search_sec=20, wait_sec=10) # 여행 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 여행 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("13 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_14_childbirth_and_childcare(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             TCFG.driver.swipe(1173, 1399, 64, 1399, 10) # 우측으로 스와이프
    #             sleep(2)
    #             self.interact_by_xpath('//android.widget.TextView[@text="출산⧸육아"]', search_sec=20, wait_sec=10) # 출산⧸육아 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 출산⧸육아 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False) # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("14 Passed")
    #             TCFG.is_passed = True
    #             break
    #
    # def test_15_Computer(self):
    #     for loop_count in range(0, TCFG.check_loop_count):
    #         try:
    #             self.interact_by_id('logo_btn', search_sec=30) # 홈쇼핑모아 로고 클릭
    #             TCFG.driver.swipe(1173, 1399, 64, 1399, 10) # 우측으로 스와이프
    #             sleep(2)
    #             self.interact_by_xpath('//android.widget.TextView[@text="컴퓨터"]', search_sec=20, wait_sec=10) # 컴퓨터 클릭
    #             self.interact_by_id('default_header_title', search_sec=20, click=False) # 컴퓨터 페이지 타이틀 노출 확인
    #             self.interact_by_xpath('//android.view.View[@text="추천순"]', search_sec=20, click=False)  # 추천순 버튼 노출 확인
    #             self.interact_by_xpath('//android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View[1]/android.view.View/android.view.View', search_sec=20, click=False) # 상품영역(상품의 이미지 및 정보) 노출 확인
    #             self.interact_by_id('default_header_back_button', search_sec=20) # 뒤로가기 버튼 클릭
    #         except:
    #             if loop_count == (TCFG.check_loop_count - 1):
    #                 print("Error!")
    #                 self.assertEqual(0, 1)
    #                 break
    #             self.exception('home')
    #         else:
    #             print("15 Passed")
    #             TCFG.is_passed = True
    #             break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Category)
	unittest.TextTestRunner(verbosity=2).run(suite)
