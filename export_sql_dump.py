import sqlite3

conn = sqlite3.connect("alx_book_store.db")

with open("alx_book_store.sql", "w") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")

conn.close()

print("✅ Dump saved to alx_book_store.sql")
