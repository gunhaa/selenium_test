import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

# 자동으로 맞는 chromedriver를 다운로드 받아줌
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 주소창을 controll하는 함수
driver.get("https://www.google.com")

time.sleep(3)

# Selector를 통한 요소 선택
# selector = "body > div.L3eUgb > div:nth-child(6) > div > div.KxwPGc.SSwjIe"
selector = "body > div.L3eUgb > div:nth-child(6) > div > div.KxwPGc.SSwjIe > div.KxwPGc.AghGtd > a:nth-child(3)"
groupt_navigation = driver.find_element(By.CSS_SELECTOR, selector)

# 요소 내 모든 정보 출력
print(groupt_navigation.text)

# 클릭(가운데 부분이 클릭됨)
groupt_navigation.click()
# 요소를 클릭하기(액션)
input()