import requests
from datetime import datetime, timedelta


class NewsFetcher:
    def __init__(self):
        self.api_key = "APIKEY" // Please login to newsapi org to get API access, key
    def fetch_news(self):
        current_date = datetime.today()
        last_week = current_date - timedelta(days=7)
        last_week_date=last_week.date()

        url = f"https://newsapi.org/v2/everything?q=cricket&from={last_week_date}&apiKey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            articles = data['articles']
            news = []
            for article in articles:
                title = article['title']
                source = article['source']['name']
                url=article['url']
                news.append({'title': title, 'source': source,'url':url})
                print(news)
            return news
        else:
            return []

