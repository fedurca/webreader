
import requests
from bs4 import BeautifulSoup
import sys 

page = requests.get('https://github.com/trending')
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
# get the repo list
repo = soup.find(class_="repo-list")

print(type(soup))
print(soup.text)

sys.exit()

# find all instances of that class (should return 25 as shown in the github main page)
repo_list = repo.find_all(class_='col-12 d-block width-full py-4 border-bottom')

print(len(repo_list))

for repo in repo_list:
    # find the first <a> tag and get the text. Split the text using '/' to get an array with developer name and repo name
    full_repo_name = repo.find('a').text.split('/')
    # extract the developer name at index 0
    developer = full_repo_name[0].strip()
    # extract the repo name at index 1
    repo_name = full_repo_name[1].strip()
    # find the first occurance of class octicon octicon-star and get the text from the parent (which is the number of stars)
    stars = repo.find(class_='octicon octicon-star').parent.text.strip()
    # strip() all to remove leading and traling white spaces
    print('developer', developer)
    print('name', repo_name)
    print('stars', stars)