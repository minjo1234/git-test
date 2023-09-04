'''
import time
from selenium import webdriver  # selenium 패키지에서 webdriver 모듈을 가져온다 -> 웹 브라우저 제어
# selenium 패키지에서 by 모듈을 가져온다 -> 웹 요소를 식별
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# 웹 드라이버를 자동으로 다운로드 및 설치하는 데 사용되는 ChromeDriverManager 클래스를 가져옵니다.

options = webdriver.ChromeOptions()
# : Chrome 웹 브라우저의 옵션을 설정하기 위해 ChromeOptions 객체를 생성합니다.
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# Chrome 브라우저의 로깅을 비활성화하기 위해 "enable-logging" 스위치를 제외한 옵션을 설정합니다.
driver = webdriver.Chrome(options=options)
# 이전에 설정한 옵션을 사용하여 Chrome 웹 드라이버를 생성합니다. 옵션설정하고 Chrome 웹 드라이버를 사용한다 .
'''

import time
from selenium import webdriver  # selenium 패키지에서 webdriver 모듈을 가져온다 -> 웹 브라우저 제
from selenium.webdriver.common.by import By  # 웹 요소식별
from webdriver_manager.chrome import ChromeDriverManager  # 웹 드라이버를 자동으로 다운로드

options = webdriver.ChromeOptions()  # options
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # logging 생성
driver = webdriver.Chrome(options=options)  # Chrome에 options 설ㅈ어

try:
    driver.get('https://www.betman.co.kr/main/mainPage/gamebuy/closedGameSlipIFR.do?gmId=G101&gmTs=220011&gameDivCd=C&isIFR=Y')
    # 전체리스트
    gameMainArea = driver.find_element(
        by=By.CLASS_NAME, value='gameMainArea')
    # 내부 class
    tabList = driver.find_element(By.XPATH, '//*[@id="tabMenuDiv"]')
    tblArea_noLine = driver.find_element(By.XPATH, '//*[@id="div_gmBuySlip"]')
    tdb_gmButSlipList = driver.find_elements(
        By.XPATH, '//*[@id="tbd_gmBuySlipList"]')
    list = driver.find_elements(By.XPATH, '//*[@id="tbd_gmBuySlipList"]/tr[3]')
    print(type(list))
    time.sleep(5)
    for i in range(len(list)):
        db_fs11 = list[i].find_element(
            By.XPATH, '//*[@id="tbd_gmBuySlipList"]/tr[1]/td[3]/span[2]').text
        badge_gray = list[i].find_element(
            By.XPATH, '//*[@id="tbd_gmBuySlipList"]/tr[1]/td[4]/span').text
        scoreDiv_fwb = list[i].find_element(
            By.XPATH, '//*[@id="tbd_gmBuySlipList"]/tr[1]/td[5]/div').text
        formBox = list[i].find_element(
            By.CLASS_NAME, value='formBox').text
        fs11 = list[i].find_element(
            By.CLASS_NAME, value='fs11').text
        print('닉네임:{} 댓글:{} 추천수:{} 날짜:{} 닉네임:{} 닉네임:{} '.format(
            db_fs11, badge_gray, scoreDiv_fwb, formBox, fs11))
except Exception as e:
    print(e)
