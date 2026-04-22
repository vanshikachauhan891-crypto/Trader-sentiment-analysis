import streamlit as st
import pandas as pd

# Load dataset
merged = pd.read_csv("merged.csv")

# Fix column names
merged.columns = merged.columns.str.lower().str.replace(" ", "_")

# DEBUG (to check data)
st.write("Columns:", merged.columns)
st.write("Preview:", merged.head())

# Aggregations
sentiment_perf = merged.groupby('classification')['closed_pnl'].mean().reset_index()
trades_freq = merged.groupby('classification').size().reset_index(name='num_trades')

# UI
st.title("📊 Trader Sentiment Dashboard")

st.subheader("Average PnL by Sentiment")
st.bar_chart(sentiment_perf.set_index('classification'))

st.subheader("Trade Frequency by Sentiment")
st.bar_chart(trades_freq.set_index('classification'))
