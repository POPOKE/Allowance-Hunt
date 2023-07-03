import pymysql
import re


#資料庫連線設定
db = pymysql.connect(host='0.tcp.jp.ngrok.io', port=14080, user='root', passwd='0624', db='fastapi', charset='utf8')
#建立操作游標
cursor = db.cursor()
#SQL語法


sql = "INSERT INTO info(serial_no, name, category, organization_name, url, content, condition_list) VALUES (%s, %s, %s, %s, %s, %s ,%s)"      
update_subsidy = "UPDATE info SET serial_no = %s, category = %s, organization_name = %s, url = %s, content = %s, condition_list = %s WHERE name = %s"

f = open('crawling_result.txt','r', encoding="utf-8")

while True:
    try:
        serial_no = f.readline()
        name = f.readline()
        category = f.readline()
        organization_name = f.readline()
        content = f.readline()
        condition_list = f.readline()
        url = f.readline()
        new_data = (serial_no, name, category, organization_name, url, content, condition_list)
        cursor.execute(sql, new_data)
    #提交修改
        db.commit()
        print('success')

    except EOFError:
        break
        
#發生錯誤時停止執行SQL
    except Exception as e:
        db.rollback()
        if  re.search(r'Duplicate entry', str(e)):
            update_subsidy = "UPDATE info SET serial_no = %s, category = %s, organization_name = %s, url = %s, content = %s, condition_list = %s WHERE name = %s"
            values = (serial_no, name, category, organization_name, url, content, condition_list)
            cursor.execute(update_subsidy, values)
            db.commit()
            print('update')
            continue
        else:   
            print('error')
            print(e)
            break

#關閉連線
db.close()
