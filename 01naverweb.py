
import time
from selenium  import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome  import ChromeDriverManager

options = webdriver.ChromeOptions( )
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

try:
    print('test 9:45')
    driver.get('https://comic.naver.com/webtoon/detail?titleId=769209&no=84')
    # https://comic.naver.com/webtoon/detail?titleId=769209&no=84
    # https://comic.naver.com/webtoon/detail?titleId=774866&no=102 
    time.sleep(5)

except Exception as ex:
   print('에러이유 ' , ex)

print('- ' * 50)
print()         