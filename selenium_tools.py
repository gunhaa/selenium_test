import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import chromedriver_autoinstaller

# 자동으로 맞는 chromedriver를 다운로드 받아줌
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

## 1. navigation 관련 기능

# # get() 원하는 페이지로 이동
# driver.get("https://www.google.com/")
# time.sleep(2)
# driver.get("https://lol.inven.co.kr/")
# time.sleep(2)
# # back() 뒤로가기
# driver.back()
# time.sleep(2)

# # forward() 앞으로 가기
# driver.forward()
# time.sleep(2)

# # 새로 고침
# driver.refresh()
# time.sleep(2)

# print("동작 끝")

## 2. browser information

# driver.get("https://naver.co.kr/")
# time.sleep(2)

# # title ~ 웹 사이트의 타이틀을 가지고옴
# title = driver.title
# print(title, "|| this is title")
# # current_url 주소창을 그대로 가지고 옴
# current_url = driver.current_url
# print(current_url, "|| this is current_url")

# ## 예제 로직
# if "nid.naver.com" in current_url:
#     print("로그인 로직이 필요함")
# else:
#     print("내가 계획한 대로 무시하고 실행")


## 3. Driver wait
# time.sleep은 너무 비효율적임, 원할때 실행을 못함

# 모듈 import 필요
# 드라이버를 최대 n초 기다림, 만약 그 동안 처리가 안되면 오류가 throw됨
# 만약 3초때 로딩이 끝나서 element가 찾아진다면 다음 코드가 실행된다, 즉 끝나는 대로 실행되는 코드
# try expect로 사용하는게 좋다
driver.get("https://naver.co.kr/")
try:
    selector = "#account > div > a"
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selector)
    ))
    print("success")
except:
    print("exception throw")

print("next code execute")

input()