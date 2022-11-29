import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.nhsinform.scot/illnesses-and-conditions/a-to-z#B')

# check status code for response received
# success code - 200
print(r)

# print content of request
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find_all('a')
 
f = open("symptoms.csv", "w")
for tag in s:
    f.write(tag.get_text().strip() + "," + "https://www.nhsinform.scot" + tag.get('href').strip() + "\n")
    
f.close()
    