import requests
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_redfin_data(fromDb):
    url = "https://redfin-com-data.p.rapidapi.com/properties/auto-complete"

    querystring = {"query":fromDb}

    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": os.getenv("RAPIDAPI_HOST")
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    urls = []

    for item in data['data']:
        for row in item['rows']:
            urls.append(row['url'])

    latest_url = None
    
    for url in urls:
        print("url:", url)
        latest_url = "https://www.redfin.com"+url

    print("latest Url:", latest_url)
    url2 = "https://redfin-com-data.p.rapidapi.com/properties/detail-by-url"

    querystring2 = {"url":latest_url}

    response2 = requests.get(url2, headers=headers, params=querystring2)
    data2 = response2.json()
    return data2