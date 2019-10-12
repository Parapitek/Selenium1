import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path='C:/Temp/geckodriver.exe')
driver.get('https://www.nstu.ru/news/news_more?idnews=119966')

h1 = driver.find_element_by_css_selector('div.page-title>h1')
title = h1.text
div = driver.find_element_by_css_selector('.page-content>div:nth-child(5)')
text = div.text
print(title)
print(text)
driver.close()