import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

pages = []

for i in range(1,5):
    url = 'https://web.archive.org/web/20121007172955/http://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    # print(soup)

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')
    # print(artist_name_list_items)

    for artist_name in artist_name_list_items:
        # print(artist_name.prettify())
        name = artist_name.contents[0]
        link = 'https://web.archive.org' + artist_name.get('href')
        # print(name)
        # print(link)
        f.writerow([name, link])
