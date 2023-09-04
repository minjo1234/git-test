import time
from selenium import webdriver  # 웹 브라우저 제어
from selenium.webdriver.common.by import By  # 웹 요소 식별
from webdriver_manager.chrome import ChromeDriverManager  # chromedriver 자동으로 설치

options = webdriver.ChromeOptions()  # options
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 로깅설정
driver = webdriver.Chrome(options=options)  # 연결 할 드라이버에 옵션 설정

try:
    like = input('���아요를 입력해주세요: ')
    url = f'https://section.blog.naver.com/Search/Post.naver?pageNo=1&rangeType=ALL&orderBy=sim&keyword={like}'
    driver.get(url)

    time.sleep(10)
except Exception as e:
    print('에러원인', e)
