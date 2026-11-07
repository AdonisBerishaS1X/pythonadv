import sqlite3
from ctypes import create_unicode_buffer

connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
''')
connection.commit()

cursor.execute('''
INSERT INTO employees(name,position,department,salary)
VALUES(?,?,?,?)
''',('John Doe','Waste Management','Waste',1500))
connection.commit()

cursor.execute('''
INSERT INTO employees(name,position,department,salary)
VALUES(?,?,?,?)
''',('Anthony Soprano','Waste Management','Waste',15000))
connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
UPDATE employees
SET salary = ?
WHERE name = ?
''',('150000','Anthony Soprano')


)

connection.commit()

cursor.execute('''
DELETE FROM employees
WHERE name = ?
'''('Anthony Soprano',)
)

connection.commit()

cursor.close()
connection.close()