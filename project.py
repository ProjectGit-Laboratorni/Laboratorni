import sqlite3

# Створення або підключення до бази даних
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Створення таблиці, якщо вона не існує
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                  (id INTEGER PRIMARY KEY, amount REAL, category TEXT, date TEXT)''')

# Функція для додавання витрат
def add_expense(amount, category, date):
    cursor.execute('''INSERT INTO expenses (amount, category, date)
                      VALUES (?, ?, ?)''', (amount, category, date))
    conn.commit()

# Приклад використання функції
add_expense(50.0, 'їжа', '2025-01-30')
add_expense(20.0, 'транспорт', '2025-01-31')

# Закриття з'єднання з базою даних