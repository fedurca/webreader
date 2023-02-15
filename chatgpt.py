'''
write simple python code to scrape ads from website bazos.cz parse them and store its data in pandas dataframe
Here is a simple Python code to scrape ads from the website bazos.cz, parse the data, and store it in a Pandas DataFrame:
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup

#url = 'https://www.bazos.cz/search.php?hledat=mazda+mx5&rubriky=www&hlokalita=&humkreis=25&cenaod=&cenado=&Submit=Hledat&kitx=ano'
#res = requests.get(url)
#soup = BeautifulSoup(res.text, 'html.parser')

read_from_web = 0

if (read_from_web):
    page = requests.get('https://www.bazos.cz/search.php?hledat=mazda+mx5&hlokalita=&humkreis=25&cenaod=10000&cenado=&order=1')
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    # get the repo list
else:
    with open("ad.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')



ads = soup.find_all('div', {'class': 'inzeraty inzeratyflex'})

data = []
for ad in ads:
    title = ad.find('h2', {'class': 'nadpis'}).text
    price = ad.find('div', {'class': 'inzeratycena'}).text
    location = ad.find('div', {'class': 'inzeratylok'}).text
    data.append([title, price, location])
    #print(type(ad))
    #print(ad.text)
    #break

df = pd.DataFrame(data, columns=['Title', 'Price', 'Location', 'Text'])

print(df)