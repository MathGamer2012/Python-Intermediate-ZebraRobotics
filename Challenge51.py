import urllib.request
import json

serverRequest = "https://newsapi.org/v2/top-headlines?country=us&apiKey=7b96e57e64d14a7c999918c200e8766e"
res = urllib.request.urlopen(serverRequest)
data = json.loads(res.read().decode("utf-8"))

for i in data["articles"]:
    print(i["title"]) 
