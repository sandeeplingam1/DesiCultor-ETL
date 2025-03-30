import os
import pandas as pd

# Define directories
RAW_DIR = os.path.join("data", "raw")
PROCESSED_DIR = os.path.join("data", "processed")

def get_latest_file(raw_dir=RAW_DIR):
    """Get the most recently added CSV file from the raw data folder"""
    csv_files = [f for f in os.listdir(raw_dir) if f.endswith(".csv")]
    if not csv_files:
        raise FileNotFoundError("❌ No CSV files found in raw data folder.")
    latest_file = max(csv_files, key=lambda f: os.path.getctime(os.path.join(raw_dir, f)))
    return os.path.join(raw_dir, latest_file)

def extract_file(file_path):
    """Reads a CSV file into a DataFrame"""
    print(f"📥 Loading raw data from: {file_path}")
    return pd.read_csv(file_path)

def clean_dataframe(df):
    """Cleans the input DataFrame using standard steps"""
    print("🔧 Cleaning column names...")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    print("🧹 Dropping duplicate rows...")
    df = df.drop_duplicates()

    print("🧼 Handling missing values...")
    df = df.dropna(how="all")  # drop rows where all values are NaN

    print("📅 Converting any 'date' columns...")
    for col in df.columns:
        if "date" in col:
            try:
                df[col] = pd.to_datetime(df[col], errors='coerce')
            except:
                pass  # silently fail if conversion doesn't work

    print("🔠 Standardizing text columns...")
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip().str.lower()

    print("✅ Data cleaning complete.")
    return df

def save_to_processed(df, file_name="cleaned_data.csv"):
    """Saves cleaned DataFrame to the processed folder"""
    output_path = os.path.join(PROCESSED_DIR, file_name)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"💾 Cleaned data saved to: {output_path}")