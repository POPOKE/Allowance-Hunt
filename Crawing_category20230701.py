import requests
from bs4 import BeautifulSoup
import time
import re

url_list = []
subsidy_name_list = []
subsidy_list = []
result = {}
# 加入headers以偽裝我們的真實身分
headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36' }
#設定網址
url_baby = "https://www.gov.tw/News3_Content.aspx?n=2&s=375315"
url_baby1 = "https://www.gov.tw/News3_Content.aspx?n=2&s=381509"
url_lowincome_elder = "https://www.gov.tw/News3_Content.aspx?n=2&s=528880"
url_scholarship = "https://www.gov.tw/News3_Content.aspx?n=2&s=381247"
url_passaway = "https://www.gov.tw/News3_Content.aspx?n=2&s=371250"


url_list.append(url_baby)
url_list.append(url_baby1)
url_list.append(url_lowincome_elder)
url_list.append(url_scholarship)
url_list.append(url_passaway)


def crawling_subsidy(url):
    subsidy_list = []
    category_list = []
    response = requests.get(url , headers = headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find("div", class_= "simple-text title").getText()
    subsidy_name_list.append(titles)
    #利用findAll爬津貼頁面下方所有內容，然後用for迴圈＆getText取文字值就好
    for contents_test in soup.findAll("div", class_= "css-tr", limit = 2):
        subsidy_list.append(contents_test.getText(strip = True)) #把抓到的前兩項內容先取文字後,放在串列中
        result[titles] = subsidy_list  #把服務跟資格做成字典的value
    #name是津貼名稱, 指定進去
    name = titles

    
    if re.findall(r'育兒|兒童|生育|育嬰|幼兒|早期療育', name):
        category_list.append('birth')
    if re.findall(r'獎學金|獎助學金|就學|教育|學費', name):
        category_list.append('students')
    if re.findall(r'國民年金|勞工|勞保|就業|職業災害|職災|職保|就保|失業|工作', name):
        category_list.append('labor')
    if re.findall(r'弱勢|中低收入|中低老人|經濟弱勢|低收入戶', name):
        category_list.append('lowincome')
    if re.findall(r'身心障礙|身障', name):
        category_list.append('disabled')
    if re.findall(r'老人|老年', name):
        category_list.append('elder')
    if re.findall(r'修繕|租賃|住屋|房屋|租金|住宅|租屋|購屋', name):
        category_list.append('house')
    if re.findall(r'喪葬|死亡|身故', name):
        category_list.append('passaway')
        
    #服務內容這邊的資料等於content_1_p
    content_1_p = result[titles][0]
    #把標題跟內文用slice方式分開取用
    content_1_title = result[titles][0][0:4]
    content_1 = result[titles][0][4:]
    #申辦資格資料等於content_2_p
    content_2_p = result[titles][1]
    #把標題跟內文用slice方式分開取用
    content_2_title = result[titles][1][0:4]
    content_2 = result[titles][1][4:]
    #category是津貼種類, 指定進去,用join從category_list串列取出成字串
    print(name)
    category = ', '.join(category_list)
    print(category)
    #url是津貼網址, 指定進去
    url = url
    

# for u in url_list跑所有的網址
for u in url_list:
    crawling_subsidy(u)
