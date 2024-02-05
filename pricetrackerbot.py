from aiogram import Bot, Dispatcher, executor, types
import webscrapper as ws
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import sendtodb as sdb
import call_scraper as callscrap
import call_compare as cc
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('BOT_TOKEN')
bot = Bot(token=key)
dp = Dispatcher(bot=bot)


button1 = InlineKeyboardButton(text="📊 Price Stats", callback_data="price_stats")
button2 = InlineKeyboardButton(text="📉 Track Price", callback_data="track_price")
button3 = InlineKeyboardButton(text="🔔 Notify Price Drop", callback_data="notify_price_drop")
button4 = InlineKeyboardButton(text="🔎 Compare Other Websites", callback_data="compare_other_websites")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2).add(button3, button4)


@dp.message_handler(commands=['start', 'websites'])
async def initiate(message: types.Message):
    await message.reply("""Hello!
I'm Price Tracker Ultimate
Send me the link of your product and will tell you the price
                        
⭕ WEBSITES I SUPPORT ⭕
1⃣ Flipkart
2⃣ Amazon
3⃣ Myntra
4⃣ Ajio
""")
    
@dp.message_handler()
async def scrap(message: types.Message):
    if "flipkart.com" in message.text:
        msg = message.text
        global url
        global asin
        global site
        global name
        global price
        global chatId
        chatId = message.chat.id
        site = "flipkart"
        asin = ""
        url = msg.split()
        pdDetails = ws.scrapFlipkart(url[-1])
        print("Scraped Successfully")
        name = pdDetails.name
        price = pdDetails.price
        if float(pdDetails.rating)>4.5:
            openion = "Must buy"
        elif float(pdDetails.rating)>4.0:
            openion = "Good option to buy"
        elif float(pdDetails.rating)<3.5:
            openion = "Don't buy"    
        else:
            openion = "You may consider it to buy"    
        await message.answer_photo(pdDetails.image_link)
        await message.reply(f"""
                            Product - {name}
Price - {price}
Rating - {pdDetails.rating} stars
Bot's Openion - {openion}
""", reply_markup=keyboard_inline)
        
    elif "range" in message.text and len(message.text.split())==4:
        range = message.text
        range = range.split()
        startingRange = range[1]
        closingRange = range[-1]
        await message.reply(f"Price range set to {startingRange} - {closingRange}")
        sdb.insertDatafrtrack(userId=chatId, link=url[-1], site=site, name=name, price=price.replace('₹',''), range_start=startingRange, range_end=closingRange, asin=asin)   

    elif "amazon.in" in message.text or "amzn.eu" in message.text:
        msg = message.text
        chatId = message.chat.id
        site = "amazon"
        url = msg.split()
        pdDetails = callscrap.callscrapAmazon(url=url[-1])
        print("Scraped Successfully")
        asin = pdDetails.asin
        name = pdDetails.name
        price = pdDetails.price
        if float(pdDetails.rating)>4.5:
            openion = "Must buy"
        elif float(pdDetails.rating)>4.0:
            openion = "Good option to buy"
        elif float(pdDetails.rating)<3.5:
            openion = "Don't buy"    
        else:
            openion = "You may consider it to buy"    
        await message.answer_photo(pdDetails.imagelink)
        await message.reply(f"""
                            Product - {name}
Price - {price}
Rating - {pdDetails.rating} stars
Bot's Openion - {openion}
""", reply_markup=keyboard_inline)
        
    elif "myntra.com" in message.text:
        msg = message.text
        chatId = message.chat.id
        site = "myntra"
        url = msg.split()
        asin = url[-1].split('/')[-2]
        pdDetails = callscrap.callscrapeMyntra(url=url[-1])
        print("Scraped Successfully")
        name = pdDetails.name
        price = pdDetails.price
        if float(pdDetails.rating)>4.5:
            openion = "Must buy"
        elif float(pdDetails.rating)>4.0:
            openion = "Good option to buy"
        elif float(pdDetails.rating)<3.5:
            openion = "Don't buy"    
        else:
            openion = "You may consider it to buy"
        await message.answer_photo(pdDetails.imagelink)   
        await message.reply(f"""
                            Product - {name}
Price - {price}
Rating - {pdDetails.rating} stars
Available Sizes - {pdDetails.available_sizes}
Bot's Openion - {openion}
""", reply_markup=keyboard_inline)
        
    elif "ajio.com" in message.text:        
        msg = message.text
        chatId = message.chat.id
        site = "ajio"
        url = msg.split()
        asin = url[-1].split('/')[-1].split('_')[0]
        print(asin)
        pdDetails = callscrap.callscrapeAjio(url=url[-1])
        print("Scraped Successfully")
        name = pdDetails.name
        price = pdDetails.price
        await message.answer_photo(pdDetails.imagelink)   
        await message.reply(f"""
                            Product - {name}
Price - {price}
Available Sizes - {pdDetails.available_sizes}
""", reply_markup=keyboard_inline)
        
    elif "nykaa.com" in message.text:
        msg = message.text
        chatId = message.chat.id
        site = "nykaa"
        url = msg.split()
        asin = url[-1].split('/')[-1].split('?')[0]
        print(asin)
        pdDetails = callscrap.callscrapeNykaa(url=url[-1])
        print("Scrapped Successfully")
        name = pdDetails.name
        price = pdDetails.price
        rating = pdDetails.rating
        if float(pdDetails.rating)>4.5:
            openion = "Must buy"
        elif float(pdDetails.rating)>4.0:
            openion = "Good option to buy"
        elif float(pdDetails.rating)<3.5:
            openion = "Don't buy"    
        else:
            openion = "You may consider it to buy"
        await message.answer_photo(pdDetails.imagelink)
        await message.reply(f"""
                            Product - {name}
Price - {price}
rating - {rating}
Bot's Openion - {openion}
""", reply_markup=keyboard_inline)
    else:
        await message.reply(f"""
We currently do not support this website.
Please use '/start' or /'websites' to know the websites that we support.                         
""")


@dp.callback_query_handler(text = ['price_stats', 'track_price', 'notify_price_drop', 'compare_other_websites'])    
async def responseQuery(call: types.CallbackQuery):
    if call.data == 'notify_price_drop':
        sdb.insertData(userId=chatId, link=url[-1], site=site, name=name, price=price.replace('₹',''), asin=asin)
        await call.message.answer("I will notify you when the price is dropped")
    elif call.data == 'track_price':
        await call.message.answer("""Set a range - 
use this format:
range: staring - ending
                """)
    elif call.data == 'compare_other_websites':
        wareL = ['shirt', 't-shirt', 'jeans', 'pant', 'shorts', 'jogger', 'skirt', 'raincoat', 'cycle']
        siteFL = ['myntra', 'ajio', 'nykaa']
        if site in siteFL:
            await call.message.answer("Sorry! Can not compare fashion and cosmetic items.")
        elif any(ele in name.lower() for ele in wareL):
            await call.message.answer("Sorry! Can not compare fashion and cosmetic items.")
        else:
            await call.message.answer("Comparing Other Websites....")
            all_data = cc.call_compare(name=name)
            if all_data[0].title==None or all_data[1].title==None:
                await call.message.answer(f"""Sorry, this same item was not found in any other website!! """)
            else:
                await call.message.answer(f"""
        Product - {name}
        Comparing Data of all websites where the product is available...
        FlipKart -
        price- {all_data[0].price}
        Amazon -
        price- {all_data[0].price}
        """)
    elif call.data == 'price_stats':
        await call.message.answer(f"""
This Feature will be available soon...
""")      
            
executor.start_polling(dp)