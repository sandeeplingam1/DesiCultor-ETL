import os
import pandas as pd
from datetime import datetime

# Step 1: Auto-detect the latest CSV in data/raw/
RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")

def get_latest_file(raw_dir):
    csv_files = [f for f in os.listdir(raw_dir) if f.endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError("❌ No CSV files found in raw data folder.")
    latest_file = max(csv_files, key=lambda f: os.path.getctime(os.path.join(raw_dir, f)))
    return os.path.join(raw_dir, latest_file)

# Step 2: Apply basic universal cleaning
def clean_dataframe(df):
    print("🔧 Cleaning column names...")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    print("🧹 Dropping duplicate rows...")
    df = df.drop_duplicates()

    print("🧼 Handling missing values...")
    df = df.dropna(how="all")  # drop rows where all values are NaN

    print("📅 Trying to convert any 'date' column...")
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass  # skip if it can't be converted

    print("🔠 Standardizing text columns...")
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip().str.lower()

    return df

# Step 3: Main ETL function
def run_cleaning_pipeline():
    print("🚀 Starting data cleaning pipeline...")

    try:
        file_path = get_latest_file(RAW_DIR)
        print(f"📥 Loading raw data from: {file_path}")
        df = pd.read_csv(file_path)

        cleaned_df = clean_dataframe(df)

        output_path = os.path.join(PROCESSED_DIR, "cleaned_data.csv")
        cleaned_df.to_csv(output_path, index=False)
        print(f"✅ Cleaned data saved to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Run the cleaning script if this file is executed directly
if __name__ == "__main__":
    run_cleaning_pipeline()