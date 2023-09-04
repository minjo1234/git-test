import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

try:
    driver.get('https://www.naver.com/')
    print('10:51')

    # 검색 입력창을 XPath로 찾기
    input_field = driver.find_element(
        By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/input')

    # 검색어 "후쿠오카"를 입력
    input_field.send_keys('후쿠오카')

    # 검색 결과가 나올 때까지 기다리기 (10초 동안 기다립니다)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="main_pack"]/section/div/div[2]/ul/li[1]/div/div[1]/a')))

    # 검색 결과 출력
    search_results = driver.find_elements(
        By.XPATH, '//*[@id="main_pack"]/section/div/div[2]/ul/li')
    for result in search_results:
        print(result.text)

except Exception as e:
    print('에러원인', e)
finally:
    driver.quit()  # 브라우저 종료
