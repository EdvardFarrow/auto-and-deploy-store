from datetime import timedelta, datetime
import pandas as pd
import random
import string
import csv
import json

# Load the home_goods_store data from a JSON file
with open('home_goods_store.json', 'r') as file:
    home_goods_store = json.load(file)

# List of possible discount values (as percentages)
discounts = [5, 10, 20, 30, 50]

# Flatten the items from the home_goods_store into a list of tuples (item_name, price)
items = [(item, price) for category in home_goods_store.values() for item, price in category.items()]

# Function to generate a unique document ID
def generate_doc_id(prefix='CHK'):
    now = datetime.now()  # Get the current date and time
    date_str = now.strftime('%Y%m%d')  # Format the current date as a string (YYYYMMDD)
    # Generate a random 4-character suffix consisting of uppercase letters and digits
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    # Combine the prefix, date, and suffix to create the document ID
    doc_id = f'{prefix}-{date_str}-{random_suffix}'
    return doc_id

# Function to create a CSV file with random sales data
def create_sales_csv(file_path, num_records=random.randint(1,10)):
    data = []  # Initialize an empty list to store the sales data

    # Loop through each record (sale)
    for _ in range(num_records):
        doc_id = generate_doc_id()  # Generate a unique document ID for each record

        num_items_in_check = random.randint(1, 10)  # Randomly decide how many items are in this sale

        # Loop through each item in the current sale
        for _ in range(num_items_in_check):
            category = random.choice(list(home_goods_store.keys()))  # Randomly select a product category
            item, price = random.choice(list(home_goods_store[category].items()))  # Randomly select an item from the category

            amount = random.randint(1, 5)  # Randomly choose the quantity of the item being sold

            discount = random.choice(discounts)  # Randomly choose a discount percentage
            discount_amount = (discount / 100) * (price * amount)  # Calculate the discount amount

            total = round(price * amount - discount_amount, 2)  # Calculate the total price after discount

            # Add the sale details to the data list
            data.append([doc_id, item, category, amount, price, discount, total])

    # Create a pandas DataFrame with the sales data
    df = pd.DataFrame(data, columns=['doc_id', 'item', 'category', 'amount', 'price', 'discount', 'total'])

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

    return df  # Return the DataFrame for further use

# Generate a sales CSV file with a random file name and a random number of records
create_sales_csv(f'{random.randint(1, 20)}_{random.randint(1, 6)}.csv', num_records=random.randint(1, 10))




