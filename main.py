import time
import pandas as pd
from sqlalchemy import create_engine, text

DB_URL = "mysql+mysqlconnector://user:password@localhost:3306/my_database"

def connect_with_retry(max_attempts=10, delay=10):
    for attempt in range(1, max_attempts + 1):
        try:
            print(f"Спроба підключення {attempt}/{max_attempts}...")
            engine = create_engine(DB_URL)
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            print("Підключення успішне!")
            return engine
        except Exception as e:
            print(f"База ще не готова: {e}")
            if attempt < max_attempts:
                time.sleep(delay)
    raise Exception("Не вдалось підключитись до бази після 10 спроб")

engine = connect_with_retry()
df = pd.read_sql("SELECT * FROM titanic", engine)
print(df)
print(f"\nРядків: {len(df)}, Колонок: {len(df.columns)}")