# TestTaskForZARMA


Задача 1
_______

# Подключение к API и получение данных
# Напишите скрипт на Python, который подключается к API и получает данные.
# Например, используйте публичное API https://jsonplaceholder.typicode.com/posts.
# Сохраните полученные данные в формате JSON в файл.

import requests
import json

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def save_data_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

api_url = "https://jsonplaceholder.typicode.com/posts"
data = fetch_data_from_api(api_url)

if data is not None:
    save_data_to_json(data, "posts.json")

_______

Задача 2
________

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

________

Задача 3 
________

# Объединение данных из разных источников
# Напишите скрипт на Python, который объединяет данные из двух источников.
# Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name).
# Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount).
# Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах для каждого продукта.

import csv
import json


def read_csv(filepath):
    products = {}
    try:
        with open(filepath, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products[row['product_id']] = row['product_name']
    except IOError as e:
        print(f"Error reading CSV file: {e}")
    return products


def read_json(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []


def merge_data(products, sales):
    merged_data = []
    for sale in sales:
        product_id = sale['product_id']
        if product_id in products:
            merged_data.append({
                'product_name': products[product_id],
                'amount': sale['amount']
            })
    return merged_data


def main():
    products = read_csv('products.csv')
    sales = read_json('sales.json')
    merged_data = merge_data(products, sales)

    print("Sales Information:")
    for data in merged_data:
        print(data)


main()

____
Скрипт создания файлов для объединения:
import csv

# Данные для products.csv
products_data = [
    {'product_id': '1', 'product_name': 'Laptop'},
    {'product_id': '2', 'product_name': 'Smartphone'},
    {'product_id': '3', 'product_name': 'Tablet'}
]

# Создание файла и запись данных
with open('products.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['product_id', 'product_name'])
    writer.writeheader()
    writer.writerows(products_data)

print("Файл products.csv был успешно создан.")

import json

# Данные для sales.json
sales_data = [
    {'product_id': '1', 'amount': 5},
    {'product_id': '2', 'amount': 10},
    {'product_id': '3', 'amount': 7}
]

# Создание файла и запись данных
with open('sales.json', mode='w') as file:
    json.dump(sales_data, file, indent=4)

print("Файл sales.json был успешно создан.")

____
________

Задача 4
________
# Оптимизация скрипта
# Дан следующий скрипт на Python для обработки списка чисел.
# Оптимизируйте его для повышения производительности.
#
# numbers = [i for i in range(1, 1000001)]
# squares = []
# for number in numbers:
#     squares.append(number ** 2)

squares = [number ** 2 for number in range(1, 1000001)]



________
