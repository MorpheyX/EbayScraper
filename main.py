from scraper import scrapebay
request = input('request: ')
filename = input('spreadsheet filename: ')

if __name__ == "__main__":
    scrapebay(request, filename)
