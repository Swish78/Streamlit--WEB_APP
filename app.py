import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Price Viewer")
st.subheader("By Swayam")

# Define a list of stock symbols to choose from
stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']

# Create a selectbox to choose a stock symbol
tickerSymbol = st.selectbox("Choose a stock ticker symbol", stock_symbols)

# If a stock symbol has been selected
if tickerSymbol:

    tickerData = yf.Ticker(tickerSymbol)
    start = st.date_input('Select Start Date')
    end = st.date_input('Select End Date')

    # Display the selected stock symbol
    st.write(f"Shown are Closing and Volume of {tickerSymbol} stock")
    tickerDF = tickerData.history(period='id', start=start, end=end)

    # Fetch the historical price data for the selected stock

    st.line_chart(tickerDF.Close)
    st.line_chart(tickerDF.Volume)

else:
    st.write("Please choose a stock ticker symbol above.")
