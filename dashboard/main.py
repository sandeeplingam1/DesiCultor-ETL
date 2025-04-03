import streamlit as st
import pandas as pd
import plotly.express as px
import os

# ---- Page Config ----
st.set_page_config(page_title="DesiCultor Dashboard", layout="wide")

# ---- Custom Styling with Agri Theme ----
st.markdown("""
<style>
    /* Set background color */
    body {
        background-color: #fefae0;
    }
    /* Change sidebar and general layout */
    .css-1d391kg { background-color: #fdf6e3 !important; }
    .st-eb { background-color: #fefae0 !important; }

    /* Headings and tab colors */
    h1, h2, h3, .stTabs [role="tab"] {
        color: #386641;
    }

    /* Tabs styling */
    .stTabs [role="tab"] {
        font-weight: bold;
        padding: 8px 20px;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin-right: 5px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #dda15e !important;
        color: white !important;
    }

    /* Metric box styling */
    .element-container:has(.stMetric) {
        background-color: #f4f1de;
        border-radius: 10px;
        padding: 10px;
    }

    /* Table Styling */
    .stDataFrame {
        background-color: white;
    }
</style>
""", unsafe_allow_html=True)

# ---- Load Data ----
@st.cache_data
def load_data():
    file_path = os.path.join("data", "processed", "cleaned_data.csv")
    return pd.read_csv(file_path, parse_dates=["arrival_date"])

df = load_data()

# ---- Metrics ----
total_records = len(df)
top_state = df.groupby("state")["modal_price"].mean().idxmax()
highest_price = df["modal_price"].max()

# ---- Header ----
st.title("🚜 DesiCultor: Crop Price Dashboard")
st.markdown("A farm-to-door **data experience** that blends agri-insight with analytics.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Records", f"{total_records:,}")
col2.metric("Top State", top_state.title())
col3.metric("Highest Modal Price", f"₹ {int(highest_price):,}")

# ---- Filters (Compact + Above Tabs) ----
with st.container():
    with st.expander("🌾 Filter Options", expanded=True):
        col1, col2 = st.columns(2)

        # Commodity filter
        commodities = sorted(df["commodity"].dropna().unique())
        selected_commodity = col1.selectbox("Filter by Commodity", ["All"] + commodities)

        # State filter
        states = sorted(df["state"].dropna().unique())
        selected_state = col2.selectbox("Filter by State", ["All"] + states)

# ---- Filter Logic ----
filtered_df = df.copy()
if selected_commodity != "All":
    filtered_df = filtered_df[filtered_df["commodity"] == selected_commodity]

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

# ---- Tabs Layout ----
tab1, tab2, tab3 = st.tabs(["📈 Price Trend", "📊 Avg Price by State", "📂 Data Explorer"])

# ---- Tab 1: Price Trend ----
with tab1:
    st.subheader("📈 Modal Price Trend Over Time")

    trend_df = filtered_df.groupby("arrival_date")["modal_price"].mean().reset_index()

    fig = px.line(
        trend_df,
        x="arrival_date",
        y="modal_price",
        title="Average Modal Price Over Time",
        markers=True,
        labels={"arrival_date": "Date", "modal_price": "Modal Price (₹)"},
        template="simple_white",
    )
    fig.update_traces(line=dict(color="#bc4749", width=3), marker=dict(size=6))
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))

    st.plotly_chart(fig, use_container_width=True)

# ---- Tab 2: Avg Price by State ----
with tab2:
    st.subheader("📊 Average Modal Price by State")

    state_avg = filtered_df.groupby("state")["modal_price"].mean().sort_values(ascending=False).reset_index()

    fig2 = px.bar(
        state_avg,
        x="modal_price",
        y="state",
        orientation="h",
        title="State-wise Avg Modal Price",
        labels={"modal_price": "Avg Price (₹)", "state": "State"},
        template="simple_white",
    )
    fig2.update_traces(marker_color="#6a994e")
    fig2.update_layout(margin=dict(l=20, r=20, t=50, b=20))

    st.plotly_chart(fig2, use_container_width=True)

# ---- Tab 3: Data Explorer ----
with tab3:
    st.subheader("📂 Data Explorer")
    st.markdown(f"Showing **{len(filtered_df):,}** records based on your filters.")
    st.dataframe(filtered_df.head(50), use_container_width=True)