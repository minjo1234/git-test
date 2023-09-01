from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

option = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=option)

try:
    driver.get('http://www.naver.com/')
except Exception as e:
    driver.get('https://www.google.com/')
