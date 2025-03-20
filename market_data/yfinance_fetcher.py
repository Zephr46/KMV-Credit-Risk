import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")

    latest_price = hist["Close"][-1]
    shares_outstanding = stock.info.get("sharesOutstanding", 0)
    
    market_value_equity = latest_price * shares_outstanding
    asset_volatility = hist["Close"].pct_change().std()

    return {"market_value_equity": market_value_equity, "asset_volatility": asset_volatility}
