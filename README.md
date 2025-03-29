# Simple Stock Price Alert Script

A straightforward Python script that monitors Apple (AAPL) stock price and fetches relevant news when significant changes occur.

## Test
This is a test commit to verify GitHub connection.

## Features

- Fetches daily stock prices from Alpha Vantage API
- Calculates price changes
- Gets relevant news articles when price changes by more than 2%
- Clean, commented code - perfect for learning API integration

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   ALPHA_VANTAGE_API_KEY=your_key_here
   NEWS_API_KEY=your_key_here
   ```

## Usage

Simply run:
```bash
python stock_monitor.py
```

The script will:
1. Get today's and yesterday's AAPL stock prices
2. Calculate the percentage change
3. If change > 2%, fetch and display relevant news articles

## API Requirements

- Alpha Vantage API (for stock data)
- NewsAPI (for news articles)

Get your API keys at:
- https://www.alphavantage.co/support/#api-key
- https://newsapi.org/register

## Example Output

```
Current AAPL Price: $223.85
Price Change: 2.15%

Latest News:
AAPL: 🔺2.15%
Headline: [News headline here]
Brief: [News description here]
--------------------------------------------------
```

## License

MIT License 