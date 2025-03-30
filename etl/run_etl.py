from db_handler import insert_into_sqlite

from clean_data import (
    get_latest_file,
    extract_file,
    clean_dataframe,
    save_to_processed
)

def run_etl():
    print("\n🚀 Starting DesiCultor ETL Run")

    try:
        # Step 1: Get latest raw CSV
        latest_file_path = get_latest_file()
        print(f"📁 Latest file found: {latest_file_path}")

        # Step 2: Extract
        raw_df = extract_file(latest_file_path)

        # Step 3: Clean
        cleaned_df = clean_dataframe(raw_df)

        # Step 4: Save cleaned CSV
        save_to_processed(cleaned_df)
        
        # Step 5: Insert into SQLite DB
        insert_into_sqlite(cleaned_df)

        print("✅ ETL run complete!\n")

    except Exception as e:
        print(f"❌ ETL failed: {e}\n")

# Run this file directly to trigger ETL
if __name__ == "__main__":
    run_etl()