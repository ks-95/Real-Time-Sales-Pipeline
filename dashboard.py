import streamlit as st
import duckdb
import pandas as pd
import time
import os

# Page Config
st.set_page_config(page_title="Yukin.ai Prep: Real-Time AI", layout="wide")
st.title("🚀 Real-Time Sales & Anomaly Detection")

# Helper to connect to DuckDB
def get_data():
    con = duckdb.connect()
    if os.path.exists("live_stream.json"):
        # Primary Query: Get KPIs, Latest Sale, and Historical Average in one go
        query = """
        WITH base_data AS (
            SELECT * FROM read_json_auto('live_stream.json')
        ),
        stats AS (
            SELECT 
                count(*) as total_sales,
                round(sum(price), 2) as total_revenue,
                avg(price) as global_avg
            FROM base_data
        ),
        latest_entry AS (
            SELECT product, price, transaction_id, timestamp
            FROM base_data
            ORDER BY timestamp DESC
            LIMIT 1
        )
        SELECT 
            s.*, 
            l.product as last_prod, 
            l.price as last_price, 
            l.timestamp as last_ts
        FROM stats s, latest_entry l
        """
        return con.execute(query).df()
    return None

# Placeholders for UI
kpi_area = st.empty()
alert_area = st.empty()
chart_area = st.empty()
table_area = st.empty()

while True:
    df = get_data()
    
    if df is not None and not df.empty:
        # 1. Update KPI Cards
        with kpi_area.container():
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Transactions", int(df['total_sales'][0]))
            col2.metric("Total Revenue", f"${df['total_revenue'][0]:,.2f}")
            col3.metric("Global Avg Price", f"${df['global_avg'][0]:,.2f}")

        # 2. THE ALERT LOGIC (The "AI" Part)
        # If the latest price is > 3x the global average, trigger red alert
        last_price = df['last_price'][0]
        avg_price = df['global_avg'][0]
        
        with alert_area.container():
            if last_price > (avg_price * 3):
                st.error(f"🚨 ANOMALY DETECTED! Product: {df['last_prod'][0]} | Price: ${last_price:,.2f} | (Threshold: 3x Avg)")
            else:
                st.success("✅ System Status: Normal. Monitoring stream...")

        # 3. Recent Transactions Table
        with table_area.container():
            st.subheader("Latest Stream Events")
            # Pull last 5 rows for the table
            con_temp = duckdb.connect()
            recent_df = con_temp.execute("SELECT timestamp, product, price FROM read_json_auto('live_stream.json') ORDER BY timestamp DESC LIMIT 5").df()
            st.table(recent_df)
            
    else:
        st.info("Waiting for 'live_stream.json'... Please start your producer script.")

    time.sleep(2)
    st.rerun()