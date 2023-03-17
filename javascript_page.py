
#from https://gist.github.com/AnderRV/ce1e59d4f626dfab25873cc98dea1c48
#pip install numpy selenium pandas webdriver_manager
import time
 
import pandas as pd
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
 
def parse_img_url(url):
    # get the first url
    url = url.split(", ")[0]
    # split it by `/`
    splitted_url = url.split("/")
    # loop over the elements to find where `cloudfront` url begins
    for idx, part in enumerate(splitted_url):
        if "cloudfront" in part:
            # add the HTTP scheme and concatenate the rest of the URL
            # then return the processed url
            return "https://" + "/".join(splitted_url[idx:])
    
    # as we don't know if that's the only measurement to take,
    # return None if the cloudfront couldn't be found
    return None 
 
def extract_data(element):
    img = element.find_element(By.TAG_NAME, "img").get_attribute("srcset")
    img = parse_img_url(img)
 
    # A>B means the B elements where A is the parent element.
    dietary_attrs = element.find_elements(By.CSS_SELECTOR, "div[class*='DietaryAttributes']>span")
    # if there aren't any, then `dietary_attrs` will be None and `if` block won't work
    # but if there are any dietary attributes, extract the text from them
    if dietary_attrs:
        dietary_attrs = [attr.text for attr in dietary_attrs]
    else:
        # set the variable to None if there aren't any dietary attributes found.
        dietary_attrs = None
 
    # get the span elements where the parent is a `div` element that 
    # has `ItemBCardDefault` substring in the `class` attribute
    price = element.find_elements(By.CSS_SELECTOR, "div[class*='ItemBCardDefault']>span")
    # extract the price text if we could find the price span
    if price:
        price = price[0].text
    else:
        price = None
 
    name = element.find_element(By.TAG_NAME, "h2").text
    size = element.find_element(By.CSS_SELECTOR, "div[class*='Size']").text
 
    return {
        "price": price,
        "name": name,
        "size": size,
        "attrs": dietary_attrs,
        "img": img
    }
 
# start by defining the options
options = webdriver.ChromeOptions()
options.headless = False # it's more scalable to work in headless mode
# normally, selenium waits for all resources to download
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none' 
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)
 
#url = "https://www.instacart.com/store/sprouts/collections/bread?guest=True"
url = "https://www.iwant.cz/iphone-c2372#s=pd"

 
driver.get(url)
time.sleep(1)
 
content = find_element( "div[class*='productList-item'")
#breads = content.find_elements(By.TAG_NAME, "productList-item-title")
 
data = []


print(type(content))
print(content)

sys.exit()
 
for bread in breads:
    extracted_data = extract_data(bread)
    data.append(extracted_data)
 
df = pd.DataFrame(data)
df.to_csv("result.csv", index=False)
 
driver.quit()