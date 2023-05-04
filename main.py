import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

sitemap_index_url = "https://www.bloomberg.com/feeds/bbiz/sitemap_index.xml"
response = requests.get(sitemap_index_url)
soup = BeautifulSoup(response.content, "xml")

sitemap_urls = [loc.text for loc in soup.find_all("loc")]

#driver = webdriver.Chrome()
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get(sitemap_urls[0])
soup1 = BeautifulSoup(driver.page_source, "xml")
urls = [loc1.text for loc1 in soup1.find_all("loc")]

driver.get(urls[0])
driver
time.sleep(5)
a=driver.title

soup2 = BeautifulSoup(driver.page_source, "xml")
title=soup2.find("h3").text
time=soup2.find("div").text

import pandas as pd
data=pd.DataFrame([{"Title":title,
                  "Time":time}])
                  
data.to_json("news8.json")
