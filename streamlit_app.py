import streamlit as st
import pandas as pd
import yfinance as yf

# VCP Stock Screener App
st.set_page_config(page_title="VCP Stock Screener", layout="wide")

st.title("Volatility Contraction Pattern (VCP) Stock Screener")
st.write("Analyze Indian cash market stocks for VCP patterns and fundamentals.")

# Sidebar filters
st.sidebar.header("Filters")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., RELIANCE.NS)")

if ticker:
    # Fetch data
    data = yf.download(ticker, period="6mo", interval="1d")
    if not data.empty:
        st.subheader(f"Price Chart for {ticker}")
        st.line_chart(data['Close'])

        # Basic VCP calculation: 50/200 EMA
        data['EMA50'] = data['Close'].ewm(span=50, adjust=False).mean()
        data['EMA200'] = data['Close'].ewm(span=200, adjust=False).mean()
        st.subheader("EMA50 vs EMA200")
        st.line_chart(data[['EMA50','EMA200']])

        # Display latest values
        latest = data.iloc[-1]
        st.write({
            'Close': latest['Close'],
            'EMA50': latest['EMA50'],
            'EMA200': latest['EMA200']
        })
    else:
        st.error("No data found for this ticker.")
else:
    st.info("Please enter a stock ticker to see analysis.")
