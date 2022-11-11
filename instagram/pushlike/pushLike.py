from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from loginInfo import InstaLogin
import time

options = webdriver.ChromeOptions()

options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://instagram.com')
driver.implicitly_wait(15)
print('접속완료')

def login() :
    btn= driver.find_elements(By.TAG_NAME, 'button')[1]
    btn.click()

    inputbox = driver.find_elements(By.TAG_NAME, 'input')[0]
    inputbox.click()
    driver.find_element(By.NAME,'username').send_keys(InstaLogin.INSTA_LOGIN_ID)

    inputbox = driver.find_elements(By.TAG_NAME, 'input')[1]
    inputbox.click()
    inputbox.send_keys(InstaLogin.INSTA_LOGIN_PW)

    inputbox.send_keys(Keys.ENTER)
    time.sleep(5)
    driver.implicitly_wait(15)
    print('로그인 완료')

def find_tag(insta_tag) :

    driver.get('https://www.instagram.com/explore/tags/{}/'.format(insta_tag))
    time.sleep(5)
    driver.implicitly_wait(15)
    print('태그 검색 완료')

    new_feed = driver.find_elements(By.XPATH, '//article//img //ancestor :: div[2]')[9]
    new_feed.click()

def push_like(like_cnt) :

    for i in range(like_cnt):
        driver.implicitly_wait(15)

        span = driver.find_element(By.XPATH, '//*[@aria-label="좋아요" or @aria-label="좋아요 취소"]//ancestor :: span[2]')
        like_btn = span.find_element(By.TAG_NAME, 'button')
        btn_svg = like_btn.find_element(By.TAG_NAME, 'svg')
        svg = btn_svg.get_attribute('aria-label')

        if svg == '좋아요' :
            like_btn.click()
            print('{} 좋아요를 눌렀습니다.'.format(i+1))
            time.sleep(1)
        else :
            print('{} 이미 좋아요를 눌렀습니다.'.format(i+1))
            time.sleep(1)

        if i < like_cnt-1 :
            next_feed_xpath = driver.find_element(By.XPATH, '//*[@aria-label="다음" and @height="16"]//ancestor :: div[2]')
            next_feed = next_feed_xpath.find_element(By.TAG_NAME, 'button')
            next_feed.click()
            time.sleep(3)

login()
find_tag('좋아요')
push_like(50)


print("프로그램을 종료합니다.")
driver.quit()