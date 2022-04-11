from bs4 import BeautifulSoup
from distutils import util
import requests
from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# session = HTMLSession()
# r = session.get("https://www.emag.ro/")
# r.html.render()
# html = r.text
#
# soup = BeautifulSoup(html, 'lxml')
# html = soup.find_all()
# containers = soup.find_all('h2')

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.emag.ro/")

browser.set_window_position(0, 0)
browser.set_window_size(1920, 1080)

item = browser.find_element(by=By.XPATH, value="//*[@data-id='23']")
# produse = browser.find_element(by=By.XPATH, value="//*[@class='em em-burger']")
# produse.click()
hover = ActionChains(browser).move_to_element(item)
hover.perform()

promo = browser.find_element(by=By.XPATH, value="//*[@class='label label-success']")
promo.click()

page = browser.page_source

print(page)

browser.quit()
# print(item)

# html = browser.page_source
#
# soup = BeautifulSoup(html, 'lxml')
# container = soup.find('div', 'card-v2')
# topFav = container.find_all("span", string='Top Favorite')
#
# print(container)
# caut spanurile care contin Top Favorite si verific lungimea resultSetului
# in functie de care stabilesc daca retin informariile sau nu

# for span in topFav:
#     print(span)
#     print("\n\n")





