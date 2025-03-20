import requests
from bs4 import BeautifulSoup

def get_financial_data(ticker):
    url = f"https://www.screener.in/company/{ticker}/"
    headers = {"User-Agent": "Mozilla/5.0"}  # Avoid blocking

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"error": f"Failed to fetch data for {ticker}"}

    soup = BeautifulSoup(response.text, "html.parser")
    
    try:
        table_rows = soup.find_all("tr")

        # Extract relevant financial data
        revenue = next((row.find_all("td")[1].text for row in table_rows if "Sales" in row.text), None)
        net_profit = next((row.find_all("td")[1].text for row in table_rows if "Net Profit" in row.text), None)
        icr = next((row.find_all("td")[1].text for row in table_rows if "Interest Coverage" in row.text), None)

        return {
            "Revenue": revenue,
            "Net Profit": net_profit,
            "Interest Coverage Ratio": icr
        }

    except Exception as e:
        return {"error": str(e)}

# Test it
print(get_financial_data("RELIANCE"))
