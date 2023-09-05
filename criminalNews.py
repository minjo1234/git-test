import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from selenium import webdriver  # 웹 브라우저 식별
from selenium.webdriver.common.by import By  # 웹 요소 식별
from webdriver_manager.chrome import ChromeDriverManager  # 크롬브라우저 자동설치


options = webdriver.ChromeOptions()  # 옵션
options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 로깅
driver = webdriver.Chrome(options=options)  # 크롬 => 서버
driver.get('https://search.jtbc.co.kr/search/news?term=%EB%B2%94%EC%A3%84&type=vod')


urls = []

# url의 정보를 가져온다
# url의 정보를 가져오고 그 url의 정보를 href로 환산한다  .


def get_url():
    url_list = []
    for i in range(10):
        newsTitleXpath = '//*[@id="wrap"]/div[2]/div/div[2]/div[1]/main/div[3]/ul/li['+str(
            i+1)+']/div/a'

        title = driver.find_element(By.XPATH, newsTitleXpath)
        href = title.get_attribute('href')
        url_list.append(href)
    return url_list


for i in range(5):
    pageButton = driver.find_element(
        By.XPATH, '//*[@id="wrap"]/div[2]/div/div[2]/div[1]/main/div[4]/ul/li['+str(i+1)+']/a')
    pageButton.click()
    urls += get_url()


text_list = []
for url in urls:
    driver.get(url)
    wait = WebDriverWait(driver, 2)
    text = driver.find_element(By.XPATH, '//*[@id="articlebody"]/div[1]')
    text_list.append(text.text)

df = pd.DataFrame(text_list, columns=['text'])
df.to_csv('crawlingcrime.csv',  encoding='utf-8-sig')


#
#
