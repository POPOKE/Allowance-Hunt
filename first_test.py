################################打開FB,輸入帳密送出,OK!
from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome() #用Chrome瀏覽器開網頁
driver.get("https://www.facebook.com/")

email = driver.find_element("id","email")
password = driver.find_element("id","pass")

email.send_keys('example@gmail.com')
password.send_keys('*****')
password.submit() 
