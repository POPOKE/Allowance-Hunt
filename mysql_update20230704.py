import pymysql
import re

# 資料庫連線設定
db = pymysql.connect(host='linebot-subsidy-mysql.fly.dev', port=3306, user='guest', passwd='theflymysql', db='Allowance_Master', charset='utf8')
# 建立操作游標
cursor = db.cursor()
# SQL語法

# 新增資料語法insertinto
sql = "INSERT INTO AllowanceDetails(serial_no, name, category, organization_name, url, content, condition_list) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# 開啟更新檔(記得修改檔案的相對路徑)
f = open('crawling_result.txt', 'r', encoding="utf-8")

while True:
    try:
        line = f.readline().strip()  #消除換行
        if line == "":
            break
        else:
            serial_no = line
            name = f.readline().strip()
            category = f.readline().strip()
            organization_name = f.readline().strip()
            content = f.readline().strip()
            condition_list = f.readline().strip()
            url_ = f.readline().strip()
            new_data = (serial_no, name, category, organization_name, url_, content, condition_list)
            cursor.execute(sql, new_data)  # 執行指令
            db.commit()  # 提交至SQL指令
            print('success')

# 發生錯誤時停止執行SQL
    except Exception as e:
        db.rollback()
        if re.search(r'Duplicate entry', str(e)):
            update_subsidy = "UPDATE AllowanceDetails SET serial_no = %s, category = %s, organization_name = %s, url = %s, content = %s, condition_list = %s WHERE name = %s"
            values = (serial_no, category, organization_name, url_, content, condition_list, name)
            cursor.execute(update_subsidy, values)
            db.commit()
            print('update')
            continue
        else:
            print('error')
            print(e)
            break

# 關閉連線
db.close()

