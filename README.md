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
