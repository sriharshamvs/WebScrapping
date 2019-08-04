import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

url_list = []
headings_name= ['State', 'Constituency', 'O.S.N.', 'Candidate', 'Party', 'EVM Votes', 'Postal Votes', 'Total Votes', '% of Votes']
headings = []
data = []
candidate = []

with open('links.txt', 'r') as linksFile:
    for url in linksFile:
        url_list.append(url)

with open('ElectionResults.csv','w') as ERfile:
    writer = csv.writer(ERfile)
    writer.writerow(headings_name)

for link in url_list:
    page = requests.get(link)
    soup = BeautifulSoup(page.text, "lxml")

    table = soup.find('table', class_='table-party')

    headings = []
    data =[]

    for th in table.find_all('th'):
        headings.append((th.text).strip('\r\n').strip(" ").rstrip())

    state, const = headings[0].split("-",1)
    headings.remove(headings[0])
    headings.remove(headings[1])

    for tr in table.find_all('tr'):
        candidate = [state, const]
        for td in tr.find_all('td'):
            td = td.string
            candidate.append(td)
        if len(candidate) != 2:
            data.append(candidate)

    for result in data:
        with open('ElectionResults.csv','a') as ERfile:
            writer = csv.writer(ERfile)
            print(result)
            writer.writerow(result)
            sleep(0.1)
