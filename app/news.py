from newsapi.newsapi_client import NewsApiClient
from types import SimpleNamespace
import json
import iso8601

newsapi = NewsApiClient(api_key = "78b9d599c4f94f8fa3afb1a5458928d6")

class News():
    def __init__(self):
        pass
    
    def search(self, q, category):
        top_headlines = newsapi.get_top_headlines(q = q, category = category)
        return top_headlines

def process_date(date):
    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    parsed = iso8601.parse_date(date)
    return months[parsed.month-1] + " " + str(parsed.day) + ", " + str(parsed.year)

# print(process_date("2020-11-06T15:30:00Z"))

# test = News()
# temp = test.search("anne hathaway", "entertainment")
# for article in temp["articles"]:
#      print(article["url"])
#      print(article["publishedAt"])
#      print()


