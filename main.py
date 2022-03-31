import pandas as pd                                      # Untuk data manipulation
from bs4 import BeautifulSoup                            #
from selenium import webdriver                           # Untuk membuka web secara otomatis
from selenium.webdriver.chrome.options import Options    #

#Link digimap
url = 'https://shopee.co.id/shop/255563049/search?page=0&sortBy=pop'
path = 'C:\webdrivers\chromedriver.exe'

#Customize chrome display
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')

datas = []
pageNumber = 0
for page in range(0,2):
    pageNumber += 1
    # print("Page : ", pageNumber)
    driver = webdriver.Chrome(executable_path=path, options=chrome_options)
    driver.get(url)

    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
    soup = BeautifulSoup(html, "html.parser")
    items = soup.findAll('div', 'shop-search-result-view__item col-xs-2-4')

    for i in items :
        name = i.find('div' , '_10Wbs- _2STCsK _3IqNCf').text
        print(name)