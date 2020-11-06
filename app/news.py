from newsapi.newsapi_client import NewsApiClient
from types import SimpleNamespace
import json

newsapi = NewsApiClient(api_key = "78b9d599c4f94f8fa3afb1a5458928d6")

class News():
    def __init__(self):
        pass
    
    def search(self, q, category):
        top_headlines = newsapi.get_top_headlines(q = q, category = category)
        return top_headlines #allows for using dot notation


# test = News()
# temp = test.search("help", "technology")
# for article in temp["articles"]:
#     print(article["title"])
#     print(article["source"]["name"])