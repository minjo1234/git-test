
import time
from selenium import webdriver  # selenium 패키지에서 webdriver 모듈을 가져온다 -> 웹 브라우저 제
from selenium.webdriver.common.by import By  # 웹 요소식별
from webdriver_manager.chrome import ChromeDriverManager  # 웹 드라이버를 자동으로 다운로드
import pandas as pd  # pandas �����지

options = webdriver.ChromeOptions()  # options
options.add_experimental_option(
    "excludeSwitches", ["enable-logging"])  # logging 생성
driver = webdriver.Chrome(options=options)  # Chrome에 options 설ㅈ어
text_list = []
pathcsv = './betmandata/betman2020.csv'  # csv��일 경로
try:
    driver.get(
        'https://www.betman.co.kr/main/mainPage/gamebuy/gameSlipIFR.do?gmId=G101&gmTs=200001&gameDivCd=C&isIFR=Y')
    # 전체리스트
    gameMainArea = driver.find_element(
        by=By.CLASS_NAME, value='gameMainArea')
    # 내부 class
    tabList = driver.find_element(By.XPATH, '//*[@id="tabMenuDiv"]')
    tblArea_noLine = driver.find_element(By.XPATH, '//*[@id="div_gmBuySlip"]')
    tdb_gmButSlipList = driver.find_elements(
        By.XPATH, '//*[@id="tbd_gmBuySlipList"]')
    list = driver.find_elements(By.XPATH, '//*[@id="tbd_gmBuySlipList"]/tr[3]')
    print(type(list))
    time.sleep(5)
    index = driver.find_elements(By.XPATH, '//*[@id="tbd_gmBuySlipList"]')
    print(type(index))
    result = []
    # tr 태그를 가져옵니다.
    tr_elements = driver.find_elements(
        By.XPATH, '//*[@id="tbd_gmBuySlipList"]/tr')

# tr 태그의 개수를 세어 출력합니다.
    print(f'Total number of tr elements: {len(tr_elements)}')
    for i in range(len(tr_elements)):
        # 각 행에 대한 XPath 생성
        row_xpath = f'//*[@id="tbd_gmBuySlipList"]/tr[{i + 1}]'
        # //*[@id="tbd_gmBuySlipList"]/tr[{i+1}]
        # //*[@id="tbd_gmBuySlipList"]/tr[1]/td[3]/span[2]
        db_fs11 = driver.find_element(
            By.XPATH, row_xpath + f'/td[{3}]/span[{2}]').text
        # //*[@id="tbd_gmBuySlipList"]/tr[1]/td[3]/span[2]
        badge_gray = driver.find_element(
            By.XPATH, row_xpath + f'/td[{4}]/span').text
        # //*[@id="tbd_gmBuySlipList"]/tr[1]/td[4]/span
        scoreDiv_fwb = driver.find_element(
            By.XPATH, row_xpath + f'/td[{5}]/div').text
        # //*[@id="tbd_gmBuySlipList"]/tr[1]/td[5]/div
        formBox = driver.find_element(
            By.XPATH, row_xpath + f'/td[{6}]/div').text
        # //*[@id="tbd_gmBuySlipList"]/tr[1]/td[6]/div
        fs11 = driver.find_element(
            By.XPATH, row_xpath + f'/td[{7}]').text
        result.append([db_fs11, badge_gray, scoreDiv_fwb, formBox, fs11])
        n_table = pd.DataFrame(result, columns=(
            '2020' 'db_fs11', 'badge_gray', 'scoreDiv_fwb', 'formBox', 'fs11'))
        n_table_to_csv = n_table.to_csv(
            pathcsv, index=True, encoding='utf-8', mode='w')
# //*[@id="tbd_gmBuySlipList"]/tr[1]/td[7]
        print('리그: {} 경기: {} 경기결과 : {} 승,무,패: {}  경기일시:{} '.format(
            db_fs11, badge_gray, scoreDiv_fwb, formBox, fs11))


except Exception as e:
    print(e)
