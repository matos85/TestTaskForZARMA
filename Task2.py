# Обработка данных с использованием SQL
# Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age.
# Напишите Python-скрипт, который подключается к этой базе данных, выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

import sqlite3

def select_users_older_than_30(db_name):
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute("SELECT name, age FROM users WHERE age > 30")

        rows = cursor.fetchall()

        for row in rows:
            print(f"Name: {row[0]}, Age: {row[1]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

select_users_older_than_30("example.db")

