import requests
from bs4 import BeautifulSoup

#step 1 (scraping/ extrating)
URL = "https://www.moneycontrol.com/india/stockpricequote/"
RAW_HTML_STRING = requests.get(URL)


#step 2 (parsing)
PARSED_HTML = BeautifulSoup(RAW_HTML_STRING.content, 'html.parser')
a_tags = PARSED_HTML.find_all('a', class_="bl_12")


#step 3 (save the data)
f = open("data.csv", "w")
for a in a_tags:
    f.write(a.get_text() + "," +  a.get("href") + "\n")
f.close()