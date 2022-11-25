# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

# 테스트 15개 소요시간 : 약 40분
class Login(testModule):

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
        sleep(1)
        TCFG.driver.close_app()
        # TCFG.driver.terminate_app('com.buzzni.android.subapp.shoppingmoa')
        sleep(1)
        TCFG.driver.launch_app()
        sleep(1)
        try:
            self.interact_by_id('mid_popup_activity_stop_today_btn', search_sec=10) # 오늘은 그만보기 클릭
        except:
            pass
        try:
            self.interact_by_id('timeline_floating_banner_close_btn', search_sec=3) # 플로팅 배너 닫기 클릭
        except:
            pass

    def test_01_Home_Shopping(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                try:
                    self.interact_by_id('mid_popup_activity_stop_today_btn', search_sec=20) # 오늘은 그만보기 클릭
                except:
                    pass
                try:
                    self.interact_by_id('timeline_floating_banner_close_btn', search_sec=8) # 플로팅 배너 닫기 클릭
                except:
                    pass
                self.interact_by_id('filter_btn', search_sec=10) # 필터 버튼 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="홈&쇼핑"]', search_sec=10) # 홈&쇼핑 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=10) # 적용하기 클릭
                try:
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    except:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담⧸렌탈"]', search_sec=5, click=False) # 상담/렌탈일 경우 pass
                    print("1 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                    print("1 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                self.interact_by_xpath('//*[contains(@content-desc,"장바구니")]', search_sec=20, wait_sec=10) # 장바구니 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.view.View[@content-desc="로그인"]', search_sec=20) # 로그인 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text,"30일")]', search_sec=10) # 30일 동안 보지 않기 클릭
                except:
                    pass
                self.interact_by_xpath('//android.widget.Button[@text="내비게이션"]', search_sec=20, wait_sec=5) # 슬라이드 메뉴 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="주문/배송"]', search_sec=20, wait_sec=5, click=False) # 주문/배송 노출 확인
                TCFG.driver.swipe(12, 1237, 12, 600)
                sleep(3)
                TCFG.driver.swipe(12, 1237, 12, 600)
                sleep(3)
                TCFG.driver.swipe(12, 1237, 12, 600)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]/android.widget.TextView', search_sec=20) # 로그아웃 클릭
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
            except:
                if loop_count == TCFG.check_loop_count-1:
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("1 Passed")
                TCFG.is_passed = True
                break

    def test_02_CJ_OnStyle(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="CJ온스타일"]', search_sec=20) # CJ온스타일 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("2 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("2 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("2 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=10) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text,"모바일웹")]', search_sec=8) # 모바일웹에서 보기 클릭
                except:
                    pass
                TouchAction(TCFG.driver).tap(None, 660, 203, 1).perform() # 장바구니 클릭 클릭
                sleep(3)
                self.interact_by_xpath('//android.widget.CheckBox[@text="자동 로그인"]', search_sec=20) # 자동 로그인 해제
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 클릭
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="취소"]', search_sec=10) # 취소버튼 클릭
                except:
                    pass
                self.interact_by_xpath('//android.view.View[@content-desc="뒤로 가기"]', search_sec=20, wait_sec=10) # 뒤로가기 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="CJ ONSTYLE"]', search_sec=15) # 홈 버튼 클릭
                except:
                    self.interact_by_xpath('//*[contains(@content-desc, "홈으로")]', search_sec=10, wait_sec=10) # 홈으로 가기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=10, wait_sec=10) # 오늘 그만 보기 클릭
                except:
                    pass
                TouchAction(TCFG.driver).tap(None, 505, 1322, 1).perform() # 마이페이지 클릭
                sleep(15)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]/android.widget.TextView', search_sec=200, wait_sec=5) # 로그아웃 버튼 클릭
            except:
                if loop_count == TCFG.check_loop_count-1:
                    print("Error!")
                    self.assertEqual(0, 2)
                    break
            else:
                print("2 Passed")
                TCFG.is_passed = True
                break

    def test_03_Lotte_HomeShopping(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=10) # 필터 버튼 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="롯데홈쇼핑"]', search_sec=20) # 롯데홈쇼핑 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("3 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("3 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("3 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=10) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.Image[@text="icn-close-01-1"]', search_sec=60, wait_sec=10) # 혜택 닫기 버튼 클릭
                except:
                    pass
                try:
                    self.interact_by_xpath('//android.widget.Image[@text="icn-close-02-3"]', search_sec=5, wait_sec=10) # 팝업 닫기 버튼 클릭
                except:
                    pass
                try:
                    self.interact_by_xpath('//*[contains(@text,"오늘")]', search_sec=60, wait_sec=10) # 오늘은 그만보기 클릭
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc,"담겨있음")]', search_sec=5, wait_sec=60) # 장바구니 클릭
                # TouchAction(TCFG.driver).tap(None, 1334, 423, 1).perform() # 장바구니 클릭
                # sleep(2)
                # TouchAction(TCFG.driver).tap(None, 1334, 423, 1).perform() # 장바구니 클릭
                # sleep(2)
                # self.interact_by_xpath('//*[contains(@content-desc,"로그인")]', search_sec=60) # 로그인 클릭
                sleep(20)
                TouchAction(TCFG.driver).tap(None, 610, 359, 1).perform() # 로그인 클릭
                sleep(2)
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20, wait_sec=15) # 로그인 클릭
                self.interact_by_id('com.android.chrome:id/url_bar', search_sec=20, wait_sec=15) # url 클릭
                self.interact_by_id('com.android.chrome:id/url_bar', search_sec=20, send_keys_msg="https://m.lotteimall.com", click=False) # 홈 입력
                TouchAction(TCFG.driver).tap(None, 654, 1300, 1).perform() # 이동 클릭
                sleep(3)
                try:
                    self.interact_by_xpath('//*[contains(@text,"오늘")]', search_sec=10) # 오늘 그만 보기 클릭
                except:
                    pass
                try:
                    self.interact_by_xpath('//android.widget.Image[@text="icn-close-01-1"]', search_sec=10) # 팝업 닫기 클릭
                except:
                    pass
                self.interact_by_xpath('//android.view.View[@content-desc="마이롯데"]', search_sec=20, wait_sec=30) # 마이롯데 클릭
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃 로그아웃"]/android.widget.TextView', search_sec=20, wait_sec=4) # 로그아웃 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 3)
                    break
            else:
                print("3 Passed")
                TCFG.is_passed = True
                break

    def test_04_GS_SHOP(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                self.interact_by_xpath('(//android.widget.ImageView)[6]', search_sec=20) # GS SHOP 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("4 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("4 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("4 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘은")]', search_sec=20) # 오늘은 그만보기 클릭
                except:
                    pass
                try:
                    self.interact_by_xpath('//*[contains(@content-desc,"장바구니")]', search_sec=20, wait_sec=15) # 장바구니 클릭
                    self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="buzzni@buzzni.com", click=False) # 아이디 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="buzzni007!", click=False) # 비밀번호 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20) # 로그인 버튼 활성화
                    TouchAction(TCFG.driver).tap(None, 656, 1302, 1).perform() # 로그인 (이동 클릭)
                    sleep(2)
                    try:
                        self.interact_by_xpath('//*[contains(@content-desc,"30일")]', search_sec=10) # 30일 동안 보지 않기 클릭
                    except:
                        pass
                    try:
                        self.interact_by_xpath('//*[contains(@text, "7일간 안보기")]', search_sec=20) # 7일간 안보기 클릭
                    except:
                        pass
                except:
                    self.interact_by_xpath('(//android.view.View[@content-desc="상담신청"])[1]', search_sec=20) # 상담신청 클릭
                    self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
                    self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="buzzni@buzzni.com", click=False) # 아이디 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="buzzni007!", click=False) # 비밀번호 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20) # 로그인 버튼 활성화
                    TouchAction(TCFG.driver).tap(None, 656, 1302, 1).perform() # 로그인 (이동 클릭)
                    sleep(2)
                    try:
                        self.interact_by_xpath('//*[contains(@text, "7일간 안보기")]', search_sec=20) # 7일간 안보기 클릭
                    except:
                        pass
                    self.interact_by_xpath('//android.view.View[@content-desc="뒤로가기"]', search_sec=20) # 뒤로가기 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="마이쇼핑"]/android.widget.TextView', search_sec=20) # 마이쇼핑 클릭
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="7일간 안보기"]', search_sec=30) # 7일간 안보기 클릭
                except:
                    pass
                TCFG.driver.swipe(36, 1081, 36, 317)
                sleep(3)
                TCFG.driver.swipe(36, 1081, 36, 317)
                sleep(3)
                TouchAction(TCFG.driver).tap(None, 180, 748, 1).perform() # 로그아웃 클릭
                sleep(2)
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 4)
                    break
            else:
                print("4 Passed")
                TCFG.is_passed = True
                break

    def test_05_GongyoungShopping(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                self.interact_by_xpath('(//android.widget.ImageView)[7]', search_sec=20) # 공영쇼핑 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("5 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("5 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("5 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=20) # 오늘은 그만보기 클릭
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc,"장바구니")]', search_sec=20) # 장바구니 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="로그인"]/android.widget.TextView', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.view.View[@text="아이디 저장"]', search_sec=20) # 아이디 저장 해제
                self.interact_by_xpath('//android.view.View[@content-desc="로그인"]', search_sec=20) # 로그인 버튼 클릭
                self.interact_by_xpath('//android.widget.TextView[@text="로그아웃"]', search_sec=20, wait_sec=5) # 로그아웃 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 5)
                    break
            else:
                print("5 Passed")
                TCFG.is_passed = True
                break

    def test_06_NS_HomeShopping(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//android.widget.TextView[@text="NS홈쇼핑"]', search_sec=20) # NS홈쇼핑 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("6 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("6 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("6 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=10) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=20, wait_sec=10) # 오늘은 그만보기 클릭
                except:
                    pass
                TouchAction(TCFG.driver).tap(None, 671, 207, 1).perform() # 장바구니 클릭
                sleep(2)
                # self.interact_by_xpath('(//android.widget.Button)[4]', search_sec=20) # 장바구니 클릭
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 버튼 클릭
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="30일 후에 변경하기"]', search_sec=20) # 30일 후 변경하기 버튼 클릭
                except:
                    pass
                self.interact_by_xpath('//android.widget.Button[@text="쇼핑 계속하기"]', search_sec=20) # 쇼핑 계속하기 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="사이드메뉴"]', search_sec=200, wait_sec=10) # 사이드메뉴 클릭
                TCFG.driver.swipe(333, 1258, 333, 333)
                sleep(2)
                TCFG.driver.swipe(333, 1258, 333, 333)
                sleep(2)
                self.interact_by_xpath('//android.widget.Button[@text="로그아웃"]', search_sec=20, wait_sec=5) # 로그아웃 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="네"]', search_sec=20, wait_sec=5) # 네 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 6)
                    break
            else:
                print("6 Passed")
                TCFG.is_passed = True
                break

    def test_07_Shinsegae_TV_Shopping(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=200) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="신세계TV쇼핑"]', search_sec=20) # 신세계TV쇼핑 클릭
                except:
                    self.interact_by_xpath('//android.widget.TextView[@text="신세계라이브쇼핑"]', search_sec=20) # 신세계라이브쇼핑 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("7 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("7 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("7 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘은")]', search_sec=20) # 오늘은 그만보기 클릭
                except:
                    pass
                self.interact_by_xpath('//android.widget.Button[@text="장바구니"]', search_sec=20) # 장바구니 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="확인"]', search_sec=10) # 확인 클릭
                except:
                    pass
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni01", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.CheckBox[@text="아이디 저장"]', search_sec=20) # 아이디 저장 해제
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 버튼 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="마이쇼핑"]', search_sec=20) # 마이쇼핑 버튼 클릭
                TCFG.driver.swipe(36, 1081, 36, 317)
                sleep(3)
                TCFG.driver.swipe(36, 1081, 36, 317)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]/android.widget.TextView', search_sec=20, wait_sec=5) # 로그아웃 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 7)
                    break
            else:
                print("7 Passed")
                TCFG.is_passed = True
                break

    def test_08_KT_Alpha_Shopping(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "KT")]', search_sec=20) # KT알파 쇼핑 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("8 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("8 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("8 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=20) # 오늘 그만 보기 클릭
                    self.interact_by_xpath('//*[contains(@text, "닫기")]', search_sec=20) # 닫기 클릭
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc, "장바구니")]', search_sec=20) # 장바구니 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="로그인"]/android.widget.TextView', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 버튼 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="비밀 번호 변경 알림"]', search_sec=10, click=False) # 비밀 번호 변경 알림이 노출될 경우
                    TCFG.driver.swipe(217, 1660, 217, 1400, 10) # 하단으로 이동
                    sleep(3)
                    self.interact_by_xpath('//android.widget.TextView[@text="30일 후에 변경"]', search_sec=20) # 30일 후에 변경 버튼 클릭
                except:
                    try:
                        self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 버튼 클릭
                    except:
                        pass
                    try:
                        self.interact_by_xpath('//android.widget.Button[@text="다음에 동의할게요"]', search_sec=10) # 다음에 동의할게요 버튼 클릭
                        self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 버튼 클릭
                    except:
                        self.interact_by_xpath('//android.view.View[@content-desc="상품 둘러보기"]', search_sec=20) # 상품 둘러보기 버튼 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="카테고리"]/android.widget.TextView', search_sec=20, wait_sec=10) # 카테고리 버튼 클릭
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]', search_sec=200, wait_sec=5) # 로그아웃 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 8)
                    break
            else:
                print("8 Passed")
                TCFG.is_passed = True
                break

    def test_09_CJ_Onstyle_Plus(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "CJ온스타일")]', search_sec=20) # CJ온스타일 플러스 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("9 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("9 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("9 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=10) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text,"모바일웹")]', search_sec=8) # 모바일웹에서 보기 클릭
                except:
                    pass
                TouchAction(TCFG.driver).tap(None, 660, 203, 1).perform() # 장바구니 클릭 클릭
                sleep(3)
                self.interact_by_xpath('//android.widget.CheckBox[@text="자동 로그인"]', search_sec=20) # 자동 로그인 해제
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 클릭
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="취소"]', search_sec=10) # 취소버튼 클릭
                except:
                    pass
                self.interact_by_xpath('//android.view.View[@content-desc="뒤로 가기"]', search_sec=20, wait_sec=10) # 뒤로가기 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="CJ ONSTYLE"]', search_sec=15) # 홈 버튼 클릭
                except:
                    self.interact_by_xpath('//*[contains(@content-desc, "홈으로")]', search_sec=10, wait_sec=10) # 홈으로 가기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=10, wait_sec=10) # 오늘 그만 보기 클릭
                except:
                    pass
                TouchAction(TCFG.driver).tap(None, 505, 1322, 1).perform() # 마이페이지 클릭
                sleep(15)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                TCFG.driver.swipe(12, 1237, 12, 600) # 하단으로 이동
                sleep(2)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]/android.widget.TextView', search_sec=200, wait_sec=5) # 로그아웃 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 2)
                    break
            else:
                print("9 Passed")
                TCFG.is_passed = True
                break

    def test_10_Lotte_OneTV(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 900) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 900) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "롯데")]', search_sec=20) # 롯데OneTV 플러스 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("10 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("10 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("10 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=10) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.Image[@text="icn-close-01-1"]', search_sec=60, wait_sec=10) # 혜택 닫기 버튼 클릭
                except:
                    pass
                try:
                    self.interact_by_xpath('//android.widget.Image[@text="icn-close-02-3"]', search_sec=5, wait_sec=10) # 팝업 닫기 버튼 클릭
                except:
                    pass
                try:
                    self.interact_by_xpath('//*[contains(@text,"오늘")]', search_sec=60, wait_sec=10) # 오늘은 그만보기 클릭
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc,"담겨있음")]', search_sec=5, wait_sec=60) # 장바구니 클릭
                # TouchAction(TCFG.driver).tap(None, 1334, 423, 1).perform() # 장바구니 클릭
                # sleep(2)
                # TouchAction(TCFG.driver).tap(None, 1334, 423, 1).perform() # 장바구니 클릭
                # sleep(2)
                # self.interact_by_xpath('//*[contains(@content-desc,"로그인")]', search_sec=60) # 로그인 클릭
                sleep(20)
                TouchAction(TCFG.driver).tap(None, 610, 359, 1).perform() # 로그인 클릭
                sleep(2)
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력이
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20, wait_sec=15) # 로그인 클릭
                self.interact_by_id('com.android.chrome:id/url_bar', search_sec=20, wait_sec=15) # url 클릭
                self.interact_by_id('com.android.chrome:id/url_bar', search_sec=20, send_keys_msg="https://m.lotteimall.com", click=False) # 홈 입력
                TouchAction(TCFG.driver).tap(None, 654, 1298, 1).perform() # 이동 클릭
                sleep(3)
                try:
                    self.interact_by_xpath('//*[contains(@text,"오늘")]', search_sec=10) # 오늘 그만 보기 클릭
                except:
                    pass
                self.interact_by_xpath('//android.view.View[@content-desc="마이롯데"]', search_sec=20, wait_sec=30) # 마이롯데 클릭
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃 로그아웃"]/android.widget.TextView', search_sec=20, wait_sec=30) # 로그아웃 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 10)
                    break
            else:
                print("10 Passed")
                TCFG.is_passed = True
                break

    def test_11_GS_MY_SHOP(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "GS")]', search_sec=20) # GS MY SHOP 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("11 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("11 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("11 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@content-desc,"장바구니")]', search_sec=20, wait_sec=15) # 장바구니 클릭
                    self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="buzzni@buzzni.com", click=False) # 아이디 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="buzzni007!", click=False) # 비밀번호 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20) # 로그인 버튼 활성화
                    TouchAction(TCFG.driver).tap(None, 656, 1302, 1).perform() # 로그인 (이동 클릭)
                    sleep(2)
                    try:
                        self.interact_by_xpath('//*[contains(@content-desc,"30일")]', search_sec=10) # 30일 동안 보지 않기 클릭
                    except:
                        pass
                    try:
                        self.interact_by_xpath('//*[contains(@text, "7일간 안보기")]', search_sec=20) # 7일간 안보기 클릭
                    except:
                        pass
                except:
                    self.interact_by_xpath('(//android.view.View[@content-desc="상담신청"])[1]', search_sec=20) # 상담신청 클릭
                    self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
                    self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="buzzni@buzzni.com", click=False) # 아이디 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="buzzni007!", click=False) # 비밀번호 입력
                    self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20) # 로그인 버튼 활성화
                    TouchAction(TCFG.driver).tap(None, 656, 1302, 1).perform() # 로그인 (이동 클릭)
                    sleep(2)
                    try:
                        self.interact_by_xpath('//*[contains(@text, "7일간 안보기")]', search_sec=20) # 7일간 안보기 클릭
                    except:
                        pass
                    self.interact_by_xpath('//android.view.View[@content-desc="뒤로가기"]', search_sec=20) # 뒤로가기 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="마이쇼핑"]/android.widget.TextView', search_sec=20) # 마이쇼핑 클릭
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="7일간 안보기"]', search_sec=30) # 7일간 안보기 클릭
                except:
                    pass
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TouchAction(TCFG.driver).tap(None, 180, 748, 1).perform() # 로그아웃 클릭
                sleep(2)
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
            except:
                if loop_count == TCFG.check_loop_count - 1:
                    print("Error!")
                    self.assertEqual(0, 11)
                    break
            else:
                print("11 Passed")
                TCFG.is_passed = True
                break

    def test_12_Shopping_and_T(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "쇼핑엔T")]', search_sec=20) # 쇼핑엔T 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("12 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("12 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("12 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=5, click=False) # 오늘 그만 보기 클릭
                    TouchAction(TCFG.driver).tap(None, 423, 2411, 1).perform() # 오늘 그만 보기 클릭
                    sleep(1)
                except:
                    pass
                try:
                    self.interact_by_xpath('//*[contains(@text, "장바구니")]', search_sec=20) # 장바구니 클릭
                except:
                    self.interact_by_xpath('//*[contains(@content-desc, "장바구니")]', search_sec=20) # 장바구니 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20, wait_sec=10) # 로그인 버튼 클릭
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]', search_sec=20) # 로그아웃 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
            except:
                if loop_count == TCFG.check_loop_count - 1:
                    print("Error!")
                    self.assertEqual(0, 12)
                    break
            else:
                print("12 Passed")
                TCFG.is_passed = True
                break

    def test_13_SK_Store(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "SK스토아")]', search_sec=20) # SK스토아 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("13 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("13 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("13 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=5) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="오늘하루 그만보기"]/android.widget.TextView', search_sec=20) # 오늘하루 그만보기
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc, "장바구니")]', search_sec=20, wait_sec=10) # 장바구니 클릭
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=200, send_keys_msg="testbuzzni", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.CheckBox[@text="자동로그인"]', search_sec=20) # 자동로그인 해제
                self.interact_by_xpath('//android.view.View[@content-desc="로그인"]/android.widget.TextView', search_sec=20, wait_sec=10) # 로그인 버튼 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="다음에 변경하기"]/android.widget.TextView', search_sec=20) # 다음에 변경하기 클릭
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc, "SK stoa")]', search_sec=200) # SK stoa 클릭
                try:
                    self.interact_by_xpath('//android.view.View[@content-desc="오늘 하루 보지 않기"]/android.widget.TextView', search_sec=5) # 오늘 하루 보지 않기 클릭
                except:
                    pass
                self.interact_by_xpath('//android.view.View[@content-desc="마이페이지"]', search_sec=20) # 마이페이지 버튼 클릭
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]', search_sec=20) # 로그아웃 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 13)
                    break
            else:
                print("13 Passed")
                TCFG.is_passed = True
                break

    def test_14_NS_HomeShopping_ShopPlus(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "NS")]', search_sec=60) # NS홈쇼핑 샵플러스 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("14 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("14 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("14 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20, wait_sec=10) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=20, wait_sec=10) # 오늘은 그만보기 클릭
                except:
                    pass
                TouchAction(TCFG.driver).tap(None, 671, 207, 1).perform() # 장바구니 클릭
                sleep(2)
                # self.interact_by_xpath('(//android.widget.Button)[4]', search_sec=20) # 장바구니 클릭
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 버튼 클릭
                try:
                    self.interact_by_xpath('//android.widget.Button[@text="30일 후에 변경하기"]', search_sec=20) # 30일 후 변경하기 버튼 클릭
                except:
                    pass
                self.interact_by_xpath('//android.widget.Button[@text="쇼핑 계속하기"]', search_sec=20) # 쇼핑 계속하기 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="사이드메뉴"]', search_sec=200, wait_sec=10) # 사이드메뉴 클릭
                TCFG.driver.swipe(333, 1258, 333, 333)
                sleep(2)
                TCFG.driver.swipe(333, 1258, 333, 333)
                sleep(2)
                self.interact_by_xpath('//android.widget.Button[@text="로그아웃"]', search_sec=20, wait_sec=5) # 로그아웃 버튼 클릭
                self.interact_by_xpath('//android.widget.Button[@text="네"]', search_sec=20, wait_sec=5) # 네 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 14)
                    break
            else:
                print("14 Passed")
                TCFG.is_passed = True
                break

    def test_15_KT_Alpha_Shopping_TVPlus(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                self.exception('home')
                self.interact_by_id('filter_btn', search_sec=20) # 필터 버튼 클릭
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                TCFG.driver.swipe(78, 1079, 78, 822) # 다른 제휴사 보이도록 스와이프
                sleep(3)
                self.interact_by_xpath('//*[contains(@text, "KT")]', search_sec=20) # KT알파 쇼핑 TV플러스 클릭
                self.interact_by_id('timeline_filter_apply_button', search_sec=20) # 적용하기 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="방송 준비중입니다."]', search_sec=10, click=False) # 방송 준비중일 경우 pass
                    print("15 Passed")
                    TCFG.is_passed = True
                    break
                except:
                    try:
                        self.interact_by_id('timeline_live_child_small_bg', search_sec=10) # 첫번째상품 클릭
                    except:
                        self.interact_by_id('timeline_live_child_large_preview', search_sec=10) # 첫번째상품 클릭
                    try:
                        self.interact_by_xpath('//android.widget.TextView[@text="상담신청"]', search_sec=5, click=False) # 상담신청일 경우 pass
                        print("15 Passed")
                        TCFG.is_passed = True
                        break
                    except:
                        try:
                            self.interact_by_xpath('//*[contains(@text,"품절")]', search_sec=8, click=False) # 품절된 상품일 경우 pass
                            print("15 Passed")
                            TCFG.is_passed = True
                            break
                        except:
                            pass
                self.interact_by_id('product_detail_buy_button', search_sec=20) # 구매하기 클릭
                try:
                    self.interact_by_xpath('//*[contains(@text, "오늘")]', search_sec=20) # 오늘 그만 보기 클릭
                    self.interact_by_xpath('//*[contains(@text, "닫기")]', search_sec=20) # 닫기 클릭
                except:
                    pass
                self.interact_by_xpath('//*[contains(@content-desc, "장바구니")]', search_sec=20) # 장바구니 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="로그인"]/android.widget.TextView', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//android.widget.EditText)[1]', search_sec=20, send_keys_msg="testbuzzni@gmail.com", click=False) # 아이디 입력
                self.interact_by_xpath('(//android.widget.EditText)[2]', search_sec=20, send_keys_msg="choppa2017!", click=False) # 비밀번호 입력
                self.interact_by_xpath('//android.widget.Button[@text="로그인"]', search_sec=20) # 로그인 버튼 클릭
                try:
                    self.interact_by_xpath('//android.widget.TextView[@text="비밀 번호 변경 알림"]', search_sec=10, click=False) # 비밀 번호 변경 알림이 노출될 경우
                    TCFG.driver.swipe(217, 1660, 217, 1400, 10) # 하단으로 이동
                    sleep(3)
                    self.interact_by_xpath('//android.widget.TextView[@text="30일 후에 변경"]', search_sec=20) # 30일 후에 변경 버튼 클릭
                except:
                    try:
                        self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 버튼 클릭
                    except:
                        pass
                    try:
                        self.interact_by_xpath('//android.widget.Button[@text="다음에 동의할게요"]', search_sec=10) # 다음에 동의할게요 버튼 클릭
                        self.interact_by_xpath('//android.widget.Button[@text="확인"]', search_sec=20) # 확인 버튼 클릭
                    except:
                        self.interact_by_xpath('//android.view.View[@content-desc="상품 둘러보기"]', search_sec=20) # 상품 둘러보기 버튼 클릭
                self.interact_by_xpath('//android.view.View[@content-desc="카테고리"]/android.widget.TextView', search_sec=20, wait_sec=10) # 카테고리 버튼 클릭
                TCFG.driver.swipe(217, 1200, 217, 100)
                sleep(3)
                self.interact_by_xpath('//android.view.View[@content-desc="로그아웃"]', search_sec=200, wait_sec=5) # 로그아웃 버튼 클릭
            except:
                if loop_count == 0:
                    print("Error!")
                    TCFG.is_finished = True
                    self.assertEqual(0, 15)
                    break
            else:
                print("15 Passed")
                TCFG.is_finished = True
                TCFG.is_passed = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Login)
	unittest.TextTestRunner(verbosity=2).run(suite)