from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

option = Options()
service = Service()
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://www.naver.com/")
