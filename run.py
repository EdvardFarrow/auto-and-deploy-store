import os 
import pandas as pd
import re
import configparser
from pgdb import PGDatabase
import psycopg2 

# Reading the configuration file
config = configparser.ConfigParser()  # Create a config parser object
config.read('config.ini')  # Read the 'config.ini' file

# Get the path pattern for sales files and the directory path from the configuration file
sales_path_pattern = config.get('Paths', 'sales_path_pattern')
directory = config.get('Paths', 'directory')

# Convert the sales file path pattern into a regular expression object
sales_path_regex = re.compile(sales_path_pattern)

sales_df = []  # Initialize an empty list to store the dataframes

# Process each file in the specified directory
for filename in os.listdir(directory):
    # If the filename matches the regular expression pattern
    if sales_path_regex.match(filename):
        file_path = os.path.join(directory, filename)  # Get the full file path
        print(f"File path: {file_path}")
        # Read the CSV file into a pandas dataframe and append it to the list
        sales_df.append(pd.read_csv(file_path))
        print(f"File: {filename}")

# Initialize the PostgreSQL database connection using the credentials from the config file
database = PGDatabase(
    host=config.get('Database', 'host'),
    database=config.get('Database', 'database'),
    user=config.get('Database', 'user'),
    password=config.get('Database', 'password')
)

# Loop through each dataframe in the sales_df list
for f in sales_df:
    print(f"{f.iterrows()}")
    # Loop through each row in the dataframe
    for i, row in f.iterrows():
        # Create an SQL query to insert data into the 'sales' table
        query = f"INSERT INTO sales values ('{row['doc_id']}', '{row['category']}', '{row['item']}', {row['amount']}, {row['price']}, {row['discount']}, {row['total']})"
        print(query)  # Print the query for debugging
        database.post(query)  # Execute the query to insert data into the database