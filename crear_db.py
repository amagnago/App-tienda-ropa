import sqlite3

conn = sqlite3.connect('tienda_ropa.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS prendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                tipo TEXT NOT NULL,
                talle TEXT NOT NULL,
                color TEXT,
                precio REAL
            )''')

conn.commit()
conn.close()