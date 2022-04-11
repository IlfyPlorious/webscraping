import os.path

from bs4 import BeautifulSoup
from distutils import util
import requests
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                               chrome_options=chrome_options)
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



#??? why it's not working


f = open("page.txt", "r")
print(getProduseFromPage(f))
