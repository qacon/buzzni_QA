from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
import pandas as pd

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
time.sleep(2) # 2초 대기
driver.maximize_window() # 브라우저 최대화

ele = driver.find_element(by=By.XPATH, value="//*[contains(text(),'쟁글 트렌딩')]") # 엘레멘트가 있는 곳까지 스크롤 다운
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
time.sleep(2)

# 로그인 페이지 이동
ele = driver.find_element(by=By.XPATH, value="//*[contains(text(),'로그인')]")
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
ele.click()

time.sleep(2)
ele = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Google 계정으로 시작')]")
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
ele.click()
time.sleep(2)

# 아이디 입력
driver.find_element(by=By.NAME, value='identifier').send_keys('jun@crossangle.io')
time.sleep(2)
ele = driver.find_element(by=By.XPATH, value="(//*[contains(@class, 'VfPpkd-RLmnJb')])[2]")
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
driver.execute_script("arguments[0].click();", ele)
# ele.click()
time.sleep(2)

# 비밀번호 입력
driver.find_element(by=By.NAME, value='password').send_keys('!tlgjatlf1')
ele = driver.find_element(by=By.XPATH, value="(//*[contains(@class, 'VfPpkd-RLmnJb')])[2]")
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
driver.execute_script("arguments[0].click();", ele)
time.sleep(2)
ele = driver.find_element(by=By.XPATH, value="//*[contains(text(),'쟁글 트렌딩')]")

# esc 누르기
pyautogui.press('esc')
time.sleep(2)

# 로그아웃 버튼 클릭
ele = driver.find_element(by=By.XPATH, value="//*[contains(text(),'로그아웃')]")
driver.execute_script("arguments[0].setAttribute('style',arguments[1]);", ele, "background: yellow; border: 2px solid red;")
ele.click()
time.sleep(10)

driver.close() # 페이지 닫기
print('웹 크롤링이 완료되었습니다.')

# ele = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'로그아웃')]")))