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