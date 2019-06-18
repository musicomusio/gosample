import time
import sys
from urllib.parse import urlencode
from urllib.parse import urljoin
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

base_url = "https://search.rakuten.co.jp/search/mall/"
shop_id  = "sid=279082"

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
#driver = webdriver.Chrome(chrome_options=options)


urllist = []
# https://search.rakuten.co.jp/search/mall/?p=2&sid=279082

def query_url(base,counter):
    
    args = {"p": counter,"sid": "279082"}
    res = base_url + "?{}".format(urlencode(args))
    return res

for i in range(1,28):
    targetpage = query_url(base_url,i)
    print(targetpage)
    driver.get(targetpage)
    WebDriverWait(driver, 1)
    v = driver.find_elements_by_css_selector(".searchresultitem > .image > a")
    for t in v:
        urllist.append(t.get_attribute("href"))


driver.close()

with open("./test.csv", 'w' ) as f:
    for data in urllist:
        print(data, file=f)

sys.exit()
