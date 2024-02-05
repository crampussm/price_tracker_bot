from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
from dataclasses import dataclass

@dataclass
class ProductDetails:
    name: str
    price: str
    available_sizes: str
    image: str

def scrapeAjio(url):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto(url=url, timeout=300000000)
        soup = BeautifulSoup(page.content(), 'html.parser')
        namestr1 = soup.find(class_="brand-name").text
        namestr2 = soup.find(class_="prod-name").text
        name = f'{namestr1} {namestr2}'
        price = soup.find(class_="prod-sp").text
        sizeParent = soup.find_all(class_="size-instock")
        image = soup.find(class_="rilrtl-lazy-img img-alignment zoom-cursor rilrtl-lazy-img-loaded").attrs['src']
        available_sizes = ''
        for size in sizeParent:
            available_sizes = size.text + ' ' + available_sizes
        print(available_sizes)
        print(name)
        print(price)
        print(image)
        product_details = ProductDetails(
            name=name,
            price=price.replace('\u20b9', ''),
            available_sizes=available_sizes,
            image=image
        )

        jsonstr = json.dumps(product_details.__dict__)

        with open("data.json", "w") as jsonfile:
            jsonfile.write(jsonstr)
            jsonfile.close()
        


if __name__=='__main__':
    with open("url.txt", "r") as f:
        url = f.read()

    scrapeAjio(url=url)