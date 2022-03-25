from pprint import pprint
import requests
import bs4

url = 'https://habr.com/ru/all'
headers = {
    'authority': 'www.kith.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en-US,en;q=0.9',
}
KEYWORDS = ['фото', 'дизайн', 'web', 'python']

response = requests.get(url, headers=headers)
response.raise_for_status()
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
# print(articles)

for article in articles:
    title = article.h2.string
    paragraphs = article.find_all('p')
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    date = article.find(class_='tm-article-snippet__datetime-published')
    paragraphs = set(paragraph.text.strip() for paragraph in paragraphs)
    hubs = set(hub.text.strip() for hub in hubs)
    href = url + article.h2.a['href']

    if None in (title, paragraphs, hubs, date, href):
        continue
    keywords_ = set(KEYWORDS)

    preview_info = str(title.text.lower() + str(paragraphs).lower() + str(hubs).lower()).split()
    # print(preview_info)

    for keyword in keywords_:
        if keyword in preview_info:
            pprint(title.text + ' ' + date.text + ' ' + href)





