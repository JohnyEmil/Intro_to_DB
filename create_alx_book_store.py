import sqlite3

# إنشاء قاعدة البيانات
conn = sqlite3.connect("alx_book_store.db")
cursor = conn.cursor()

# الجداول
cursor.execute("""
CREATE TABLE IF NOT EXISTS Authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_name VARCHAR(215) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INTEGER NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215),
    address TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    quantity DOUBLE NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
)
""")

conn.commit()
conn.close()

print("✅ Database and tables created!")
