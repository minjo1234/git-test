from bs4 import BeautifulSoup
import time
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
