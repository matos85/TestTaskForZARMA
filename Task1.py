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
