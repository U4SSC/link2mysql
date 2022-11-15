import config
import pandas as pd
import pymysql
import pymysql.cursors

conn = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PASSWD, db=config.DB_NAME, cursorclass=pymysql.cursors.DictCursor)

def select_all(tablename:str):
    return pd.read_sql("SELECT * FROM `"+tablename+"`", conn)
#     with conn.cursor() as cursor:
#         sql = "SELECT * FROM `"+tablename+"`"
#         cursor.execute(sql)
#         return cursor.fetchall()

def find_user(username:str):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `user` WHERE `username` = %s"
        cursor.execute(sql, username)
        return cursor.fetchone()
