import pandas as pd

data = {'datetime_with_tz': ['2023-11-25T10:00:00+05:30', '2023-11-24T09:00:00-08:00', '2023-11-25T12:00:00+00:00']}
df = pd.DataFrame(data)

df['datetime_with_tz'] = pd.to_datetime(df['datetime_with_tz'], utc=True)

df.sort_values(by='datetime_with_tz', inplace=True)

print(df)