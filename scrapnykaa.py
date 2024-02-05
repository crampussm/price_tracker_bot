from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
from dataclasses import dataclass

@dataclass
class ProductDetails:
    name: str
    price: str
    ratings: str
    image: str

def scrapeNykaa(url):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto(url=url, timeout=300000000)
        soup = BeautifulSoup(page.content(), 'html.parser')
        name = soup.find(class_="css-1gc4x7i").text
        price = soup.find(class_="css-1jczs19").text.replace("\u20b9", "")
        rating = soup.find(class_="css-m6n3ou").text.replace("/5", "")
        imageParent = soup.find(class_="css-ile3gb")
        imagelink = imageParent.findChild('img', recursive=False).attrs['src']
        print(type(name))
        print(type(price))
        print(type(rating))
        print(type(imagelink))
        product_details = ProductDetails(
            name=name,
            price=price,
            ratings=rating,
            image=imagelink
        )
        jsonstr = json.dumps(product_details.__dict__)

        with open("data.json", "w") as jsonfile:
            jsonfile.write(jsonstr)



if __name__=='__main__':
    with open("url.txt", "r") as f:
        url = f.read()
        f.close()

    # os.remove("url.txt")
    scrapeNykaa(url=url)            