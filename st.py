
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
    st.subheader('Forecast Data')
    st.write(forecast.tail())
    
    # prediction chart
    st.subheader('Forecast Chart')
    st.write(m.plot(forecast))
    
    # prediction components chart
    st.subheader('Components')
    st.write(m.plot_components(forecast))

def plot_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y = data['Open'], name = 'stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y = data['Close'], name = 'stock_open'))
    fig.layout.update(title_text = 'Time Series Data', xaxis_rangeslider_visible = True)
    st.plotly_chart(fig)
    
    
def main():
    
    st.header('Stock Market prediction.')
    st.markdown("""
                - Model will try to preditc.
                """)
    
    ticker = st.text_input('Please type the stock ticker', value = 'AAPL').upper()
    
    # raw data
    st.subheader('Raw Data')
    
    try:
        data = load_data(ticker)   
        st.write(data.tail())
        # plot raw data
        plot_data(data)
        with st.spinner('Forecasting...'):
            predict(data)

    except:
        st.error("Ticker no recognizable.Please visit this [link](https://finance.yahoo.com/lookup) to check on ticker codes.", icon="🚨")


    
    



if __name__ == '__main__':
    main()