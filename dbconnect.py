import config
import pymysql
import pymysql.cursors

conn = pymysql.connect(host=config.DB_HOST, port=config.DB_PORT, user=config.DB_USER, password=config.DB_PASSWD, db=config.DB_NAME)

def select_all(tablename:str):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM `"+tablename+"`"
        cursor.execute(sql)
        return cursor.fetchall()