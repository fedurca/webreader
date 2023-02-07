'''
write simple python code to scrape ads from website bazos.cz parse them and store its data in pandas dataframe
Here is a simple Python code to scrape ads from the website bazos.cz, parse the data, and store it in a Pandas DataFrame:
'''

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.bazos.cz/search.php?hledat=mazda+mx5&rubriky=www&hlokalita=&humkreis=25&cenaod=&cenado=&Submit=Hledat&kitx=ano'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

ads = soup.find_all('div', {'class': 'inzeraty inzeratyflex'})

data = []
for ad in ads:
    #title = ad.find('div', {'class': 'nadpis'}).text
    #price = ad.find('div', {'class': 'cena'}).text
    #location = ad.find('div', {'class': 'lokalita'}).text
    #data.append([title, price, location])
    print(type(ad))
    print(ad.text)
    break

df = pd.DataFrame(data, columns=['Title', 'Price', 'Location'])

print(df)