from bs4 import BeautifulSoup
import requests
import csv

#open with google sheets to test

def scrapeStats(url):
    getResponse = requests.get(url)
    #verifying successful request response
    if getResponse.status_code == 200:
        #parse HTML content
        doc = BeautifulSoup(getResponse.content, "html.parser")
        #saving only table data
        table = doc.find(class_='wf-card mod-table mod-dark')
        headers = []
        rows = []
        #extract and fill the header and row arrays with table data 
        for th in table.find_all('th'):
            headers.append(th.text.strip())
        for tr in table.find_all('tr')[1:]:
            row = []
            for td in tr.find_all('td'):
                row.append(td.text.strip())
            rows.append(row)
        return headers, rows
    else:
        #in case of unsuccessful request response
        print("Request Error")
        return None, None

def clean_data(headers, rows):
    #appending new team column
    for row in rows:
        player_name = row[0]
        team_name = player_name.split()[-1]
        row.append(team_name)
    #deleting redundant agents column
    agents_index = headers.index('Agents')
    for row in rows:
        del row[agents_index]
    del headers[agents_index]

def save_to_csv(headers, rows, fileName):
    with open(fileName, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        #write headers and rows
        #create team header
        writer.writerow(headers + ['Team'])
        for row in rows:
            writer.writerow(row)
    print(f"Data has been saved to {fileName}")

def main():
    #change this depending on the vlr stats page that you want it to scrape from
    url = "https://www.vlr.gg/event/stats/1921/champions-tour-2024-masters-madrid?exclude=&min_rounds=0&agent=all"
    #created CSV file name 
    fileName = 'vlr_stats.csv'
    #scraping data
    headers, rows = scrapeStats(url)
    #check data is retrieved successfully
    if headers and rows:
        #clean data
        clean_data(headers, rows)
        #save data to CSV file
        save_to_csv(headers, rows, fileName)

if __name__ == "__main__":
    main()