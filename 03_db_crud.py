import pymysql
import prettytable

# 1. 連結MySQL
link=pymysql.connect(
    # (1) 透過 ngrok 連線
    # host="0.tcp.jp.ngrok.io",
    # user="root", 
    # passwd="", 
    # db="dbclasshw",
    # charset="utf8",
    # port=12632

    # (2) 本機連線
    host="localhost",
    user="root", 
    passwd="", 
    db="dbclasshw",
    charset="utf8",
    port=3306
)

table = 'member'
cur = link.cursor()  # 取得指令操作變數

# 2. 清單與 CRUD 的 function
# (1) 呈現清單
show_list = ["離開程式","顯示會員列表","新增會員資料","更新會員資料","刪除會員資料"]
def show_items():
    for i in range(len(show_list)):
        print(f"({i}) {show_list[i]}")

    n = input("指令:")
    try:
        n = int(n)
        if n in range(0,5):
            return n
        else:
            raise ValueError  # 強制停止並回報 ValueError 資訊
    except ValueError:
        return show_items()

# (2) 顯示會員列表
def show_data():
    p1 = prettytable.PrettyTable(["編號","姓名","生日","地址"], encoding="utf-8")
    p1.align["編號"] = "l"
    p1.align["姓名"] = "l"
    p1.align["生日"] = "l"
    p1.align["地址"] = "l"

    cur.execute(f"SELECT * FROM `{table}`")
    datas = cur.fetchall()

    for data in datas:
        p1.add_row([data[0], data[1], data[2], data[3]])

    print(p1)

# (3) 新增會員資料
def insert_data():
    data = [input("請輸入會員姓名:"), input("請輸入會員生日:"), input("請輸入會員地址:")]
    
    # 兩種寫法與 SQL injection 有關
    cur.execute(f"INSERT INTO {table}(name, birthday, address) VALUES('{data[0]}', '{data[1]}', '{data[2]}')")
    # cur.execute(f"INSERT INTO {table} (name, birthday, address) VALUES(%s,%s,%s)", data)

# (4) 更新會員資料
def update_data():
    show_data()
    data_id = input("請選擇你要修改的資料編號：")
    data = [input("請輸入會員姓名:"), input("請輸入會員生日:"), input("請輸入會員地址:")]
    
    # 兩種寫法與 SQL injection 有關
    cur.execute(f"UPDATE {table} SET name='{data[0]}' ,birthday='{data[1]}' ,address='{data[2]}' WHERE id={data_id}")
    # cur.execute(f"UPDATE {table} SET name=%s ,birthday=%s ,address=%s WHERE id={data_id}", data)

# (5) 刪除會員資料
def delete_data():
    show_data()
    data_id = input("請選擇你要刪除的資料編號：")
    cur.execute(f"DELETE FROM {table} WHERE id={data_id}")

# 3. 傳送SQL指令
while True:
    n = show_items()
    if n == 0:
        break
    elif n == 1:
        show_data()
    else:
        if n == 2:
            insert_data()
        elif n == 3:
            update_data()
        else:
            delete_data()

        link.commit() # 執行SQL指令

# 4. 關閉MySQL連線
link.close()
