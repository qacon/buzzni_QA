# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from TestModule import testModule
from Bootstrap import initialize_bp
from Bootstrap import TEST_CONFIG as TCFG

class Purchase_product(testModule):

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

    def test_01_CreditCard_Payment(self):
        for loop_count in range(0, TCFG.check_loop_count):
            try:
                # 데브앱 iOS 결제테스트 샘플(kb pay 앱 없이 결제)
                self.interact_by_id('홈', search_sec=20, click=False) # 홈 버튼 노출 확인
                self.interact_by_id('마이메뉴', search_sec=20) # 마이메뉴 클릭
                sleep(10)
                TCFG.driver.swipe(217, 676, 217, 127, 10)
                sleep(3)
                TCFG.driver.swipe(217, 472, 217, 689, 10)
                sleep(3)
                self.interact_by_id('커머스 상품 (dev용)', search_sec=7) # 커머스 상품(dev용) 클릭
                sleep(10)
                TouchAction(TCFG.driver).tap(None, 81, 151, 1).perform() # 입력창 클릭
                sleep(10)
                TouchAction(TCFG.driver).tap(None, 29, 789, 1).perform() # 숫자클릭
                sleep(3)
                TouchAction(TCFG.driver).tap(None, 25, 620, 1).perform() # 1 클
                sleep(1)
                TouchAction(TCFG.driver).tap(None, 100, 622, 1).perform() # 3 클
                sleep(1)
                TouchAction(TCFG.driver).tap(None, 264, 624, 1).perform() # 7 클
                sleep(1)
                TouchAction(TCFG.driver).tap(None, 100, 622, 1).perform() # 3 클
                sleep(1)
                TouchAction(TCFG.driver).tap(None, 371, 105, 1).perform()  # 검색 클릭
                sleep(1)
                self.interact_by_xpath('//XCUIElementTypeStaticText[@name="쵸파_테스트 자동화 상품"]', search_sec=20) # 쵸파_테스트 자동화 상품 클릭
                self.interact_by_xpath('//*[contains(@name, "바로구매")]', search_sec=20) # 바로구매 클릭
                self.interact_by_xpath('(//*[contains(@name, "바로구매")])[2]', search_sec=20) # 바로구매 클릭
                self.interact_by_xpath('//*[contains(@name, "결제하기")]', search_sec=20) # 결제하기 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="앱 없이 결제"]', search_sec=20) # 앱 없이 결제 클릭
                self.interact_by_id('휴대폰번호', search_sec=20, send_keys_msg="010-7513-6165", click=False) # 핸드폰 번호 입력
                self.interact_by_id('주민등록번호 앞 7자리', search_sec=20, send_keys_msg="910131-1", click=False) # 주민번호 입력
                self.interact_by_xpath('//XCUIElementTypeStaticText[@name="개인정보 수집이용 동의"]', search_sec=20) # 개인정보 수집이용 동의 체크
                self.interact_by_xpath('//*[contains(@name, "확인")]', search_sec=20) # 확인클릭
                self.interact_by_id('로그인', search_sec=20) # 로그인 클릭
                self.interact_by_xpath('(//XCUIElementTypeButton[@name="결제하기"])[2]', search_sec=20) # 결제하기 클릭
                # 비밀번호 클릭(KB페이의 경우 번호 버튼이 잡힘)
                self.interact_by_xpath('//XCUIElementTypeButton[@name="3"]', search_sec=20) # 3 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="1"]', search_sec=20) # 1 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="8"]', search_sec=20) # 8 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="2"]', search_sec=20) # 2 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="3"]', search_sec=20) # 3 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="1"]', search_sec=20) # 1 클릭
                self.interact_by_xpath('//*[contains(@name, "확인")]', search_sec=20) # 확인 버튼 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="주문 상세보기"]', search_sec=20) # 주문상세보기 버튼 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="주문취소"]', search_sec=20) # 주문 취소 버튼 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="다음"]', search_sec=20) # 다음 버튼 클릭
                self.interact_by_id('주문실수', search_sec=20) # 주문실수 버튼 클릭
                self.interact_by_xpath('//XCUIElementTypeCell[2]/XCUIElementTypeTextView', search_sec=20, send_keys_msg="주문취소 테스트입니다!!!", click=False) # 상세사유 입력
                self.interact_by_xpath('//XCUIElementTypeButton[@name="다음"]', search_sec=20) # 다음 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="취소요청"]', wait_sec=20, search_sec=10) # 취소요청 클릭
                self.interact_by_xpath('//XCUIElementTypeButton[@name="취소 상세보기"]', search_sec=20) # 취소 상세보기 클릭
                self.interact_by_xpath('//*[contains(@name, "취소완료")]', search_sec=20, click=False) # 취소완료 텍스트 노출 확인
            except:
                # if loop_count == (TCFG.check_loop_count-1):
                if loop_count == 0:
                    print("Error!")
                    self.assertEqual(0, 1)
                    break
                self.exception('home')
            else:
                print("1 Passed")
                TCFG.is_passed = True
                break

    def tearDown(self):
        if TCFG.is_finished:
            TCFG.driver.quit()
            TCFG.is_initialized=False

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Purchase_product)
	unittest.TextTestRunner(verbosity=2).run(suite)
