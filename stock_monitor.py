import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys and configuration
ALPHA_VANTAGE_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
NEWS_API_KEY = os.getenv('NEWS_API_KEY')
STOCK_NAME = "AAPL"
COMPANY_NAME = "Apple Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Get stock price data from Alpha Vantage
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={ALPHA_VANTAGE_KEY}'
response = requests.get(url)
data = response.json()["Time Series (Daily)"]

# Get the last two days of data
data_list = list(data.items())
today_data = float(data_list[0][1]["4. close"])
yesterday_data = float(data_list[1][1]["4. close"])

# Calculate percentage change
difference = today_data - yesterday_data
percentage_change = round((difference / yesterday_data) * 100)

# If price change is more than 2%, get news
if abs(percentage_change) > 2:
    # Prepare news API request
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    
    # Get news articles
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    
    # Format articles
    formatted_articles = [
        f"{STOCK_NAME}: {'🔺' if percentage_change > 0 else '🔻'}{abs(percentage_change)}%\n"
        f"Headline: {article['title']}\n"
        f"Brief: {article['description'] if article['description'] else 'No description available.'}"
        for article in three_articles
    ]
    
    # Print results
    print(f"\nCurrent {STOCK_NAME} Price: ${today_data:.2f}")
    print(f"Price Change: {percentage_change}%\n")
    
    print("Latest News:")
    for article in formatted_articles:
        print(article)
        print("-" * 50) 