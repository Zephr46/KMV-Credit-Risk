import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from screener_scraper import get_financial_data

# Dummy function to get stock price & volatility
def get_stock_data(ticker):
    # Replace this with actual stock API (like Yahoo Finance)
    return np.random.uniform(500, 2000), np.random.uniform(0.02, 0.05)

# Function to preprocess data
def preprocess_data(ticker):
    stock_price, volatility = get_stock_data(ticker)
    financials = get_financial_data(ticker)

    if "error" in financials:
        return None, financials["error"]

    revenue = float(financials["Revenue"].replace(",", "").split(" ")[0])  # Convert '10,00,000 Cr' to number
    net_profit = float(financials["Net Profit"].replace(",", "").split(" ")[0])
    icr = float(financials["Interest Coverage Ratio"].replace(",", "").split(" ")[0])

    # Convert into feature array
    features = np.array([[stock_price, volatility, revenue, net_profit, icr]])

    return features, None

# Train ML model (use real historical data for better results)
def train_model():
    # Placeholder dataset - replace this with real labeled data
    X_train = np.random.rand(100, 5)  # 5 features
    y_train = np.random.choice([0, 1], size=100)  # 0 = Low Risk, 1 = High Risk

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    return model

# Prediction function
def predict_risk(ticker):
    model = train_model()
    features, error = preprocess_data(ticker)

    if error:
        return error

    prediction = model.predict(features)
    risk_label = "High" if prediction[0] == 1 else "Low"

    return {"Stock": ticker, "Risk": risk_label}

# Test
print(predict_risk("RELIANCE"))
