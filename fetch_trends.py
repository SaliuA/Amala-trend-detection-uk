# fetch_trends.py

import os
import time
from datetime import datetime
import pandas as pd
from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def fetch_google_trends_data(
    keyword: str,
    geo: str = 'GB',
    timeframe: str = 'today 5-y',
    save_dir: str = 'data'
):
    """
    Fetch Google Trends interest-over-time data and save as CSV.

    Parameters:
        keyword (str): Keyword to search (e.g., 'Amala').
        geo (str): Country code (default = 'GB' for United Kingdom).
        timeframe (str): Time range (default = 'today 5-y').
        save_dir (str): Directory to save CSV file.
    """
    print(f"\n🔍 Fetching Google Trends data for '{keyword}' in {geo}...")

    # Create pytrends connection with retries
    pytrends = TrendReq(hl='en-GB', tz=0, retries=3, backoff_factor=0.5)

    try:
        # Build search payload
        pytrends.build_payload([keyword], geo=geo, timeframe=timeframe)
        time.sleep(2)  # Rate limit buffer

        # Fetch interest over time
        df = pytrends.interest_over_time()

        if df.empty:
            print(f"[!] No data found for '{keyword}' in {geo}.")
            return

        # Drop partial data column
        if 'isPartial' in df.columns:
            df.drop(columns='isPartial', inplace=True)

        # Ensure data directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Create filename
        date_str = datetime.now().strftime('%Y%m%d')
        filename = f"{keyword.lower().replace(' ', '_')}_trends_{date_str}.csv"
        filepath = os.path.join(save_dir, filename)

        # Save to CSV
        df.to_csv(filepath)
        print(f"[✓] Saved: {filepath}")

    except TooManyRequestsError:
        print("[⚠] Google blocked too many requests. Try again later.")
    except Exception as e:
        print(f"[X] An unexpected error occurred: {e}")

# Run directly
if __name__ == '__main__':
    fetch_google_trends_data(keyword='Amala', geo='GB', timeframe='today 5-y')
