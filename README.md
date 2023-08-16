# HASS-AD-WebScraper
Webscrapers for Homeassistant with Appdaemon

## Setup
- Install Appdaemon. Follow these instructions: https://appdaemon.readthedocs.io/en/latest/INSTALL.html
- Connect Appdaemon to Homeassistant by getting a long lived token in HA and inserting it in the appdaemon.yaml config.
- Put the YOUR_SCRIPT.py in the /conf/apps/ folder
- Add the contents apps.yaml or if not existent put apps.yaml in /conf/apps/
- Put requirements.txt in /conf folder (this downloads the library for the script to work)
- Add the contents of the configuration.yaml to your HA configuration.yaml (creates a virtual sensor)
- Add the contents of automation.yaml to your HA automation.yaml. This adds a periodic event called SCRAPE_LECH_TEMP, which in return triggers the script which then updates the sensor

## Scrapers
- Scrapes temperature for this page: https://www.nid.bayern.de/wassertemperatur/iller_lech/augsburg-hochablass-12004002
