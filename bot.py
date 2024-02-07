# Bot By @gringomdz & API by @Webzin116
import telebot
import requests
import json

# Coloque seu token aqui
TOKEN = '6813923620:AAFVzq-XTFafTNkGORm7UnTtVCzIUbRJ4Aw'


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['ia'])
def handle_ia(message):
    chat_id = message.chat.id
    query = message.text[4:]  # Remove '/ia ' do início da mensagem para não bugar a resposta

    # Api usada 
    worker_api_url = "https://chatgpt.apinepdev.workers.dev/?question=" + query

    response = requests.get(worker_api_url)
    response_data = response.json()

    answer = response_data.get('answer', 'Desculpe o bot esta offline')

    bot.send_chat_action(chat_id, 'typing')
    bot.send_message(chat_id, f"\n{answer}")

bot.polling()
