
# data manipulation
import yfinance as yf
from datetime import datetime
import time
import pandas as pd
import numpy as np

#visualization
import plotly.express as px 
import plotly.graph_objects as go

# model
from prophet import Prophet

import streamlit as st


def load_data(ticker):
    end = datetime.now()
    start = datetime(2015, 1, 1)

    start_timer = time.time()
    stock = yf.download(ticker, start = start, end = end)
    stock.reset_index(inplace = True)
    end_timer = time.time() - start_timer
    
    return stock

def predict(data):
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns = {'Date': 'ds', 'Close': 'y'})
    
    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods = 365)
    forecast = m.predict(future)
    st.subheader('predictions dataset')
    st.write(forecast.tail())
    
    # prediction chart
    st.subheader('Predicted Chart')
    st.write(m.plot(forecast))
    
    # prediction components chart
    st.subheader('Components')
    st.write(m.plot_components(forecast))

def plot_data(data):
    fig = go.Figure(data=[go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

    #fig.add_trace(go.Scatter(x=data['Date'], y = data['Open'], name = 'stock_open'))
    #fig.add_trace(go.Scatter(x=data['Date'], y = data['Close'], name = 'stock_open'))
    #fig.layout.update(title_text = 'Time Series Data', xaxis_rangeslider_visible = True)
    
    
    st.plotly_chart(fig)
    
    
def main():
    
    st.header('Stock Market prediction.')
    st.markdown("""
                ## How it works
                - First, type the ticker of the company you want to check.
                - If you don't know the company ticker, you can check at [yahoo finance](https://finance.yahoo.com/) website, type the company name at the search bar and yahoo will show its ticker.
                - A candlestick chart will be displayed showing the original data.
                - Then, after a few seconds the model will plot a prediction chart where the blue area correnponds to the price prediction.
                - Some famous company tickers: Google(GOOG), Microsoft(MSFT), Tesla(TSLA).
                ---
                """)
    
    ticker = st.text_input('Please type the stock ticker', value = 'AAPL').upper()
    
    # raw data
    st.subheader('Original Data')
    
    try:
        data = load_data(ticker)   
        st.write(data.tail())
        # plot raw data
        st.subheader(f'Candlestick chart for {ticker}')
        plot_data(data)
        st.markdown('---')
        
        with st.spinner('Forecasting...'):
            st.header(f'Forecast chart for {ticker}')
            predict(data)

    except:
        st.error("Ticker no recognizable.Please visit this [link](https://finance.yahoo.com/lookup) to check on ticker codes.", icon="🚨")



if __name__ == '__main__':
    main()