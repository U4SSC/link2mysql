import config
import pandas as pd
import pymysql
import pymysql.cursors
# ===============file_upload=====================
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
# Flask 單一檔案上傳
# ===============file_upload=====================

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
        if cursor.execute(sql, username) == 1:
            return cursor.fetchone()
        return False

def delete_data():
   with conn.cursor() as cursor:
        sql = "DELETE FROM `kpi_1`"
        cursor.execute(sql)
        conn.commit()
        return 

def insert_data(arr):
    with conn.cursor() as cursor:
        for col0 , col1 , col2 , col3 , col4 , col5 , col6 in arr:
            
            sql = """INSERT INTO `{table}` (`Country Name`, `Country Code`, `2010`, `2011`, `2012`, `2013`, `2014`) VALUES (%(col0)s, %(col1)s, %(col2)s, %(col3)s, %(col4)s, %(col5)s, %(col6)s)""".format(table="kpi_1")
            args = {
                "col0": col0,
                "col1": col1,
                "col2": col2,
                "col3": col3,
                "col4": col4,
                "col5": col5,
                "col6": col6
            }
            cursor.execute(sql, args)
            conn.commit()
        return 





# <form> 標籤裡的 enctype 屬性一定要填寫 multipart/form-data 才能上傳檔案。




