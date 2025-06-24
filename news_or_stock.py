import requests
import os
from dotenv import load_dotenv
from utils import log_event

load_dotenv()

def fetch_news_or_stock():
    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("❌ NEWS_API_KEY not found in .env file.")
        return 
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&pageSize=3&apiKey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        articles = data.get("articles", [])

        print("\nTop Business Headlines in the U.S: ")
        for i, article in enumerate(articles, start=1):
            print(f"{1}. {article['title']}")
            print(f"    Source: {article['source']['name']}")
            print(f"    URL: {article['url']}\n")

        log_event("Fetched news headlines successfully.")

    except Exception as e:
        log_event(f"Error fetching news: {e}")
        print("❌ Failed to fetch news headlines.")