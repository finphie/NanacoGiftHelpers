from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('number', type=int, help='nanaco番号')
parser.add_argument('password', help='パスワード')
parser.add_argument('gifts', nargs='+', help='ギフトID')

args = parser.parse_args()

with webdriver.Chrome('../chromedriver.exe') as driver:

    # 要素が見つかるまで10秒待機
    driver.implicitly_wait(10)

    # nanacoログインページに移動
    driver.get('https://www.nanaco-net.jp/pc/emServlet')

    # nanaco番号入力
    driver.find_elements_by_name('XCID')[1].send_keys(args.number)

    # パスワード入力
    driver.find_element_by_name('LOGIN_PWD').send_keys(args.password)

    # ログインボタンをクリック
    driver.find_element_by_name('ACT_ACBS_do_LOGIN1').click()

    # ギフトID登録画面に移動
    driver.find_element_by_css_selector('#gift > a').click()

    for gift in args.gifts:

        # 登録ボタンをクリック
        driver.find_element_by_xpath('//*[@id="register"]/form/p/input').click()

        # ギフトID入力画面に遷移
        WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
        gift_page_handle = driver.window_handles[1]
        driver.switch_to.window(gift_page_handle)

        # ギフトID入力
        print(gift, end='')
        driver.find_element_by_id('gift01').send_keys(gift[0:4])
        driver.find_element_by_id('gift02').send_keys(gift[4:8])
        driver.find_element_by_id('gift03').send_keys(gift[8:12])
        driver.find_element_by_id('gift04').send_keys(gift[12:16])
        driver.find_element_by_id('submit-button').click()

        # ギフトID登録
        try:
            driver.find_element_by_xpath('//*[@id="nav2Next"]/input[2]').click()
            print('...ok')
        except NoSuchElementException:
            print('...error')

        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # ログアウト
    driver.find_element_by_css_selector('#logout > a').click()