import requests
from bs4 import BeautifulSoup
import time

url_list = []
subsidy_name_list = []
subsidy_list = []
result = {}
# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
#設定網址
url_baby = "https://www.gov.tw/News3_Content.aspx?n=2&s=375315"
url_adopt = "https://www.gov.tw/News3_Content.aspx?n=2&s=371550&lep=8"


url_list.append(url_baby)
url_list.append(url_adopt)


def crawling_subsidy(url):
    subsidy_list=[]
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find("div", class_= "simple-text title").getText()

    subsidy_name_list.append(titles)
    #利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
    for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
        # print(contents_test)
        subsidy_list.append(contents_test.getText().replace('\n'," ")) #把抓到的前兩項內容先取文字後,放在串列中
    
    result[titles] = subsidy_list #把服務跟資格做成字典的value
    print(url)
    print(titles)
    print(subsidy_list[0])
    print(subsidy_list[1])

#for u in url_list跑所有的網址
for u in url_list:
    crawling_subsidy(u)
