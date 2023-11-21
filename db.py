import os
import pyodbc

server = os.getenv("SQL_SERVER")
database = os.getenv("SQL_DATABASE")
username = os.getenv("SQL_USER")
password = os.getenv("SQL_PASSWORD")
driver = os.getenv("SQL_DRIVER")

def exec_query(sql):
    data = ""
    with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            data = "|".join([column[0] for column in cursor.description])
            row = cursor.fetchone()
            i = 0
            while row:
                data += "\n" + "|".join([str(c) for c in row])
                row = cursor.fetchone()
                if i >= 10:
                    break
    return data