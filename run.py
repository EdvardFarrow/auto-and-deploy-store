import os 
import pandas as pd
import re
import configparser
from pgdb import PGDatabase
import psycopg2 

# Чтение конфигурационного файла
config = configparser.ConfigParser()
config.read('config.ini')

# Получаем путь к директории и паттерн для файлов
sales_path_pattern = config.get('Paths', 'sales_path_pattern')
directory = config.get('Paths', 'directory')

# Преобразуем регулярное выражение в объект регулярного выражения
sales_path_regex = re.compile(sales_path_pattern)

# Обработка файлов в директории
for filename in os.listdir(directory):
    # Если файл соответствует регулярному выражению
    if sales_path_regex.match(filename):
        file_path = os.path.join(directory, filename)
        
        # Проверяем, существует ли такой файл
        if os.path.exists(file_path):
            # Читаем CSV в DataFrame
            sales_df = pd.read_csv(file_path)
            print(f"Файл: {filename}")
            print(sales_df)
        else:
            print(f"Файл {filename} не найден")


database = PGDatabase(
    host=config.get('Database', 'host'),
    database=config.get('Database', 'database'),
    user=config.get('Database', 'user'),
    password=config.get('Database', 'password')
)


for i, row in sales_df.iterrows():
    query = f"INSERT INTO sales values ('{row['doc_id']}', '{row['category']}', '{row['item']}', {row['amount']}, {row['price']}, {row['discount']}, {row['total']})"
    print(query)
    database.post(query)