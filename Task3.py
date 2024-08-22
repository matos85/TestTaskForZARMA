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

