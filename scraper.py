import requests
from openpyxl import *
from bs4 import BeautifulSoup


def scrapebay(request, filename):
    wb = Workbook()
    ws = wb.active

    ws.append(['Title', 'Price', 'Image Link', 'URL'])
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={request}&_sacat=0&_sop=15'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='s-item__wrapper clearfix')
    for i in items:
        img = i.div.img['src']
        urlX = i.a['href']
        title = i.text
        price = i.find('span', class_='s-item__price').text
        row = [title, price, img, urlX]
        ws.append(row)

    wb.save(f'{filename}.xlsx')
