from bs4 import BeautifulSoup
import requests
import csv

def scrapeStats(url):

    getResponse = requests.get(url)

    #checking for a successful response from the request
    if getResponse.status_code == 200:
        doc = BeautifulSoup(getResponse.text, "html.parser")
        print(doc.prettify())


def save_to_csv(headers, rows, fileName):

    with open(fileName, 'w', newLine='') as csvFile:
        writer = csv.writer(csvFile)

def main():

    #change this depending on the vlr stats page that you want it to scrape from
    url = "https://www.vlr.gg/event/stats/1921/champions-tour-2024-masters-madrid?exclude=&min_rounds=0&agent=all"

    fileName = 'vlr_stats.csv'















#need to save the data <tbody> tags on the page, which contain <tr>
#tags, which hold the player stats
#this can then be converted into some dataframe/file
