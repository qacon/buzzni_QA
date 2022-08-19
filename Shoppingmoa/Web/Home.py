from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def interact(by_type, name, wait_sec=2, click=True, send_keys_msg=None):
    if by_type == 'XPATH':
        if send_keys_msg == None:
            if click == True:
                ele = driver.find_element(by=By.XPATH, value=name)
                driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
                driver.execute_script("arguments[0].click();", ele)
            elif click == False:
                ele = driver.find_element(by=By.XPATH, value=name)
                driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
        else:
            driver.find_element(by=By.XPATH, value=name).send_keys(send_keys_msg)
        sleep(wait_sec)
    elif by_type == 'NAME':
        if send_keys_msg == None:
            if click == True:
                ele = driver.find_element(by=By.NAME, value=name)
                driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
                driver.execute_script("arguments[0].click();", ele)
            elif click == False:
                ele = driver.find_element(by=By.NAME, value=name)
                driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
        else:
            driver.find_element(by=By.NAME, value=name).send_keys(send_keys_msg)
        sleep(wait_sec)

url = 'https://hsmoa.com/'

# 사람처럼 보이게 하는 옵션들
options = webdriver.ChromeOptions()
options.add_argument('disable-gpu') # 가속(GPU) 사용 안함
options.add_argument('lang=ko_KR') # 언어 설정
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options) # 크롬 드라이버 설치

driver.implicitly_wait(30) # 웹페이지 전체가 로드 될때까지 기다린다.
driver.set_page_load_timeout(30)

driver.get(url) # url 이동
sleep(2) # 2초 대기
driver.maximize_window() # 브라우저 최대화

# 검색어 입력란 확인
interact(by_type="XPATH", name="//*[contains(@class, 'search-input')]")
# 검색어 입력
interact(by_type="NAME", name="query", click=False, send_keys_msg='마스크')
# 검색 클릭
interact(by_type="XPATH", name="//*[contains(@class, 'search-submit')]")
# 낮은가격순 클릭
interact(by_type="XPATH", name="//*[contains(@data-order, 'price asc')]", wait_sec=5)
# GS SHOP 클릭
interact(by_type="XPATH", name="//*[contains(@id,'gsshop')]", wait_sec=5)
# 첫번째 상품 클릭
interact(by_type="XPATH", name="//*[contains(@class, 'lazy')]", wait_sec=5)

# 브라우저 탭 객체를 리스트로 반환. [0] 은 인덱싱. 첫번재 탭을 의미
driver.window_handles[0]
# 두번째 탭으로 이동
driver.switch_to.window(driver.window_handles[1])

# 구매하기 클릭
interact(by_type="XPATH", name="//*[contains(@class,'gui-btn big red buy-button')]", wait_sec=5)
# 구매하기 클릭(옵션이 있을 경우 그냥 백그라운드에 구매하기를 클릭해서 로그인으로 넘어감)
interact(by_type="XPATH", name="//*[contains(@id,'btnDirectOrd')]", wait_sec=5)
# id입력란에 아이디 입력
interact(by_type="NAME", name="id", click=False, send_keys_msg='buzzni@buzzni.com')
# pw입력란 비밀번호 입력
interact(by_type="NAME", name="passwd", click=False, send_keys_msg='buzzni007!')
# 로그인 클릭
interact(by_type="XPATH", name="//*[contains(@id,'btnLogin')]", wait_sec=5)
# 장바구니 노출 확인
interact(by_type="XPATH", name="//*[contains(@class,'btn_goto_cart')]", wait_sec=10, click=False)

# 페이지2 닫기
driver.close()
# 첫번째 탭으로 이동
driver.switch_to.window(driver.window_handles[0])
# 페이지1 닫기
driver.close()
print('웹 크롤링이 완료되었습니다.')