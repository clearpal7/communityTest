import requests
import re
import logging
from bs4 import BeautifulSoup


class CoinPannCrawler:

    def __init__(self, page, markup='lxml', timeout=5):
        self.session = requests.session()
        self.markup = markup
        self.page = page
        self.timeout = timeout

    def get_html_text(self):
        url = "http://coinpan.com/free"
        payload = {'mid': 'free', 'page': self.page}
        headers = {
            'Accept': 'text/html,application/xhtml_xml,application/xml;q=0.9,*/*;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 FireFox/57.0'
        }
        r = requests.get(url, params=payload, headers=headers)
        return r.text