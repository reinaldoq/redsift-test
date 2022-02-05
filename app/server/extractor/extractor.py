import requests
from bs4 import BeautifulSoup


class Extractor:
    def get_titles(self, urls):
        titles = []
        for url in urls:
            try:
                reqs = requests.get(url)
            except:
                pass
            soup = BeautifulSoup(reqs.text, 'html.parser')
            for title in soup.find_all('title'):
                titles.append(title.get_text())
        return titles
