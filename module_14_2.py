# Выбор элементов и функции в SQL запросах
# Задача "Средний баланс пользователя":
import sqlite3

connection = sqlite3.connect('not_telegram_2.db')
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
                       (f'User{i + 1}', f'example{i + 1}@gmail.com', f'{(i + 1) * 10}', '1000'))


def balance_user():
    global cursor
    cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', ('500',))


def del_user():
    global cursor
    cursor.execute('DELETE FROM Users WHERE (id - 1) % 3 = 0')


def del_users():
    global cursor
    cursor.execute('DELETE FROM Users')


def del_six():
    global cursor
    cursor.execute('DELETE FROM Users WHERE id = 6')


def count_users():
    global cursor
    cursor.execute('SELECT COUNT(*) FROM Users')
    return cursor.fetchone()[0]


def sum_users():
    global cursor
    cursor.execute('SELECT SUM(balance) FROM Users')
    return cursor.fetchone()[0]


def avg_balance():
    global cursor
    cursor.execute('SELECT AVG(balance) FROM Users')
    return cursor.fetchone()[0]


# create_users()
# balance_user()
# del_user()
del_six()
# del_users()
print(count := count_users())
print(balance := sum_users())
print(balance / count)
print(avg_balance())
connection.commit()
connection.close()
