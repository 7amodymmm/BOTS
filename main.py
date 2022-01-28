import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
dev = types.InlineKeyboardButton(text="- Owner 👁️",url="https://t.me/uufffuu")
@bot.message_handler(commands=["start"])
def f(message):
	user = message.from_user.username
	v = f"https://t.me/pydroi_d_3/36"
	name = message.chat.first_name
	key=types.InlineKeyboardMarkup()
	key.raw_width=4
	key.add(dev)
	bot.send_photo(message.chat.id,v,f"""
- - - - - - - - - - - - - -
- Hi {name} @{user}
- Welcome Bot 
- Download Form TikTok
- Send Url ?
- - - - - - - - - - - - - - """,reply_markup=key)
@bot.message_handler(func=lambda m:True)
def f(message):
	url = message.text
	if "https://vm.tiktok.com" not in url:
		bot.reply_to(message,"Send Url Video TikTok 😠")
	if "https://vm.tiktok.com" in url:
		key=types.InlineKeyboardMarkup()
		key.raw_width=4
		key.add(dev)
		ur = requests.get(f"https://iqhost.xyz/tiktok/dvid/{url}").json()["video"][0]
		bot.send_video(message.chat.id,ur,"- Done Download Video ✅",reply_to_message_id=(message.message_id),reply_markup=key)  
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://modybots.herokuapp.com"+str(BOT_TOKE