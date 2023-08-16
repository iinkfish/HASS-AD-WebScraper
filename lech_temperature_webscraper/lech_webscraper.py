import appdaemon.plugins.hass.hassapi as hass
import requests
from bs4 import BeautifulSoup

class LechWebscraper(hass.Hass):

    def initialize(self):
        self.listen_event(self.scrapePage, "SCRAPE_LECH_TEMP")


    def scrapePage(self, event_name, data, kwargs):
        self.log("Beginning webscraping")
        html_lech = requests.get('https://www.nid.bayern.de/wassertemperatur/iller_lech/augsburg-hochablass-12004002').text

        soup = BeautifulSoup(html_lech, 'lxml')
        temperatures = soup.find_all('td')
        timestamps = soup.find_all('td', class_='row')
        self.log("fetched temperature " + temperatures[1].text)
        #self.log(self.get_state(entity_id = "sensor.lech_temperatur", attribute = "all"))
        self.set_state(entity_id = "sensor.lech_temperatur", state = temperatures[1].text)
