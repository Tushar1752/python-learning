#news api question

import requests
import json

query=input("Enter what type of news you like the most:")
url=f"https://newsapi.org/v2/top-headlines?country=in&apiKey=dc002e47ead743d199d42e9343c43cfd&category={query}"
response=requests.get(url)
news=json.loads(response.text)
print(response.text) 
print(news,type(news))

for article in news['articles']:
    print(article['title'])
    print(article['description'])
    print(article['url'])