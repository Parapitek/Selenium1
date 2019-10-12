import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#nums = open('p1.txt', 'r').read().splitlines()

driver = webdriver.Firefox(executable_path='C:/Temp/geckodriver.exe')
driver.get('https://nstu.ru')

a1 = driver.find_element_by_css_selector('a.header__login-link span')
time.sleep(1)
a1.click()
#actions = ActionChains(driver)
#actions.click(a1)

#actions.moveToElement(element).build().perform();

#driver.close()














































































































































'''import time
from selenium import webdriver
import unittest
driver = webdriver.Firefox(executable_path='C:/Temp/geckodriver.exe')

#time.sleep(5)

#driver.get("https://login.nstu.ru/ssoservice/XUI/#login/")
driver.get("https://vk.com")
time.sleep(5)
login_input = driver.find_element_by_id('index_email')
login_input.send_keys('glucanat@gmail.com')
password_input = driver.find_element_by_id('index_pass')
password_input.send_keys('***')
submit_btn = driver.find_element_by_id('index_login_button')
submit_btn.click()

f = open('p2.txt')
for line in f:
    print(line)

'''