# import requests
# URL = 'https://wallpaperaccess.com/galaxy-hd-phone'
# page = requests.get(URL)
# print(page)
import cfscrape
scraper = cfscrape.create_scraper()
print(scraper.get("https://wallpaperaccess.com/galaxy-hd-phone").content)
