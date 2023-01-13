
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

for tag in inzeraty:
    
    nadpis = soup.find(class_='nadpis')
    #print(type(nadpis))
    #<class 'bs4.element.Tag'>
    nadpis_plain = nadpis.get_text().strip()
    print(nadpis_plain)
    
    cena = soup.find(class_='inzeratycena')
    cena_plain = cena.get_text().strip()
    print(cena_plain)
    #print(record.contents[3])
    #print(tag.contents[1])
    #print(next(tag.children).strip())
    #print(next(tag.strings).strip())
    #print(next(tag.stripped_strings))
    break
    # record.contents[0]
#print(repo)

sys.exit()

# get the repo list
nadpis = soup.find(class_="nadpis")

cena = soup.find(class_="inzeratycena")



# find all instances of that class (should return 25 as shown in the github main page)
#repo_list = repo.find_all(class_='inzeratycena')

#print(len(repo_list))

for zaznam in repo:
    print(zaznam)
    # find the first <a> tag and get the text. Split the text using '/' to get an array with developer name and repo name
    # full_repo_name = repo.find('a').text.split('/')
    # extract the developer name at index 0
    # developer = full_repo_name[0].strip()
    # extract the repo name at index 1
    # repo_name = full_repo_name[1].strip()
    # find the first occurance of class octicon octicon-star and get the text from the parent (which is the number of stars)
    # stars = repo.find(class_='octicon octicon-star').parent.text.strip()
    # strip() all to remove leading and traling white spaces
    # print('developer', developer)
    # print('name', repo_name)
    # print('stars', stars)