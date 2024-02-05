import json
import subprocess
from dataclasses import dataclass
import os

@dataclass
class Productdetails:
    asin: str
    name: str
    price: str
    imagelink: str
    rating: str

@dataclass
class ProductDetailsMyntra:
    name: str
    price: str
    imagelink: str
    rating: str
    available_sizes: str

@dataclass
class ProductDetailsAjio:
    name: str
    price: str
    imagelink: str
    available_sizes: str 

@dataclass
class ProductDetailsNykaa:
    name: str
    price: str
    imagelink: str
    rating: str

def callscrapAmazon(url):
    with open("url.txt", "w") as f:
        f.write(url)
        f.close()

    subprocess.run(["python", "scrapamazon.py"])

    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()


    product_details = Productdetails(
        asin=data['asin'],
        name=data['name'], 
        price=data['price'],
        imagelink=data['imagelink'],
        rating=data['rating']
    )
    print(product_details.name)
    print(product_details.price)
    print(product_details.imagelink)
    print(product_details.rating)
    return product_details

def callscrapeMyntra(url):
    with open("url.txt", "w") as f:
        f.write(url)
        f.close()

    subprocess.run(["python", "scrapmyntra.py"]) 

    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()

    product_details = ProductDetailsMyntra(
        name=data['name'],
        price=data['price'],
        imagelink=data['image'],
        rating=data['ratings'],
        available_sizes=data['available_sizes']
    )
    print(product_details.name)
    print(product_details.price)
    print(product_details.imagelink)
    print(product_details.rating)
    print(product_details.available_sizes)
    return product_details


def callscrapeAjio(url):
    with open("url.txt", "w") as f:
        f.write(url)
        f.close()

    subprocess.run(["python", "scrapajio.py"])

    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()

    product_details = ProductDetailsAjio(
        name=data['name'],
        price=data['price'],
        imagelink=data['image'],
        available_sizes=data['available_sizes']
    )
    print(product_details.name)    
    print(product_details.price)
    print(product_details.imagelink)
    print(product_details.available_sizes)
    return product_details

def callscrapeNykaa(url):
    with open("url.txt", "w") as f:
        f.write(url)
        f.close()

    subprocess.run(["python", "scrapnykaa.py"])

    with open("data.json", "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()

    product_details = ProductDetailsNykaa(
        name=data['name'],
        price=data['price'],
        imagelink=data['image'],
        rating=data['ratings']
    )
    print(product_details.name)
    print(product_details.price)
    print(product_details.imagelink)
    return product_details