import requests
import pandas as pd

API_KEY = 'zTEF7McdCXoCQzCT5da9N4ENETzd06eJ'

BASE_URL = 'https://api.nytimes.com/svc/topstories/v2/{}.json'

section = 'movies'

url = BASE_URL.format(section)

params = {
    'api-key': API_KEY
}

response = requests.get(url, params=params)
movie = input("Enter the movie name you want to search for: ").lower()
if response.status_code == 200:
    data = response.json()
    # print(data,"\n")
    # print(type(data),"\n")
extracted_Data = data.get("results")
searched = []
for idx, d in enumerate(extracted_Data):
      if movie in d.get("title").lower():
        searched.append({"title":d.get("title"),"published_date":d.get("published_date"),"created_date":d.get("created_date")})
df = pd.DataFrame(searched)

print(searched)

excel_file = 'NYT Movies.xlsx'
df.to_excel(excel_file, index=False, sheet_name='NYT Movies')

print(f"Data has been successfully saved to {excel_file}")
df.to_excel('NYT Movies.xlsx')

#else:
#     print(f"Failed to fetch data: {response.status_code}")