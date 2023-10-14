# Stock-Market-Forecast
- This project is a stock market prediction tool with the following key components:

## Data Gathering:

Utilizes the Yahoo Finance API via the yfinance library to fetch historical stock price data.
The user specifies a company's ticker symbol, and the program retrieves the relevant data for analysis.

## Data Visualization:

Employs Plotly Express and Plotly Graph Objects to create interactive visualizations, specifically candlestick charts.
Displays the original stock price data as an interactive candlestick chart for the selected company.

## Time Series Forecasting:

Utilizes the Prophet library for time series forecasting. It transforms the historical stock price data into a format suitable for modeling.
Develops a Prophet model to predict future stock prices.
Generates a prediction chart that shows the predicted stock price trend and associated uncertainty.

## User Interface:

Utilizes Streamlit to create a user-friendly interface.
Allows the user to input a company's ticker symbol.
Provides guidance on finding a company's ticker symbol.
Handles exceptions gracefully and displays informative error messages.

## Usage:

The user inputs a company's ticker symbol.
The application fetches historical stock price data for the selected company.
It displays the original data as a candlestick chart.
The Prophet model predicts future stock prices and shows the prediction chart, including uncertainty intervals.
The user can explore these visualizations to gain insights into the stock's historical performance and potential future trends.

## Instructions:

The user should input a stock ticker symbol (e.g., AAPL for Apple).
The program fetches and displays the historical stock price data.
The user can explore the original candlestick chart.
After a brief processing time, the program presents a prediction chart with future price predictions and trends.
Users are guided on how to find a company's ticker symbol if they are unsure.
This project combines data retrieval, data visualization, and time series forecasting to provide users with valuable insights into the stock market's historical performance and potential future trends for a selected company. It is a user-friendly tool with a clear and interactive interface.

- You can check the live version of the projet [HERE](https://hugomilesi-stock-market-forecast-st-skvbiy.streamlit.app/)
