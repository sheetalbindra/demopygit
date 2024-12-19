import requests
import json

api_key = 'zTEF7McdCXoCQzCT5da9N4ENETzd06eJ'
url = f'https://api.nytimes.com/svc/topstories/v2/arts.json?api-key={api_key}'

response = requests.get(url)

if response.status_code == 200:
    articles = response.json()
    for index, article in enumerate(articles['results']):
        print(f"{index}. {article['title']}")
else:
    print('Failed to fetch articles:', response.status_code)