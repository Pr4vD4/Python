import requests as rq
import bs4

def get_title():
    url = 'https://ngknn.ru/'
    response = rq.get(url)
    return bs4.BeautifulSoup(response.text, 'html.parser').select_one('#content > div.item-page > div > div.page-header.text-center > h2').text
