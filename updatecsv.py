import csv
import datetime
import os
import webscrapper as ws
import urllib, requests
import call_scraper as callscrap
import subprocess


def notifyDrop(price_prev, price_now, userid, pdname, pdlink):
    msg = f"""
🔴 PRICE DROP ALERT 🔴

{pdname}
{pdlink}
Price Before - {price_prev} (Price Dropped📉) 
Price Now - {price_now}
The Price is dropped. Buy it now.
"""
    if int(price_prev) > int(price_now):
        url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        '6353495818:AAHV5tF2EYqjBj4xqMGeRRBdQhUO3raWyVs', f'{userid}', urllib.parse.quote_plus(f'{msg}'))
        _ = requests.get(url, timeout=10)


def trackRngrchdnotify(price_prev, price_now, userid, pdname, pdlink, range_start, range_end):
    range = [range_start, range_end]
    range.sort()
    msg = f"""
🔴 PRICE RANGED REACHED ALERT 🔴

{pdname}
{pdlink}
Price Before - {price_prev} (Price Dropped📉) 
Price Now - {price_now}
The price of this product is reached in your prefferable price range: {range[0]} - {range[1]}
Buy now.
"""
    if int(price_now) >= int(range[0]) and int(price_now) <= int(range[1]):
        url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % (
        '6353495818:AAHV5tF2EYqjBj4xqMGeRRBdQhUO3raWyVs', f'{userid}', urllib.parse.quote_plus(f'{msg}'))
        _ = requests.get(url, timeout=10)


def updateCsv(files):
    for file in files:
        myList = []
        with open(file, "r") as datafile:
            data = csv.reader(datafile, delimiter=',')
            next(data)
            for row in data:
                myList.append(row)
            datafile.close() 

        url = myList[-2][1]
        if myList[-2][2]=="flipkart":
            pdDetails = ws.scrapFlipkart(url=url)
            if "trackrange" in str(file):
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace('₹','').replace(',','')}", f"{str(datetime.datetime.now())}", "", ""])
                    datafile.close()

                trackRngrchdnotify(price_prev=myList[-2][4], price_now=pdDetails.price.replace('₹','').replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url, range_start=myList[1][6], range_end=myList[1][7])
            else:
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace('₹','').replace(',','')}", f"{str(datetime.datetime.now())}"])
                    datafile.close()

                notifyDrop(price_prev=myList[-2][4], price_now=pdDetails.price.replace('₹','').replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url) 
        elif myList[-2][2]=="amazon":
            pdDetails = callscrap.scrapAmazon(url=url)
            if "trackrange" in str(file):
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace(',','')}", f"{str(datetime.datetime.now())}", "", ""])
                    datafile.close()

                trackRngrchdnotify(price_prev=myList[-2][4], price_now=pdDetails.price.replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url, range_start=myList[1][6], range_end=myList[1][7])
            else:
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace('₹','').replace(',','')}", f"{str(datetime.datetime.now())}"])
                    datafile.close()

                notifyDrop(price_prev=myList[-2][4], price_now=pdDetails.price.replace('₹','').replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url)    
        elif myList[-2][2]=="myntra":
            pdDetails = callscrap.callscrapeMyntra(url=url)
            if "trackrange" in str(file):
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace(',','')}", f"{str(datetime.datetime.now())}", "", ""])
                    datafile.close()

                trackRngrchdnotify(price_prev=myList[-2][4], price_now=pdDetails.price.replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url, range_start=myList[1][6], range_end=myList[1][7])
            else:
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace('₹','').replace(',','')}", f"{str(datetime.datetime.now())}"])
                    datafile.close()

                notifyDrop(price_prev=myList[-2][4], price_now=pdDetails.price.replace('₹','').replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url)   
        elif myList[-2][2]=="ajio":
            pdDetails = callscrap.callscrapeAjio(url=url)
            if "trackrange" in str(file):
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace(',','')}", f"{str(datetime.datetime.now())}", "", ""])
                    datafile.close()

                trackRngrchdnotify(price_prev=myList[-2][4], price_now=pdDetails.price.replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url, range_start=myList[1][6], range_end=myList[1][7])    
            else:
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace('₹','').replace(',','')}", f"{str(datetime.datetime.now())}"])
                    datafile.close()

                notifyDrop(price_prev=myList[-2][4], price_now=pdDetails.price.replace('₹','').replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url)
        elif myList[-2][2]=="nykaa":
            pdDetails = callscrap.callscrapeNykaa(url=url)
            if "trackrange" in str(file):
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace(',','')}", f"{str(datetime.datetime.now())}", "", ""])
                    datafile.close()

                trackRngrchdnotify(price_prev=myList[-2][4], price_now=pdDetails.price.replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url, range_start=myList[1][6], range_end=myList[1][7])    
            else:
                with open(file, "a") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["", f"{url}", f"{myList[-2][2]}", f"{myList[-2][3]}", f"{pdDetails.price.replace('₹','').replace(',','')}", f"{str(datetime.datetime.now())}"])
                    datafile.close()

                notifyDrop(price_prev=myList[-2][4], price_now=pdDetails.price.replace('₹','').replace(',',''), userid=myList[1][0], pdname=myList[-2][3], pdlink=url)                     

path = "./csvfiles"

folders = os.listdir(path)
files = []

for folder in folders:
    path2 = f"./csvfiles/{folder}"
    for f in os.listdir(path2):
        files.append(f"{path2}/{f}")


subprocess.run(['python', 'pricetrackerbot.py'])

while True:
    time = datetime.datetime.now()

    time_now = f"{time.hour}:{time.minute}:{time.second}"

    if time_now == "0:0:0":
        updateCsv(files=files)
    elif time_now == "6:0:0":
        updateCsv(files=files)
    elif time_now == "12:0:0":
        updateCsv(files=files) 
    elif time_now == "18:0:0":
        updateCsv(files=files)
    elif time_now == "23:43:0":
        updateCsv(files=files)   
    else:
        pass