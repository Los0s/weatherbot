# -*- coding: utf-8 -*-
import telebot
import pyowm
import random

bot = telebot.TeleBot(My token)
owm = pyowm.OWM(My token, language = 'ru')

randomlistone = ['кажется твоя мама хочет что бы ты одел шапку', 'достаточно холодно что бы никуда не идти', 'лучше одень шапку']
randomlisttwo = ['отличная погода для прогулки', 'уже можно кушать мороженое', 'может съездим на шашлыки']
randomlistthree = ['жарко, очень жарко', 'я умираю, дайте мне воды', 'пошли купатся', 'смотри не умри от жары']
randomlistfor = ['кажется твоя мама хочет что бы ты одел шапку', 'не забудь про подштанники', 'на улице очень холодно, может никуда не пойдем?']



stickerone = 'CAACAgIAAxkBAAIDXF5L7XhCFIvsUevecH4H6RmRuQxrAAIgAAOc_jIwtdxzHomqKuAYBA'
stickertwo = 'CAACAgIAAxkBAAIDal5L8EmNQlU7XbPal_3FDae4Mxb8AAIbAAOc_jIwHIvROO0U1YgYBA'
stickerthree = 'CAACAgIAAxkBAAIDtF5MAcaIIf4adRM_cX5xjfFAHHvAAAIiAAOc_jIwfJJOFZcAASrDGAQ'
stickerfore = 'CAACAgIAAxkBAAIDtV5MAq5lC0AEDV65bgGskXXHXXw6AAIVAAOc_jIw-s-ED4CBZWEYBA'
stickerfive = 'CAACAgIAAxkBAAIETl5MPKDK9-m3yTxTsRI_WIBE4tZXAAIPAAOc_jIwECcymytqvFgYBA'
stickersix = 'CAACAgIAAxkBAAIEV15MPlyesm3kg7eSSoxuU9QC8UNGAAIZAAOc_jIwa2cGK5LLFaMYBA'
stickersev = 'CAACAgIAAxkBAAIEWl5MPwQubEWzMezl6jh9XM5ts0RxAAIMAAOc_jIwC9JihhxLcLoYBA'
stickereight = 'CAACAgIAAxkBAAIEg15MQxoWpy1mjSMfgmkaTf4Gr-UaAAIYAAOc_jIwk9E8MgHE84YYBA'
stickernine = 'CAACAgIAAxkBAAIEiF5MRJOYQDsnXaSRbx1O83yetwnNAAIjAAOc_jIwYtIVuCqdptEYBA'
stickerten = 'CAACAgIAAxkBAAIEiV5MRRUSaIR25zDAHU7sh2hLAuAlAAISAAOc_jIw4DVLQ657a9QYBA'
stickereleven = 'CAACAgIAAxkBAAIEil5MRaRE5GcLywjNh5iIMiYgDUwmAAITAAOc_jIwuOyJRYHXHzoYBA'
stickertwelv = 'CAACAgIAAxkBAAIFGV5M32Z2o8Hi__fbbIvqcJGeQ3gHAAIeAAOc_jIw2mt0gmh8fmwYBA'
stickerthreee = 'CAACAgIAAxkBAAIFGl5M4BGX4Kafy-XUBP--KoLkdLYfAAIMAAOc_jIwC9JihhxLcLoYBA'





@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_sticker(message.chat.id, stickerone)
	bot.send_message(message.chat.id, 'Привет ' + message.from_user.first_name + ', напишы мне город что бы узнать из него погоду')
	
	
	




@bot.message_handler(content_types=['text'])
def weath(message):
	try:
		locate = (message.text)
		weather = owm.weather_at_place(locate)
		w = weather.get_weather()
		temp = w.get_temperature(unit='celsius')['temp']
		status = w.get_detailed_status()
		temperature = round(temp)
		bot.reply_to(message, 'на улице ' + str(temperature))
		bot.reply_to(message, 'в небе ' + status)
		if int(temperature) >= 0 and temperature <= 10:
			randomsone = random.choice(randomlistone)
			bot.reply_to(message, randomsone)
			if randomsone == 'кажется твоя мама хочет что бы ты одел шапку':
				bot.send_sticker(message.chat.id, stickertwo)
			if randomsone == 'достаточно холодно что бы никуда не идти':
				bot.send_sticker(message.chat.id, stickerthree)
			if randomsone == 'лучше одень шапку':
				bot.send_sticker(message.chat.id, stickerfore)
		if temperature >= 11 and temperature <= 20:
			randomstwo = random.choice(randomlisttwo)
			bot.reply_to(message, randomstwo)
			if randomstwo == 'отличная погода для прогулки':
				bot.send_sticker(message.chat.id, stickerfive)
			if randomstwo == 'уже можно кушать мороженое':
				bot.send_sticker(message.chat.id, stickersix)
			if randomstwo == 'может съездим на шашлыки':
				bot.send_sticker(message.chat.id, stickersev)
		if temperature >= 21 and temperature <=100:
			randomsthree = random.choice(randomlistthree)
			bot.reply_to(message, randomsthree)
			if randomsthree == 'жарко, очень жарко':
				bot.send_sticker(message.chat.id, stickereight)
			if randomsthree == 'я умираю, дайте мне воды':
				bot.send_sticker(message.chat.id, stickernine) 
			if randomsthree == 'пошли купатся':
				bot.send_sticker(message.chat.id, stickerten)
			if randomsthree == 'смотри не умри от жары':
				bot.send_sticker(message.chat.id, stickereleven)
		if temperature < 0:
			randomsfore = random.choice(randomlistfor)
			bot.reply_to(message, randomsfore)
			if randomsfore == 'кажется твоя мама хочет что бы ты одел шапку':
				bot.send_sticker(message.chat.id, stickertwo)
			if randomsfore == 'не забудь про подштанники':
				bot.send_sticker(message.chat.id, stickertwelv)
			if randomsfore == 'на улице очень холодно, может никуда не пойдем?':
				bot.send_sticker(message.chat.id, stickerthreee)
			 
	except:
		bot.reply_to(message, 'такого города не существует')





	
	
bot.polling(none_stop=True)
