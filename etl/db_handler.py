import sqlite3
import os

DB_PATH = os.path.join("db", "data_store.db")

def insert_into_sqlite(df, table_name="cleaned_data"):
    """Inserts cleaned DataFrame into SQLite database"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    # Connect to SQLite (creates db if it doesn't exist)
    conn = sqlite3.connect(DB_PATH)

    # Insert into table (creates table if it doesn't exist)
    try:
        df.to_sql(table_name, conn, if_exists="append", index=False)
        print(f"🗃️ Inserted {len(df)} records into '{table_name}' table in SQLite DB.")
    except Exception as e:
        print(f"❌ DB insert failed: {e}")
    finally:
        conn.close()