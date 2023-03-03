import requests
from bs4 import BeautifulSoup
import sys 
from copy import deepcopy
 
read_from_web = 1
 
if (read_from_web):
    page = requests.get('https://www.alza.cz/mobily/18843445.htm')
    soup = BeautifulSoup(page.text, 'html.parser')
#else:
#    with open("") as fp:
#        soup = BeautifulSoup(fp, 'html.parser')
 
 
inzeraty = soup.find_all(class_="price-box__price") 
pozice = 0
inzerat = {}
data_inzeratu = {}

print(soup)

 
for tag in inzeraty:
    nadpis = tag.find(class_='name browsinglink impression-binded')
    nadpis_plain = nadpis.get_text().strip()
    cena = tag.find(class_='price-box__price')
    cena_plain = cena.get_text().strip()
    inzerat["id"] = deepcopy(pozice)
    inzerat["nadpis"] = deepcopy(nadpis_plain)
    inzerat["cena"] = deepcopy(cena_plain)
    data_inzeratu[pozice] = [deepcopy(inzerat)]
    pozice += 1
 
print("")
print("")
 
print(data_inzeratu)
sys.exit() 
cena_vseho_dohromady = 0
pocet_inzeratu = len(data_inzeratu)
pocet_inzeratu = 20 
 
i=0
while(i<pocet_inzeratu):
    cena_inzeratu = data_inzeratu.get(i)[0]
    print(cena_inzeratu)
    cena_inzeratu=int(cena_inzeratu['cena'][:-3].replace(" ", ""))
    print(cena_inzeratu)
    cena_vseho_dohromady = cena_vseho_dohromady + cena_inzeratu
    i = i+1
 
 
print("cena za",pocet_inzeratu, "nejlevnějších věcí je",  cena_vseho_dohromady)
 
 
sys.exit()