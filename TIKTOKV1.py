import os
try:
	import telebot
	import requests 
	import sys
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install telebot')
    os.system('pip install pyTelegramBotAPI==3.7.7')
    os.system('pip install sys') 
sudo_user = "@h_69053"
sudo_channel = "@HHSPX"
from telebot import types
telebot.logger.setLevel(__import__('logging').DEBUG)
#----- Import Offices ----- #


#-----Operating Requirements-----#
bot = telebot.TeleBot(BOT_TOKEN)
api_key = '9044762e-8bbe-4466-b7aa-b90a78e7d455' #Dont Change
fc = f"أهلا عزيزي يجب عليك الاشتراك في قناة البوت \n قناة البوت : @{sudo_channel}"
#-----Operating Requirements-----#


#-----The Beginning-----#
def get_price():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price
price = get_price()
#-----The Beginning-----#


#-----Function-----#
def ex_id(id):
    result = False
    file = open("uuusers.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

url = f"https://api.telegram.org/bot{token}/getChat?chat_id=@{sudo_channel}"
response = requests.get(url).json()
#-----Function-----#


#-----Inline Class-----#


#-----Ar-----#
@bot.message_handler(commands=['start'])
def any_msg(message:str):
    frt = message.chat.first_name
    idd = message.from_user.id
    h = "https://pin.it/3FZOfQu"
    if message.chat.type == 'private':
        idu = message.from_user.id
        us = str(message.chat.first_name)
        f = open("uuusers.txt", 'a')
        if(not ex_id(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
    bot.send_photo(message.chat.id,h,f"""
    • اهلا بك {frt}
• بوت تحميل من التيك توك . 
• لتحميل فديو وصور ارسل رابط المنشور .
• التحميل بدون علامة مائية او اي حقوق اخرى.
• المطور - @HHSPX
    """)            	    
@bot.message_handler(commands=['admin'])
def any_msg(message:str):
    if message.from_user.username in sudo_user:
        file = open('uuusers.txt', 'r')
        li = len(file.readlines())
        file.close()
        admin_keyboard = types.InlineKeyboardMarkup()
        brod = types.InlineKeyboardButton(text='أذاعه .', callback_data='brod')
        bk = types.InlineKeyboardButton(text='نسخه احتياطيه .', callback_data='bk')
        sub = types.InlineKeyboardButton(text=f'عدد المشتركين : {li} .', callback_data='sub')
        admin_keyboard.row_width = 2
        admin_keyboard.add(brod, bk, sub)
        markup_help = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, 'أهلا عزيزي الادمن . \n يمكنك التحكم عن طريق كيبورد اسفل و شكرا .', reply_markup=admin_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:            
        if call.data == 'brod':
            mesgg = bot.send_message(call.message.chat.id, text='*ارسل لي نص الاذاعه :*', parse_mode='markdown')
            bot.register_next_step_handler(mesgg, broddd)
        if call.data == 'bk':
            bk(call.message)        
def bk(message):
    bk = open('uuusers.txt', 'rb')
    bot.send_document(message.chat.id, bk)
    
def broddd(message):
    mes = message.text
    f = open("uuuusers.txt","r")
    for idu in f:
        bot.send_message(idu, text="{}".format(mes))
@bot.message_handler(func=lambda m:True)   
def get(message):
    frt = message.chat.first_name
    usr = message.from_user.username
    try:
    	msg = message.text
    	url = requests.get(f"https://api.reiyuura.me/api/dl/tiktok?url={msg}").json()
    	tik = url["result"]["nowm"]
    	bot.send_video(message.chat.id,tik, caption="- @JJALBOT .")
    except:
        pass	  
        
        	      
server.route(f"/{BOT_TOKEN}",methods=["POST"])
def redirect_message():
	json_string = requests.get_data().decode("utf-8")
	update = telebot.types.Update.de_json(json_string)
	bot_process_new_updates([update])
	return "!", 200

if __name__ = "__main__":
	bot.remove_webhook()
	bot.set_webhook(url="https://spyrx.herokuapp.com/"+ str(BOT_TOKEN))
	server.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))