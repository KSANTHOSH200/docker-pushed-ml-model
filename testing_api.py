import requests
import json

url = "http://127.0.0.1:8000/"
que = "Explain queries in NLP"

params = {"query": que}

response = requests.get(url, params = params)

print("response is: ", response)

print("title: ", json.loads(response.text)['title'])

print(requests.get("http://127.0.0.1:8000/").text)
