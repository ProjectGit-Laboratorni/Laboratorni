import sqlite3

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                  (id INTEGER PRIMARY KEY, amount REAL, category TEXT, date TEXT)''')

def add_expense(amount, category, date):
    cursor.execute('''INSERT INTO expenses (amount, category, date)
                      VALUES (?, ?, ?)''', (amount, category, date))
    conn.commit()

add_expense(50.0, 'їжа', '2025-01-30')
add_expense(20.0, 'транспорт', '2025-01-31')

cursor.execute('''SELECT * FROM expenses''')
expense = cursor.fetchall()
for i in expense:
    print(i)
# Закриття з'єднання з базою даних
cursor.close()
