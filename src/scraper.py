



import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP request errors

    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text_content = '\n'.join(p.get_text() for p in paragraphs)

    return text_content

# URL of the webpage to scrape
page_url = "YOUR_WEBPAGE_URL_HERE"
page_url='https://contracts.justia.com/companies/amgen-inc-93/contract/565667/'

# Function call to scrape text
scraped_text = scrape_text(page_url)
# write to file 
with open('../data/raw/agreement.txt','w',encoding='utf-8') as file:
    file.write(scraped_text)

#
#print(scraped_text)

