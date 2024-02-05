from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from dataclasses import dataclass
import json
import os

@dataclass
class Item:
    title: str
    price: str

def checkFlipkart(name):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://www.flipkart.com/search?q="+ name)
        soup = BeautifulSoup(page.content(), 'html.parser')
        title=soup.find_all(class_="_4rR01T"),
        price=soup.find_all(class_="_30jeq3 _1_WHN1")
        if str(title[0][0].text) == name:
            item = Item(
                title=title[0][0].text.strip(),
                price=price[0].text.strip().replace('\u20b9', '')
            )
        else:
            item = Item(
                title=title[0][1].text.strip(),
                price=price[1].text.strip().replace('\u20b9', '')
            )
    
        itemstr = json.dumps(item.__dict__)
        with open('datacompareflpk.json', 'w') as jsonfile:
            jsonfile.write(itemstr)
    
def checkAmazon(name):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto("https://www.amazon.in/s?k=" + name)
        soup = BeautifulSoup(page.content(), 'html.parser')
        title=soup.find_all('span', class_='a-size-medium'),
        price=soup.find_all(class_='a-price-whole')
        if str(title[0][0].text) == name:
            item = Item(
                title=title[0][0].text.strip(),
                price=price[0].text.strip()
            )
        else:
            item = Item(
                title=title[0][1].text.strip(),
                price=price[0].text.strip()
            )
        
        itemstr = json.dumps(item.__dict__)    
        with open('datacompareamaz.json', 'w') as jsonfile:
            jsonfile.write(itemstr)


if __name__=='__main__':
    with open('name.txt', 'r') as f:
        name = f.read()
    print(name)
    checkFlipkart(name=name)
    checkAmazon(name=name)
    os.remove('name.txt')