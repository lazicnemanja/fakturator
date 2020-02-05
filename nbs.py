from bs4 import BeautifulSoup
import requests 

class NBS():
    def __init__(self,url):
        self.url = url
        self.__eur = 0
        self.soup = self.__get_nbs_data()

    def __get_nbs_data(self):
        r = requests.get(url = self.url) 
        return BeautifulSoup(r.text, features="html.parser")

    def formed_on(self):
        rows = self.soup.select('table tbody tr')
        cells = rows[0].select('td')
        nbs_date_raw = cells[0].select('span')[-2].text
        return nbs_date_raw.replace("/",".")

    def eur_exchange_rate(self):
        if self.__eur > 0:
            return self.__eur

        rows = self.soup.select('table tbody tr')
        cells = rows[1].select('td')
        if cells[2].string == 'EUR':
            self.__eur = float(cells[-1].string)
            return float(cells[-1].string)