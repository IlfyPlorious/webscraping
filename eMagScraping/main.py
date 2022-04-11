import os.path

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from database import *
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = os.path.join(ROOT_DIR, 'chromedriver')
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH


# /home/dragos/Drivers/chromedriver

def getPages(label):
    webpages = []
    classtag = ''

    if label == 'Promo':
        classtag = 'danger'
    else:
        classtag = 'success'

    # browser = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                               options=chrome_options)
    browser.get("https://www.emag.ro/")

    browser.set_window_position(0, 0)
    browser.set_window_size(1920, 1080)

    item = browser.find_element(by=By.XPATH, value="//*[@data-id='23']")

    hover = ActionChains(browser).move_to_element(item)
    hover.perform()

    nou = browser.find_elements(by=By.XPATH, value=f"//*[@class='label label-{classtag}']")

    nou[0].click()
    webpages.append(browser.page_source)
    secondpage = browser.find_element(by=By.XPATH, value="//*[@data-page='2']")
    secondpage.click()
    webpages.append(browser.page_source)

    for i in range(1, len(nou)):
        browser.back()
        item = browser.find_element(by=By.XPATH, value="//*[@data-id='23']")
        hover = ActionChains(browser).move_to_element(item)
        hover.perform()
        nou = browser.find_elements(by=By.XPATH, value=f"//*[@class='label label-{classtag}']")
        nou[i].click()
        webpages.append(browser.page_source)
        secondpage = browser.find_element(by=By.XPATH, value="//*[@data-page='2']")
        secondpage.click()
        webpages.append(browser.page_source)

    browser.quit()
    return webpages


def getProduseFromPage(page):
    soup = BeautifulSoup(page, 'lxml')
    containers = soup.find_all('div', 'card-item card-standard js-product-data')

    produse = []

    for container in containers:
        if container.find('span', 'card-v2-badge-cmp badge commercial-badge') is not None:
            badge = container.find('span', 'card-v2-badge-cmp badge commercial-badge').text
        else:
            badge = 'no'

        if 'Top Favorite' in badge.strip() or 'Super Pret' in badge.strip():
            categorie = badge.strip()
            produs_a = container.find('a', 'card-v2-title semibold mrg-btm-xxs js-product-url')
            produs = produs_a.text
            link = produs_a.get('href')

            produs = {
                'categorie': badge.strip(),
                'produs': produs.strip(),
                'link': link
            }

            produse.append(produs)

    return produse


def readEmagProducts():
    pages = getPages('Nou')
    pages.extend(getPages('Promo'))

    total_list = []

    for page in pages:
        total_list.extend(getProduseFromPage(page))

    return total_list


def write_all_to_database(total_list, database):
    for produs in total_list:
        if database[produs['categorie']].count_documents({'produs': produs['produs']}) == 0:
            write_one_to_collection(produs, produs['categorie'], database)


database = get_database('produse_emag')

print("""
<------------------------------------->


Hello! Aceasta aplicatie permite obtinerea produselor
cu eticheta Top Favorite sau Super Pret de pe site-ul eMag. 
Informatiile sunt preluate din baza de date de pe MongoDB.

Comenzi:
- obtine toate produsele >>>  toate
- filtreaza dupa Top Favorite >>>  top
- filtreaza dupa Super Pret >>>  super
- refresh baza de date >>>  refresh
- sterge colectie din baza de date !! folositi ghilimelele >>> purge "numele colectiei"
- inchide aplicatia >>> exit
- instructiu >>> help

""")

command = "first1"


def pretty_print(items):
    for item in items:
        print(item['produs'])
        print('\tcategorie: ', item['categorie'])
        print('\tlink: ', item['link'])
        print('\n\n')


while command != 'exit':

    if command == 'refresh':
        try:
            print('Loading... Dureaza putin pana se extrag datele. \n',
                  'Warningurile nu afecteaza rularea.\n',
                  'Daca refreshul esueaza rulati din nou comanda de refresh')
            products = readEmagProducts()
            write_all_to_database(products, database)
            print('Refresh completed')
        except:
            print('Refresh failed')
    elif command == 'toate':
        try:
            print('Extragem datele...\n')
            top = get_products_in_collection('Top Favorite', database)
            pret = get_products_in_collection('Super Pret', database)

            pretty_print(top)
            pretty_print(pret)

            print('Operatie finalizata!')
        except:
            print('Extragerea datelor a esuat')

    elif command == 'top':
        try:
            print('Extragem datele...\n')
            top = get_products_in_collection('Top Favorite', database)
            pretty_print(top)
            print('Operatie finalizata!')
        except:
            print('Extragerea datelor a esuat')

    elif command == 'super':
        try:
            print('Extragem datele...\n')
            pret = get_products_in_collection('Super Pret', database)
            pretty_print(pret)
            print('Operatie finalizata!')
        except:
            print('Extragerea datelor a esuat')
    elif 'purge' in command:
        collection = command[7:len(command)-1]
        try:
            print('Se sterge colectia ', collection.strip('"'))
            database[collection].drop()
            print('Colectie stearsa')
        except:
            print('Eroare la stergerea colectiei')
    elif command == 'help':
        print("""
Comenzi:
- obtine toate produsele >>>  toate
- filtreaza dupa Top Favorite >>>  top
- filtreaza dupa Super Pret >>>  super
- refresh baza de date >>>  refresh
- sterge colectie din baza de date !! folositi ghilimelele >>> purge "numele colectiei"
- inchide aplicatia >>> exit
- instructiu >>> help
        """)
    elif command == 'first1':
        pass
    else:
        print('! comanda necunoscuta !')

    print("\ncommand: ")
    command = input()
