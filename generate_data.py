from faker import Faker
import pandas as pd

fake = Faker()

data = {
    'customer_id': [fake.uuid4() for _ in range(1000)],
    'customer_name': [fake.name() for _ in range(1000)],
    'transaction_date': [fake.date_this_year() for _ in range(1000)],
    'amount': [fake.random_number(digits=5) for _ in range(1000)]
}

df = pd.DataFrame(data)
df.to_csv('seed_data.csv', index=False)
