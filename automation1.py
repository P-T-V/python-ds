import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
driver = webdriver.Chrome()
driver.get('https://www.youtube.com/')  # Go to YOUTUBE site
#  driver.get('https://yandex.ru/')
driver.maximize_window()

search_box = driver.find_element(By.XPATH, '//*[@id="search-form"]').find_element(By.CSS_SELECTOR, '#search')
search_box.send_keys('Lofi Girl')  # Finding search field & fill key

search_button = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
search_button.click()  # Finding search button & click

time.sleep(10)
driver.quit()
#  search_button =
