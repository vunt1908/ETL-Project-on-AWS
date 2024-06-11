import mysql.connector
import pandas as pd

config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'port': '3306',
    'database': 'customer_data'
}

try:
    conn = mysql.connector.connect(**config)
    print("Kết nối thành công")
    
    cursor = conn.cursor()
    query = "SELECT * FROM customer"
    cursor.execute(query)
    
    df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
    
    cursor.close()
    conn.close()
    print("Đong kết nối")
    
    print(df.head())
    
except mysql.connector.Error as e:
    print("Lỗi kết nối:", e)
