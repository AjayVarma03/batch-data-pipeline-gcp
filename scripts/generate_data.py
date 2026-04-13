import pandas as pd
import random
from datetime import datetime, timedelta
import os

os.makedirs('data', exist_ok=True)

# realistic mappings
products = {
    "iPhone": ("Electronics", 70000),
    "Laptop": ("Electronics", 50000),
    "Headphones": ("Electronics", 3000),
    "Shoes": ("Fashion", 2500),
    "T-Shirt": ("Fashion", 800),
    "Watch": ("Accessories", 4000),
    "Backpack": ("Accessories", 1500)
}

cities = ["Hyderabad", "Bangalore", "Mumbai", "Delhi", "Chennai"]

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery"]

statuses = ["Delivered", "Shipped", "Cancelled", "Returned"]

data = []

start_date = datetime(2024, 1, 1)

for i in range(1, 15001):  # 15K rows
    product = random.choice(list(products.keys()))
    category, base_price = products[product]

    quantity = random.randint(1, 3)
    amount = base_price * quantity + random.randint(-500, 500)

    order_date = start_date + timedelta(days=random.randint(0, 120))

    # delivery logic
    if random.random() < 0.85:
        delivery_days = random.randint(2, 7)
        delivery_date = order_date + timedelta(days=delivery_days)
        status = "Delivered"
    else:
        delivery_date = None
        status = random.choice(["Cancelled", "Returned"])

    data.append({
        "order_id": i,
        "customer_id": f"C{random.randint(1000, 9999)}",
        "product": product,
        "category": category,
        "quantity": quantity,
        "amount": amount,
        "city": random.choice(cities),
        "payment_method": random.choice(payment_methods),
        "order_date": order_date,
        "delivery_date": delivery_date,
        "status": status
    })

df = pd.DataFrame(data)

df.to_csv("data/sales.csv", index=False)

print("✅ Realistic dataset generated: 15,000 rows")