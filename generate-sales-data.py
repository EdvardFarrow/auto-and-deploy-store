from datetime import timedelta, datetime
import pandas as pd
import random
import string
import csv
import json



with open('home_goods_store.json', 'r') as file:
    home_goods_store = json.load(file)


discounts = [5, 10, 20, 30, 50]


items = [(item, price) for category in home_goods_store.values() for item, price in category.items()]


def generate_doc_id(prefix='CHK'):
    now = datetime.now()
    date_str = now.strftime('%Y%m%d')
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    doc_id = f'{prefix}-{date_str}-{random_suffix}'
    return doc_id

def create_sales_csv(file_path, num_records=random.randint(1,10)):

    data = []

    
    for _ in range(num_records):
        doc_id = generate_doc_id()

        num_items_in_check = random.randint(1, 10)

        for _ in range(num_items_in_check):
            
            category = category = random.choice(list(home_goods_store.keys()))

            item, price = random.choice(list(home_goods_store[category].items()))
            
            amount = random.randint(1, 5)
                    
            discount = random.choice(discounts)
            discount_amount = (discount / 100) * (price * amount)

            total = round(price * amount - discount_amount, 2)

            data.append([doc_id, item, category, amount, price, discount,  total])


    df = pd.DataFrame(data, columns=['doc_id', 'item', 'category', 'amount', 'price', 'discount',  'total'])

    df.to_csv(file_path, index=False)

    return df


create_sales_csv(f'{random.randint(1, 20)}_{random.randint(1, 6)}.csv', num_records=random.randint(1, 10))



