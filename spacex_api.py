import requests
import pandas as pd


def spacex_api():
    url = 'https://api.spacexdata.com/v5/launches/'
    response = requests.get(url)
    data = response.json()
    return data

launch_data = spacex_api()

df = pd.DataFrame(launch_data)
print(df)