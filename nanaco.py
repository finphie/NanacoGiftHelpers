from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import sys
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('number', type=int, help='nanaco番号')
parser.add_argument('password', help='パスワード')
parser.add_argument('gifts', nargs='+', help='ギフトID')

args = parser.parse_args()

driver = webdriver.Chrome('../chromedriver.exe')

# nanacoログインページに移動
driver.get('https://www.nanaco-net.jp/pc/emServlet')

# nanaco番号入力
element = driver.find_elements_by_name('XCID')[1]
element.send_keys(args.number)

# パスワード入力
element = driver.find_element_by_name('LOGIN_PWD')
element.send_keys(args.password)

# ログインボタンをクリック
element = driver.find_element_by_name('ACT_ACBS_do_LOGIN1')
element.click()

# ギフトID登録画面に移動
element = driver.find_element_by_css_selector('#gift > a')
element.click()

for gift in args.gifts:

    # 登録ボタンをクリック
    element = driver.find_element_by_xpath('//*[@id="register"]/form/p/input')
    element.click()

    # ギフトID入力画面に遷移
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
    gift_page_handle = driver.window_handles[1]
    driver.switch_to.window(gift_page_handle)

    # ギフトID入力
    print(gift, end='')
    element = driver.find_element_by_id('gift01')
    element.send_keys(gift[0:4])
    element = driver.find_element_by_id('gift02')
    element.send_keys(gift[4:8])
    element = driver.find_element_by_id('gift03')
    element.send_keys(gift[8:12])
    element = driver.find_element_by_id('gift04')
    element.send_keys(gift[12:16])
    element = driver.find_element_by_id('submit-button')
    element.click()

    # ギフトID登録
    try:
        element = driver.find_element_by_xpath('//*[@id="nav2Next"]/input[2]')
        element.click()
        print('...ok')
    except NoSuchElementException:
        print('...error')

    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# ログアウト
element = driver.find_element_by_css_selector('#logout > a')
element.click()

driver.quit()