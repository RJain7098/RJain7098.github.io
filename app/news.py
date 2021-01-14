from newsapi.newsapi_client import NewsApiClient
import json

newsapi = NewsApiClient(api_key = "d71bc0d973dc44fca3f46a84fddfae28")

class News():
    def __init__(self):
        pass
    
    def search(self, q, category):
        top_headlines = newsapi.get_top_headlines(q = q, category = category)
        return top_headlines


