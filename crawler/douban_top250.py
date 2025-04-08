import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

response = requests.get("https://movie.douban.com/top250",headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('div', class_='item')
for item in items:
    title = item.find('span', class_='title').text.strip()
    rating = item.find('span', class_='rating_num').text.strip()
    print(f"电影名称：{title}，评分：{rating}")