import requests
from dotenv import load_dotenv
import os
import csv

load_dotenv()

def save_results_to_csv(results, csv_file_path):
    with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # CSV 파일의 첫 행에 헤더 추가 (첫 페이지에만 추가)
        if file.tell() == 0:
            writer.writerow(["title", "url", "excerpt", 'thumbnail', 'language', 'paywall', 'contentLength', 'date'])
                        
        for data in results['data']:
            title = data.get('title', 'N/A')
            url = data.get('url', 'N/A')
            excerpt = data.get('excerpt', 'N/A')
            thumbnail = data.get('thumbnail', 'N/A')
            language = data.get('language', 'N/A')
            paywall = data.get('paywall', 'N/A')
            contentLength = data.get('contentLength', 'N/A')            
            date = data.get('date', 'N/A')
            writer.writerow([title, url, excerpt, thumbnail, language, paywall, contentLength, date])

url = "https://news-api14.p.rapidapi.com/v2/search/articles"

querystring = {"query":"Los Angeles Housing Market", "language":"en", "from":"1y"}

headers = {
	"x-rapidapi-key": os.getenv('RAPIDNEWS_KEY'),
	"x-rapidapi-host": os.getenv('RAPIDNEWS_HOST')
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
csv_file_path = "articles_results.csv"

save_results_to_csv(data, csv_file_path)

#with open("rapid_news_nolimit.txt", "w") as file:
#        json.dump(data, file, indent=4)