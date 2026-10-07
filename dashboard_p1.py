import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration
st.set_page_config(page_title="Retail Catchment Dashboard", layout="wide")
st.title("📊 Regional Retail Catchment & Profitability")
st.markdown("An interactive command center analyzing regional sales, profit-sharing, and product performance.")

# 2.Prepared Datasets
monthly_summary = pd.read_csv('monthly_summary.csv')
regional_summary = pd.read_csv('regional_summary.csv')
product_summary = pd.read_csv('product_summary.csv')

# 3. Executive KPI Scorecards
st.markdown("### Executive Summary")
col1, col2, col3 = st.columns(3)

total_revenue = regional_summary['Total_Revenue'].sum()
total_net_profit = product_summary['Total_Net_Profit'].sum()
top_product = product_summary.iloc[0]['Product_Category']

col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Net Profit", f"${total_net_profit:,.2f}")
col3.metric("Top Performing Category", top_product)

st.markdown("---")

# 4. Interactive Charts Layout
left_column, right_column = st.columns(2)

with left_column:
    st.markdown("### Monthly Net Profit Trend")
    # Plotly Line Chart
    fig_monthly = px.line(monthly_summary, x='Month', y='Net_Profit', markers=True, 
                          title="Net Profit Over Time")
    st.plotly_chart(fig_monthly, use_container_width=True)

with right_column:
    st.markdown("### Regional Gross Profit Comparison")
    # Plotly Bar Chart
    fig_regional = px.bar(regional_summary, x='Region', y='Total_Gross_Profit', color='Region',
                          title="Profitability by Spatial Catchment")
    st.plotly_chart(fig_regional, use_container_width=True)

st.markdown("### Product Category Performance")
# Plotly Bar Chart for Products
fig_product = px.bar(product_summary, x='Product_Category', y='Total_Net_Profit', color='Product_Category',
                     title="Net Profit by Category")
st.plotly_chart(fig_product, use_container_width=True)
