# DesiCultor: Data-Driven Crop Price Pipeline for Direct Farm-to-Door Models

## About the Project
This project is inspired by **DesiCultor**, a food delivery startup I co-founded with my brother during the COVID-19 lockdown in 2020. Our goal was to bridge the gap between farmers and consumers by delivering fresh produce directly to customers' doorsteps.

Today, I’m reviving this idea with a data-driven lens — by building an **ETL pipeline** that fetches, cleans, and analyzes crop pricing data across Indian markets to help optimize pricing, sourcing, and delivery decisions in farm-to-customer models.

## Tech Stack
- Python (pandas, requests)
- SQL (SQLite or PostgreSQL)
- Jupyter Notebooks
- GitHub for versioning

## Data Sources
- [Kaggle – Indian Agri Commodity Prices](https://www.kaggle.com/datasets/anshtanwar/current-daily-price-of-various-commodities-india)
- [AgMarknet – Government Mandi Data](https://data.gov.in/resource/current-daily-price-various-commodities-various-markets-mandi)

## ETL Goals
- Extract daily pricing of core produce like tomatoes, potatoes, onions, etc.
- Clean and structure data from CSV/APIs
- Store in queryable format (SQLite DB)
- Generate pricing reports by region/product



---

## 📊 Phase 2: Exploratory Data Analysis (EDA)

After cleaning the raw agri-commodity data, I conducted exploratory data analysis to uncover trends and insights valuable for decision-making in agri-logistics and delivery platforms.

### 🔍 Key Insights

- **🥔 Top Commodities**: Potato, Onion, and Brinjal were the most frequently traded crops.
- **📍 State-wise Averages**: Goa, Meghalaya, and Delhi had the highest average modal prices.
- **📈 Tomato Price Spike**: A major surge in tomato prices occurred around August 1, 2023.
- **📦 Price Volatility**: Tomato and Bhindi showed high volatility, while Wheat and Banana remained stable.

These insights simulate how data-driven decisions could enhance crop delivery, farmer payouts, and inventory strategy for DesiCultor — the agri-startup I co-founded during the COVID-19 lockdown.

---


---

## 🔮 Bonus: Predictive Modeling (Phase 2.5)

As a bonus step, I trained a basic Linear Regression model to forecast tomato prices based on historical trends.

### ⚠️ Observations:
- 🔵 The actual modal price of tomato dropped significantly during August 2023.
- 🔴 The linear regression model failed to capture this — it predicted a flat upward trend.
- This illustrates the complexity and volatility in agri-price data, highlighting the need for more advanced models in future phases.

> Future plan: Experiment with ARIMA, Prophet, or LSTM to capture non-linear trends more accurately.

---

📦 Phase 3: ETL Automation + SQLite Database Integration

In this phase, I elevated the DesiCultor pipeline from one-time analysis to an automated, modular data engineering system.

🔁 Key Additions
	•	📥 Modular Extraction: Automatically detects and loads the latest CSV from the data/raw/ folder.
	•	🧹 Reusable Cleaning Functions: Built clean_data.py with cleaning logic that can be reused for any structured dataset.
	•	🚦 Orchestrated ETL Flow: Created run_etl.py, a central controller that triggers the full Extract → Transform → Load sequence in one run.
	•	💾 Processed Output: Cleaned data is saved as cleaned_data.csv under data/processed/.
	•	🛢️ SQLite Integration: The same cleaned data is inserted into a local data_store.db for historical tracking, analysis, and simulation of cloud data warehouse workflows.

💡 Why This Matters

With this structure, DesiCultor’s data pipeline can now:
	•	Handle real-time or batch file arrivals
	•	Clean and standardize data on-the-fly
	•	Store results both as CSV and in a queryable database
	•	Be easily extended to support APIs and cloud storage (like AWS S3 or RDS)

This phase bridges the gap between basic analysis and real-world data engineering systems — and it sets the stage for future enhancements like cloud deployment, dashboards, and automated reporting.

Note: 💭 The entire pipeline can now simulate a live ingestion setup — making it a production-ready foundation for modern agri-tech platforms.

---