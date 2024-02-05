import datetime
import csv
import os

def insertData(userId, link, site, name, price, asin):
    if os.path.exists(f'./csvfiles/{str(userId)}'):
        pass
    else:
        os.mkdir(f'./csvfiles/{str(userId)}', mode=0o666)

    if site=="flipkart":
        unqcode = link.split('/')[-1]
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}"})
    elif site=="amazon":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}"})
    elif site=="myntra":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}"})
    elif site=="ajio":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}"})
    elif site=="nykaa":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}"})

def insertDatafrtrack(userId, link, site, name, price, range_start, range_end, asin):
    if os.path.exists(f'./csvfiles/{str(userId)}'):
        pass
    else:
        os.mkdir(f'./csvfiles/{str(userId)}', mode=0o666)

    if site=="flipkart":
        unqcode = link.split('/')[-1]
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}trackrange.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date', 'Start Range', 'End Range']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}", "Start Range": f'{range_start}', "End Range": f'{range_end}'})
    elif site=="amazon":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}trackrange.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date', 'Start Range', 'End Range']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}", "Start Range": f'{range_start}', "End Range": f'{range_end}'})
    elif site=="myntra":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}trackrange.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}", "Start Range": f'{range_start}', "End Range": f'{range_end}'})
    elif site=="ajio":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}trackrange.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}", "Start Range": f'{range_start}', "End Range": f'{range_end}'})        
    elif site=="nykaa":
        unqcode = asin
        with open(f'csvfiles/{str(userId)}/{str(userId)}{unqcode}trackrange.csv', "w") as csvfile:
            fieldNames = ['User Id', 'Link', 'Site', 'Name', 'Price', 'Date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
            writer.writeheader()
            writer.writerow({"User Id": f"{userId}", "Link": f"{link}", "Site": f"{site}", "Name": f"{name}", "Price": f"{price.replace(',', '')}", "Date": f"{str(datetime.datetime.now())}", "Start Range": f'{range_start}', "End Range": f'{range_end}'})