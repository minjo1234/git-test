from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)

try:
    # 네이버 메인 페이지로 이동
    driver.get("https://www.naver.com")

    # 네이버 메뉴에서 '식품' 클릭
    driver.find_element(
        'xpath', '//*[@id="query"]').click()

    # 가을 제철 식품 페이지로 이동
    driver.find_element(
        'xpath', '//*[@id="content"]/div/div[2]/div/div[1]/div/div/ul[2]/li[6]/a').click()

    # 원하는 주제를 크롤링하기 위해 필요한 코드를 작성하세요.
    # 예를 들어, 가을 제철 식품 페이지에서 데이터를 수집하고 출력하는 코드를 추가할 수 있습니다.

    # 페이지의 HTML을 가져오기
    page_source = driver.page_source

    # 여기에 데이터 수집 및 처리 코드를 추가하세요.ㅂ

except Exception as e:
    print(f"예외 발생: {str(e)}")

finally:
    # WebDriver 종료
    driver.quit()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
