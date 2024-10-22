# Создание БД, добавление, выбор и удаление элементов
# Задача "Первые пользователи":
import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')


def create_users():
    global cursor
    for i in range(10):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                       (f'User{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1) * 10}', '1_000'))


def balance_user():
    global cursor
    cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', ('500',))


def del_user():
    global cursor
    cursor.execute('DELETE FROM Users WHERE (id - 1) % 3 = 0')


def del_users():
    global cursor
    cursor.execute('DELETE FROM Users')


create_users()
balance_user()
del_user()
# del_users()
connection.commit()
connection.close()
