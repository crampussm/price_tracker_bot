import requests
from bs4 import BeautifulSoup
# from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio
from selectolax.parser import HTMLParser
from dataclasses import dataclass

@dataclass
class ProductDetails:
    name: str
    price: str
    image_link: str
    rating: str

def scrapFlipkart(url):
    r = requests.get(url=url)
    soup = BeautifulSoup(r.content, 'html.parser')

    nameflipkart = soup.find(class_="B_NuCI")
    priceflipkart = soup.find(class_="_30jeq3 _16Jk6d")
    image = soup.find(attrs = {"class": "_396cs4 _2amPTt _3qGmMb"})
    imageflipkart = image["src"]
    ratingflipkart = soup.find(class_="_3LWZlK")
    if nameflipkart.string == None:
        nameStringflipkart = f"{nameflipkart.contents[0]} {nameflipkart.contents[2]}"
        product_details = ProductDetails(
            name=nameStringflipkart,
            price=priceflipkart.string,
            image_link=imageflipkart,
            rating=ratingflipkart.text.replace(" out of 5 stars", "")
        )
        return product_details
    else:
        product_details = ProductDetails(
            name=nameflipkart.string,
            price=priceflipkart.string,
            image_link=imageflipkart,
            rating=ratingflipkart.text
        )
        return product_details  