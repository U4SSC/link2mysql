import config
import pandas as pd
import pymysql
import pymysql.cursors

conn = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PASSWD, db=config.DB_NAME)

def select_all(tablename:str):
    return pd.read_sql("SELECT * FROM `"+tablename+"`", conn)
#     with conn.cursor() as cursor:
#         sql = "SELECT * FROM `"+tablename+"`"
#         cursor.execute(sql)
#         return cursor.fetchall()