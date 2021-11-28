import sqlite3
from sqlite3 import Error

################################################################################
##################### tạo kết nối ##############################################
def create_connection(path): #kết nối tới database qua đường dẫn
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")

    #kiểm tra điều kiện connect thất bại. nếu thất bại thì connect lại
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection
connection = create_connection("GameDATA.db")
################################################################################
####################### Tạo bảng ###############################################
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
#################################################################################
######################## Tạo bảng dữ liệu #######################################
#Tạo bảng người chơi
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id_Users INTEGER PRIMARY KEY AUTOINCREMENT,
  playerName TEXT NOT NULL,
  playerMoney INTEGER,
  playerWinNum INTEGER,
  playerBINGO INTEGER,
  map1 BOOL,
  map2 BOOL,
  map3 BOOL,
  map4 BOOL,
  map5 BOOL
);
"""
execute_query(connection, create_users_table)  

#Tao bang cua hang
create_shops_table = """
CREATE TABLE IF NOT EXISTS shops (
  id_Shops INTEGER PRIMARY KEY AUTOINCREMENT,
  playerName TEXT NOT NULL,
  goods TEXT NOT NULL,
  bought BOOL, 
  cost INTEGER,
  FOREIGN KEY (playerName) REFERENCES users(playerName)
);
"""
execute_query(connection, create_shops_table)  

#############################################################################
############################## Hàm nhập dữ liệu vào table ###################
    #Dữ liệu cho player
def inputTable_user(playerName_v, playerMoney_v, playerWinNum_v, playerBINGO_v, map1_v, map2_v, map3_v, map4_v, map5_v):
    
    connection = create_connection("GameDATA.db")
    connection.execute("INSERT INTO users (playerName, playerMoney, playerWinNum, playerBINGO, map1, map2, map3, map4, map5) VALUES (:playerName_v, :playerMoney_v, :playerWinNum_v, :playerBINGO_v, :map1_vv, :map2_vv, :map3_vv, :map4_vv, :map5_vv)",
      {
        'playerName_v' : playerName_v,
        'playerMoney_v': playerMoney_v, 
        'playerWinNum_v': playerWinNum_v, 
        'playerBINGO_v': playerBINGO_v, 
        'map1_vv' : map1_v, 
        'map2_vv' : map2_v, 
        'map3_vv' : map3_v, 
        'map4_vv' : map4_v, 
        'map5_vv' : map5_v
      })
    connection.commit()
    #dữ liệu cho cửa hàng (shops)
def inputTable_shop(playerName_v, goods_v, bought_v, cost_v):
        
    connection = create_connection("GameDATA.db")
    connection.execute("INSERT INTO shops (playerName, goods, bought, cost) VALUES (:playerName_v, :goods_v, :bought_v, :cost_v)",
      {
        'playerName_v' : playerName_v,
        'goods_v' : goods_v,
        'bought_v':bought_v,
        'cost_v':cost_v
      })
    connection.commit()
#########################################################################
########################### đọc dữ liệu #################################
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
#########################################################################
############ Đọc dữ liệu Tiền và Tên người dùng #########################
def selectMoneyAndName(playerID_v,playerName_v, playerMoney_v):
    connection = create_connection("GameDATA.db")
    select_users = "SELECT id_Users, playerName, playerMoney, playerWinNum, playerBINGO, map1, map2, map3, map4, map5 from users"
    users = execute_read_query(connection, select_users)
    for user in users:

        playerID_v.append(user[0])# 0 to 1 1 to 2 2 to 3.... (list index to ID) ==> ID = list index + 1
        playerName_v.append(user[1])
        playerMoney_v.append(user[2])
        
#########################################################################
################### Cập nhật tiền #######################################
def changeDataMoney(playerID_v, playerMoney_v):
    connection = create_connection("GameDATA.db")
    cursor = connection.cursor()
    cursor.execute("UPDATE users set playerMoney = :playerMoney_v where id_Users = :playerID_v", {'playerMoney_v' : playerMoney_v, 'playerID_v':playerID_v})
    connection.commit()
#def changeDataMoney(playerID_v, playerMoney_v):
#    connection = create_connection("GameDATA.db")
#    cursor = connection.cursor()
#    cursor.execute("UPDATE users set playerMoney = :playerMoney_v where id_Users = :playerID_v", {'playerMoney_v' : playerMoney_v, 'playerID_v':playerID_v})
#    print(playerID_v)
#    print(playerMoney_v)
#########################################################################
################# Cập nhật map 1#########################################
def changeTFMap1(playerID_v):
    connection = create_connection("GameDATA.db")
    cursor = connection.cursor()
    map1_v = True
    cursor.execute("UPDATE users set map1 = :map1_v where id_Users = playerID_v", {'map1_v' : map1_v, 'playerID_v':playerID_v})
################# Cập nhật map 2#########################################
def changeTFMap1(playerID_v):
    connection = create_connection("GameDATA.db")
    cursor = connection.cursor()
    map1_v = True
    cursor.execute("UPDATE users set map2 = :map2_v where id_Users = playerID_v", {'map2_v' : map2_v, 'playerID_v':playerID_v})




