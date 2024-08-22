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
