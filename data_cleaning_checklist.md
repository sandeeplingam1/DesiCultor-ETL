# 🧼 Data Cleaning Checklist

This is a universal checklist to clean any structured dataset (CSV, Excel, API JSON).  
Use this before pushing data to your `processed/` folder.

---

## 🔰 Stage 0: Initial Load
- [ ] Can I read the file without errors? (CSV, Excel, JSON, etc.)
- [ ] Do I see expected rows/columns in `df.head()`?
- [ ] Have I verified the shape using `df.shape`?

---

## 🔍 Stage 1: Profiling the Dataset
- [ ] `df.info()` → Are data types as expected?
- [ ] `df.describe()` → Any unusual min/max or count values?
- [ ] `df.isnull().sum()` → Which columns have missing data?
- [ ] Unique value check for categorical fields (`value_counts()`)

---

## 🧹 Stage 2: Basic Cleaning
- [ ] Rename columns to `snake_case` and strip spaces
  ```python
  df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")