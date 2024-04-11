from bs4 import BeautifulSoup
import requests

#change this depending on the vlr stats page that you want it to scrape from
url = "https://www.vlr.gg/event/stats/1921/champions-tour-2024-masters-madrid?exclude=&min_rounds=0&agent=all"

results = requests.get(url)
doc = BeautifulSoup(results.text, "html.parser")
print(doc.prettify())

#need to save the data <tbody> tags on the page, which contain <tr>
#tags, which hold the player stats
#this can then be converted into some dataframe/file
