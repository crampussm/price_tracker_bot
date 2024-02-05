from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
from dataclasses import dataclass

@dataclass
class ProductDetails:
    name: str
    price: str
    ratings: str
    available_sizes: str
    image: str

def scrapeMyntra(url):
    with sync_playwright() as p:
        browser = p.webkit.launch()
        page = browser.new_page()
        page.goto(url=url, timeout=300000000)
        soup = BeautifulSoup(page.content(), 'html.parser')
        namestr1 = soup.find(class_="pdp-title")
        namestr2 = soup.find(class_="pdp-name")
        name = f'{namestr1.text} - {namestr2.text}'
        priceParent = soup.find(class_="pdp-price")
        price = priceParent.findChild('strong', recursive=False).text
        rating = soup.find(class_="index-overallRating").text
        sizes = soup.find_all(class_="size-buttons-unified-size")
        available_sizes = ''
        for size in sizes:
            available_sizes = size.text + ' ' + available_sizes
        image = soup.find(class_="image-grid-image").attrs['style']
        imagelink = image.replace('background-image: url("', '').replace('");', '')
        print(type(name))
        print(type(price))
        print(type(rating))
        print(type(available_sizes))
        print(type(imagelink))
        product_details = ProductDetails(
            name=name,
            price=price.replace('\u20b9', ''),
            ratings=rating[0],
            available_sizes=available_sizes,
            image=imagelink
        )

        jsonstr = json.dumps(product_details.__dict__)

        with open("data.json", "w") as jsonfile:
            jsonfile.write(jsonstr)
            jsonfile.close()


if __name__=='__main__':
    with open("url.txt", "r") as f:
        url = f.read()
        f.close()

    # os.remove("url.txt")
    scrapeMyntra(url=url)  