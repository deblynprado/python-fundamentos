import sqlite3

def openConnection():
  try :
    conn = sqlite3.connect('aula7.db')
    cursor = conn.cursor()
    return conn, cursor
  except sqlite3.Error as e:
    print('Cannot connect to database', e)
    return "None, execpt"

def closeConnection(conn) :
  conn.close()
  return "None, closed"

def createTable(cursor) :
  try:
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      price REAL NOT NULL
    )
  ''')
    return
  except sqlite3.Error as e:
    return('Cannot connect to database', e)
    
    
conn, cursor = openConnection();

createTable(cursor)

products =[
  ('Smartphone', 1500),
  ('Tablet', 800),
  ('Smartwatch', 400),
  ('Headphones', 200)
]

conn.executemany('''
  INSERT INTO products (name, price) VALUES (?, ?)
''', products)
conn.commit()

cursor.execute('SELECT * from products')
for product in cursor.fetchall() :
  print(product)
