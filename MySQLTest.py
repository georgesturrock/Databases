import mysql.connector
mysql.connector.connect(host='localhost',database='SalesOrdersExampleTest',user='root',password='rooter')

try:
    conn = mysql.connector.connect(host='localhost',database='SalesOrdersExampleTest',user='root',password='rooter')
    if conn.is_connected():
        print('Connected to MySQL database')

except Error as e:
    print(e)

finally:
    conn.close()
