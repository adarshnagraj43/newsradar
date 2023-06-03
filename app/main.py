from app import app
from news_fetcher import NewsFetcher
from flask import jsonify

@app.route('/news')
def fetch_news():
    news_fetcher = NewsFetcher()
    news = news_fetcher.fetch_news()
    return jsonify(news)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
