import sqlite3
import os
import pandas as pd

conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS expenses
                  (id INTEGER PRIMARY KEY, amount REAL, category TEXT, date TEXT)''')

def add_expense(info):

    info = str.split(info, " ")
    amount = info[0]
    category = info[1]
    date = info[2]

    cursor.execute('''INSERT INTO expenses (amount, category, date)
                      VALUES (?, ?, ?)''', (amount, category, date))
    conn.commit()


def all_expenses():

    cursor.execute('''SELECT * FROM expenses''')
    expense = cursor.fetchall()
    if len(expense) == 0:
        print("Таблиця порожня.")
    else:
        print(pd.DataFrame(expense, columns=['Номер витрати', 'Кількість', 'Куди', 'Дата']))
        input("Натисніть Enter.")


os.system("cls")

while True:

    x = input(str("Що ви хочете зробити?\n1 - Додати витрати\n2 - відобразити всі витрати\n9 - вийти\n0 - очистити таблицю\n"))

    if x == '1':
        a = input("Введіть ваши витрати: (Кількість, куди саме, дату у формати YYYY-MM-DD)")
        add_expense(a)
        os.system('cls')

    elif x == '2':
        all_expenses()
        os.system('cls')

    elif x == "9":
        break

    elif x == "0":

        print("Ви в цьому впевнені? (y - так, n - ні)")
        answer = input()

        if answer == 'y':
            cursor.execute("""DELETE FROM expenses""")
            conn.commit()
        if answer == 'n':
            pass

cursor.close()