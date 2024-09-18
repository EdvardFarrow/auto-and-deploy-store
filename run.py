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

sales_df = pd.DataFrame()

# Обработка файлов в директории
for filename in os.listdir(directory):
    # Если файл соответствует регулярному выражению
    if sales_path_regex.match(filename):
        file_path = os.path.join(directory, filename)
        print(f"Файл path: {file_path}")
        # Читаем CSV в DataFrame
        sales_df.append(pd.read_csv(file_path))
        print(f"Файл: {filename}")

database = PGDatabase(
    host=config.get('Database', 'host'),
    database=config.get('Database', 'database'),
    user=config.get('Database', 'user'),
    password=config.get('Database', 'password')
)

for f in sales_df:
    print(f"{f.iterrows()}")
    for i, row in f.iterrows():
        query = f"INSERT INTO sales values ('{row['doc_id']}', '{row['category']}', '{row['item']}', {row['amount']}, {row['price']}, {row['discount']}, {row['total']})"
        print(query)
        database.post(query)