from playwright.sync_api import sync_playwright
from selectolax.parser import HTMLParser
from dataclasses import dataclass
import json
import os
from bs4 import BeautifulSoup

@dataclass
class ProductDetails:
    asin: str
    name: str
    price: str
    imagelink: str
    rating: str


def scrapeAmazon(url):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto(url=url, timeout=300000000)
        soup = BeautifulSoup(page.content(), 'html.parser')
        try:
            name = soup.find(class_="a-size-large").text.strip()
            price = soup.find(class_="a-price-whole").text
            imagelink = soup.find(class_="a-dynamic-image").attrs['src']
            rating = soup.find(class_="a-icon-alt").text.replace(" out of 5 stars", "")
            link = url.split('/')
            if link[-2]=="dp":
                splited_link = link[-1].split('?')
                asin = splited_link[0]
                print(asin)
            elif link[-2]=="d":
                asin=link[-1]
                print(asin)   
            else:
                # splited_link = link[-1].split('?')
                asin = link[-2]
                print(asin)
            print(name)
            print(price)
            print(imagelink)
            print(rating)
            product_details = ProductDetails(
                asin=asin,
                name=name,
                price=price,
                imagelink=imagelink,
                rating=rating
            )

            jsonstr = json.dumps(product_details.__dict__)

            with open("data.json", "w") as jsonfile:
                jsonfile.write(jsonstr)
                jsonfile.close()
        except:
            product_details = ProductDetails(
                asin=None,
                name=None,
                price=None,
                imagelink=None,
                rating=None
            ) 
            jsonstr = json.dumps(product_details.__dict__)

            with open("data.json", "w") as jsonfile:
                jsonfile.write(jsonstr)
                jsonfile.close()     

if __name__=='__main__':
    with open("url.txt", "r") as f:
        url = f.read()
        f.close()

    scrapeAmazon(url=url)