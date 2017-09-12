#CoreTM
#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import re
import time
from time import sleep
import sys
import json
import os
import logging
import subprocess
import requests
import random
from random import randint
import base64
import urllib
from urllib import urlretrieve as dw
import urllib2
import redis
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = '410856564:AAGel_521456VYVXKlABtozSEyp-rQqRXPY'
bot = telebot.TeleBot(TOKEN)
sudo = '438573461'
redis = redis.StrictRedis(host='localhost', port=6379, db=0)


f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
bot.send_message(330330173, '*Bot Launched!*', parse_mode="Markdown")

print(f + u + i + c)

#################################################################################################################################################################################################
@bot.message_handler(commands=['start'])
def welcome(m):
       cid = m.chat.id
       markup = types.InlineKeyboardMarkup()
       oo = types.InlineKeyboardButton("CoreTM", url='https://telegram.me/CoreTM')
       markup.add(oo)
       id = m.from_user.id
       redis.sadd('memberspy',id)
       bot.send_message(cid, "*سلام*\nبه ربات دانلودر ما خوش اومدید", disable_notification=True, reply_markup=markup, parse_mode='Markdown')
#################################################################################################################################################################################################

@bot.message_handler(regexp='^# (.*)')
def all(m):
    text = m.text.split()[1]
    id = m.from_user.id
    banlist = redis.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
      try:
         if m.chat.type == 'private':
             if re.match('(http|https)://.*.(png)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'file.png')
                 bot.send_photo(m.chat.id, open('file.png'),caption='@CoreDownloaderBot')
                 os.remove('file.png')
             if re.match('(http|https)://.*.(apk)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'app.apk')
                 bot.send_document(m.chat.id, open('app.apk'),caption='@CoreDownloaderBot')
                 os.remove('app.apk')
             if re.match('(http|https)://.*.(html|htm)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'file.html')
                 bot.send_document(m.chat.id, open('file.html'),caption='@CoreDownloaderBot')
                 os.remove('file.html')
             if re.match('(http|https)://.*.(jpg)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'s.jpg')
                 bot.send_photo(m.chat.id, open('s.jpg') ,caption='@CoreDownloaderBot')
                 os.remove('s.jpg')
             if re.match('(http|https)://.*.(gif)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'s.gif')
                 bot.send_photo(m.chat.id, open('s.gif'),caption='@CoreDownloaderBot')
                 os.remove('s.gif')
             if re.match('(http|https)://.*.(zip|rar)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'file.zip')
                 bot.send_document(m.chat.id, open('file.zip'),caption='@CoreDownloaderBot')
                 os.remove('file.zip')
             if re.match('(http|https)://.*.(webp)$',text):
                 msg = bot.send_message(m.chat.id, 'در حال دانلود........!',parse_mode='Markdown')
                 dw(text,'file.webp')
                 bot.send_sticker(m.chat.id, open('file.webp'))
                 os.remove('file.webp')
      except IndexError:
                 bot.send_message(m.chat.id, '*ارور!\nلینک نامعتبر است!*',parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(commands=['bc'])
def clac(m):
    if m.from_user.id == 330330173:
        text = m.text.replace("/bc ","")
        rd = redis.smembers('memberspy')
        for id in rd:
                bot.send_message(id, "{}".format(text), parse_mode="Markdown")

#################################################################################################################################################################################################
bot.polling(True)
#end
