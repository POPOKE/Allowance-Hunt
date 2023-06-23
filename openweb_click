#可以打開網頁並點選申辦服務

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome() #用Chrome瀏覽器開網頁
driver.get("https://www.gov.tw/")
driver.find_element(By.LINK_TEXT, '申辦服務').click() #打開申辦服務超連結
