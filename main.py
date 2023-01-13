
import requests
from bs4 import BeautifulSoup
import sys 

#page = requests.get('https://www.bazos.cz/search.php?hledat=mazda+mx5&hlokalita=&humkreis=25&cenaod=10000&cenado=&order=1')
# Create a BeautifulSoup object

with open("/home/fedurca/Documents/webreader/webreader/ad.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

#soup = BeautifulSoup(page.text, 'html.parser')
# get the repo list
# repo = soup.find(class_="repo-list")

#print(type(soup))
#print(soup.)

inzeraty = soup.find_all(class_="inzeraty inzeratyflex") 

#nadpis = soup.find_all(class_="nadpis")

#cena = soup.find_all(class_="inzeratycena")

pozice = 0


for tag in inzeraty:
    print(pozice)
    nadpis = soup.find(class_='nadpis')
    #print(type(nadpis))
    #<class 'bs4.element.Tag'>
    nadpis_plain = nadpis.get_text().strip()
    print(nadpis_plain)
    
    cena = soup.find(class_='inzeratycena')
    cena_plain = cena.get_text().strip()
    print(cena_plain)
    pozice += 1

sys.exit()
