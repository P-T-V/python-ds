import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase


browser = webdriver.Chrome()

browser.maximize_window()
browser.get('https://www.microsoft.com/ru-ru/')
# self.browser.implicitly_wait(10)
#  forBusiness = browser.find_element(By.XPATH, '//*[@id="primaryArea"]/div/div[6]/div/div/div/div/div[2]/section/div/'
#                'div[2]').find_element(By.XPATH, '//*[@id="primaryArea"]/div/div[6]/div/div/div/div/div[2]/section/div/'
#                                                 'div[2]/div/div[2]/div/a').click()
#
#  browser.get('https://www.microsoft.com/ru-ru/')
#  surfaceOption = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div/header/div/div/nav/ul/li[2]/a')
#  surfaceOption = browser.find_element(By.XPATH, '//*[@id="uhf-g-nav"]/ul/li[2]').find_element(By.ID, 'shellmenu_1')
# surfaceOption = browser.find_element(By.XPATH, '//*[@id="headerUniversalHeader"]/header/div/div/div[2]/div[1]').\
#     find_element(By.CSS_SELECTOR, '#uhf-c-nav > ul > li > div > button').click()
# surfaceOption2 = browser.find_element(By.XPATH, '//*[@id="uhf-c-nav"]/ul/li/div/ul/li[5]/ul/li[2]').find_element(
#     By.ID, 'shellmenu_24')
#  surfaceOption2.click()
surfaceOption3 = browser.find_element(By.ID, 'shellmenu_24')
surfaceOption3.click()

time.sleep(10)

browser.quit()
