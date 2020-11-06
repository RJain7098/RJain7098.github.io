from newsapi.newsapi_client import NewsApiClient
from types import SimpleNamespace
import json

newsapi = NewsApiClient(api_key = "78b9d599c4f94f8fa3afb1a5458928d6")

class News():
    def __init__(self):
        pass
    
    def search(self, q, category):
        top_headlines = newsapi.get_top_headlines(q = q, category = category)
        return top_headlines

def _delete_extra(title, source):
        index = title.lower().find(source.partition(".")[0].lower())
        print(index)
        return title[0:index-2]

# test = News()
# temp = test.search("google", "technology")
# for article in temp["articles"]:
#      print(article["title"])
#      print(article["source"]["name"])
#      print(_delete_extra(article["title"], article["source"]["name"]))
#      print()

