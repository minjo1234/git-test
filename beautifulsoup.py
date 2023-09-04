from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.edge.service import Service as EdgeService

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
# : Chrome 웹 브라우저의 옵션을 설정하기 위해 ChromeOptions 객체를 생성합니다.
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# Chrome 브라우저의 로깅을 비활성화하기 위해 "enable-logging" 스위치를 제외한 옵션을 설정합니다.
driver = webdriver.Chrome(options=options)

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)


def get_url():
    url_list = []
    for i in range(10):
        newsTitleXpath = '//*[@id="content"]/div[3]/div[1]/div[2]/ul/li[' + \
            str(i+1)+']/h3/a'
        title = driver.find_element_by_xpath(newsTitleXpath)
        href = title.get_attribute('href')
        url_list.append(href)
    return url_list


url = get_url()
urls = []
urls += get_url()

pageButton = driver.find_element_by_xpath(
    '//*[@id="content"]/div[3]/div[1]/div[2]/div/ul/li[4]/a')
pageButton.click()
urls += get_url()

pageButton = driver.find_element_by_xpath(
    '//*[@id="content"]/div[3]/div[1]/div[2]/div/ul/li[6]/a')
pageButton.click()
urls += get_url()

for i in range(10):
    pageButton = driver.find_element_by_xpath(
        '//*[@id="content"]/div[3]/div[1]/div[2]/div/ul/li[7]/a')
    pageButton.click()
    urls += get_url()


text_list = []
for url in urls:
    driver.get(url)
    wait = WebDriverWait(driver, 2)
    text = driver.find_element_by_xpath('//*[@id="articlebody"]/div[1]')
    text_list.append(text.text)

    import pandas as pd
df = pd.DataFrame(text_list, columns=['text'])

df.to_csv('crime.csv', encoding='utf-8-sig')
