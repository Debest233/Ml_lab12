import pandas as pd
import random
from datetime import datetime, timedelta
from sqlalchemy import create_engine

print("Generowanie danych testowych...")
kategorie = ["books", "electronics", "clothing", "home", "toys"]
statusy = ["paid", "paid", "paid", "pending", "failed"]

dane = []
start_date = datetime(2026, 5, 1)

for i in range(1000):
    event_time = start_date + timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
    dane.append({
        "event_time": event_time,
        "user_id": f"u{random.randint(1, 100):03d}",
        "category": random.choice(kategorie),
        "amount": round(random.uniform(10.0, 500.0), 2),
        "status": random.choice(statusy)
    })

df = pd.DataFrame(dane)

print("Łączenie z bazą PostgreSQL i wgrywanie danych...")
# Połączenie do bazy w Dockerze z poziomu lokalnego Pythona (port 5432)
engine = create_engine("postgresql+psycopg2://bi:bi@localhost:5432/ntpd")

df.to_sql("transactions", engine, if_exists="replace", index=False)
print(f"Sukces! Załadowano {len(df)} wierszy do tabeli 'transactions'.")