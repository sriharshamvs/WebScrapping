import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

f = csv.writer(open('links.csv', 'a'))
#f.writerow(['link'])

def CheckStateLinkAndSave(state, constituency):
    state = state.zfill(2)
    link = 'http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseS'+ state + constituency + '.htm?ac=' + constituency
    page = requests.get(link)
    sleep(1)
    if page.status_code == 200:
        f.writerow([link])
    print(state, constituency, page)

def CheckUTLinkAndSave(UT, UT_constituency):
    UT = UT.zfill(2)
    link = 'http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU'+ UT + UT_constituency + '.htm?ac=' + UT_constituency
    page = requests.get(link)
    sleep(1)
    if page.status_code == 200:
        f.writerow([link])
    print(UT, UT_constituency, page)

for state in range(1, 27):
    if state == 24:
        for constituency in range(1,81):
            CheckStateLinkAndSave(str(state), str(constituency))
    else:
        for constituency in range(1,50):
            CheckStateLinkAndSave(str(state), str(constituency))

for UT in range(1,8):
    for UT_constituency in range(1,7):
        CheckUTLinkAndSave(str(UT), str(UT_constituency))
