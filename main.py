import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
sitemap_index_url = "https://www.bloomberg.com/feeds/bbiz/sitemap_index.xml"
response = requests.get(sitemap_index_url)
soup = BeautifulSoup(response.content, "xml")

sitemap_urls = [loc.text for loc in soup.find_all("loc")]

driver = webdriver.Chrome()
driver.get(sitemap_urls[0])
soup1 = BeautifulSoup(driver.page_source, "xml")
urls = [loc1.text for loc1 in soup1.find_all("loc")]
driver.get(urls[0])
driver
time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html")
title=soup.find("h1").text
time=soup.find("time").text

import pandas as pd
data=pd.DataFrame([{"Title":title,
                  "Time":time}])
                  
data.to_csv("news.csv")
