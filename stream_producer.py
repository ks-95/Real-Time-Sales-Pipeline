import json
import time
import random
from faker import Faker
from datetime import datetime

fake = Faker()

def generate_sale():
    return {
        "transaction_id": fake.uuid4(),
        "user_id": random.randint(1000, 9999),
        "product": random.choice(["Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard"]),
        "price": round(random.uniform(20.0, 1500.0), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

print("--- Starting Real-Time Sales Stream ---")
try:
    while True:
        sale = generate_sale()
        print(f"New Sale: {sale}")
        
        with open("live_stream.json", "a") as f:
            f.write(json.dumps(sale) + "\n")
            
        time.sleep(1) 
except KeyboardInterrupt:
    print("\nStream stopped.")
