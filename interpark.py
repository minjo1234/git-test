import time
from selenium import webdriver  # 웹 브라우저 제어
from selenium.webdriver.common.by import By  # 웹 요소 식별
from webdriver_manager.chrome import ChromeDriverManager  # chromedriver 자동으로 설치

options = webdriver.ChromeOptions()  # options
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 로깅설정
driver = webdriver.Chrome(options=options)  # 연결 할 드라이버에 옵션 설정

try:
    like = input('���아요를 입력해주세요: ')
    url = f'http://isearch.interpark.com/isearch?q={like}'
    driver.get(url)

    time.sleep(3)

    print('test 9:45')
    # 순더대로 u_cbox_list -> comments -> u_nick

    searchList = driver.find_elements(by=By.CLASS_NAME, value='searchList')
    # find_element 메서드를 사용하여 by와 같이 요소를 식별해서 가져올수 있다 .
    goods = driver.find_elements(
        by=By.CLASS_NAME, value='goods')
    print(type(goods))

    result = []
    path = './data/interpark.txt'
    cmFile = open(path, mode='w', encoding='utf-8')
    for i in range(len(goods)):
        info = goods[i].find_element(
            By.CLASS_NAME, value='info').text
        priceArea = goods[i].find_element(
            By.CLASS_NAME, value='priceArea').text
        seller = goods[i].find_element(
            By.CLASS_NAME, value='seller').text
        print('닉네임:{} 댓글:{} 추천수:{}'.format(
            info, priceArea, seller))
        cmFile.write('닉네임:{} 댓글:{} 추천수:{} \n'.format(
            info, priceArea, seller))
    print('----------------------------')
    with open(path, mode='r', encoding='utf-8') as cmFile:
        file_contents = cmFile.read()
    print("파일 내용:")
    print(file_contents)
except Exception as ex:
    print('에러이유', ex)

print('-'*70)
print()
