# This file scraps info required for the desktop app
from bs4 import BeautifulSoup
import requests

def print_rasifal(index):

    url = "https://www.hamropatro.com/rashifal"

    page = requests.get(url)
    doc = BeautifulSoup(page.text, "html.parser")
    rasifal_container = doc.find_all("div", {"id": "rashifal"})[0]

    rasifal_class = rasifal_container.find_all("div", {"class": "desc"})[index]
    rasifal = rasifal_class.p

    print(rasifal.string)