import requests
from bs4 import BeautifulSoup
import sys 
from copy import deepcopy

read_from_web = 0

if (read_from_web):
    page = requests.get('https://www.bazos.cz/search.php?hledat=mazda+mx5&hlokalita=&humkreis=25&cenaod=10000&cenado=&order=1')
    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    # get the repo list
else:
    with open("ad.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')


#print(type(soup))
#print(soup.)

inzeraty = soup.find_all(class_="inzeraty inzeratyflex") 
#nadpis = soup.find_all(class_="nadpis")
#cena = soup.find_all(class_="inzeratycena")
pozice = 0
inzerat = {}
data_inzeratu = {}

for tag in inzeraty:
    #print(pozice)
    #print(tag.get_text())
    nadpis = tag.find(class_='nadpis')
    #print(type(nadpis))
    #<class 'bs4.element.Tag'>
    nadpis_plain = nadpis.get_text().strip()
    #print(nadpis_plain)
    #print(nadpis_plain)
    cena = tag.find(class_='inzeratycena')
    cena_plain = cena.get_text().strip()
    inzerat["id"] = deepcopy(pozice)
    inzerat["nadpis"] = deepcopy(nadpis_plain)
    inzerat["cena"] = deepcopy(cena_plain)
    data_inzeratu[pozice] = [deepcopy(inzerat)]
    #print(pozice)
    #print(inzerat)
    #print(data_inzeratu[pozice])
    #print(cena_plain)
    pozice += 1

print("")
print("")

print(data_inzeratu)

cena_vseho_dohromady = 0
pocet_inzeratu = len(data_inzeratu)
pocet_inzeratu = 20 

i=0
while(i<pocet_inzeratu):
    cena_inzeratu = data_inzeratu.get(i)[0]
    #print(type(cena_inzeratu))
    #print(cena_inzeratu['cena'])
    #print(cena_inzeratu['cena'][:-3])
    cena_inzeratu=int(cena_inzeratu['cena'][:-3].replace(" ", ""))
    print(cena_inzeratu)
    cena_vseho_dohromady = cena_vseho_dohromady + cena_inzeratu
    i = i+1


print("cena za",pocet_inzeratu, "nejlevnějších věcí je",  cena_vseho_dohromady)

#print(inzerat["id"])
#print(inzerat["nadpis"])
#print(inzerat["cena"])
sys.exit()




