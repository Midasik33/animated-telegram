import telebot
import requests
import json
bot = telebot.TeleBot("8350123529:AAEJVZLp1OCG3Wi4-hCiklorYwe_KHg8Mzo")
API = 'ce86a2abe0ff7dd7163e17a3fd07a97d'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! рад тебя видеть! Напиши свой город')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message,f'Сейчас погода: {temp}°')
        image = 'sunny.png' if temp < 5.0 else 'sun.png'
        file = open('./'+image,'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message,'Город указан неверно')

bot.infinity_polling(timeout=10, long_polling_timeout = 5)