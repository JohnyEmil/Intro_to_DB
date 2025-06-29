import mysql.connector
from mysql.connector import Error

try:
    # الاتصال بخادم MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='johny'
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # إنشاء قاعدة البيانات إذا لم تكن موجودة
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"❌ MySQL error: {err}")

finally:
    # غلق الاتصال
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")
