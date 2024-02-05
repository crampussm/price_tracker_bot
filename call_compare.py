import subprocess
import json
import os
from dataclasses import dataclass

@dataclass
class Details:
    title: str
    price: str

def call_compare(name):
    with open('name.txt', 'w') as f:
        f.write(name)

    subprocess.run(["python", "comparewebsites.py"])

    try:
        with open('datacompareflpk.json', 'r') as jsonfile:
            data = json.load(jsonfile)
        detailsflpk = Details(
            title=data['title'],
            price=data['price']
        )
        print(detailsflpk.title)   
        print(detailsflpk.price)

        with open('datacompareamaz.json', 'r') as jsonfile:
            data = json.load(jsonfile)

        detailsamaz = Details(
            title=data['title'],
            price=data['price']
        )
        print(detailsamaz.title)   
        print(detailsamaz.price) 
    except:
        detailsflpk = Details(
            title=None,
            price=None
        )
        detailsamaz = Details(
            title=None,
            price=None
        )

    return [detailsflpk, detailsamaz]

