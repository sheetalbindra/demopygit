import pandas as pd
from datetime import datetime

df = pd.read_excel('NYT Movies.xlsx')

df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')

df.sort_values(by='published_date', inplace=True)

movies_dict = {}

for d in range(1, len(df)):
    title = df["title"].iloc[d]
    date = df["published_date"].iloc[d].date()

    if date in movies_dict:
        movies_dict[date].append(title)
    else:
        movies_dict[date] = [title]

print(movies_dict)

movies_data = []

for date, titles in movies_dict.items():
    movies_data = [[date, title] for title in titles]
    movies_df = pd.DataFrame(movies_data, columns=['published_date', 'title'])

    file_name = f'movies_{date}.xlsx'

    movies_df.to_excel(file_name, index=False)

    print(f"Saved {file_name}")
