from flask import Flask, request, jsonify, render_template
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from kmv_ml_model import predict_risk

# Initialize Flask
server = Flask(__name__)

# Initialize Dash
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("📊 Credit Risk Prediction Dashboard"),
    dcc.Input(id="ticker", type="text", placeholder="Enter Stock Ticker"),
    html.Button("Analyze", id="analyze-button", n_clicks=0),
    html.Div(id="output")
])

@app.callback(
    Output("output", "children"),
    Input("analyze-button", "n_clicks"),
    Input("ticker", "value")
)
def update_dashboard(n_clicks, ticker):
    if not ticker:
        return "❌ Please enter a stock ticker."

    try:
        result = predict_risk(ticker.upper())

        if isinstance(result, str):
            return f"❌ Error: {result}"

        return f"✅ Stock: {result['Stock']} - Predicted Default Risk: {result['Risk']}"

    except Exception as e:
        return f"❌ Error: {str(e)}"
import time

try:
    app.run(debug=True)
except Exception as e:
    print("Error:", e)
finally:
    input("Press Enter to exit...")  # Keeps the window openS