import misc
from yobit import get_btc
import telebot

token = misc.token

bot=telebot.AsyncTeleBot(token)

@bot.message_handler(commands=["btc"])
def btc(message):
    bot.send_message(message.chat.id,get_btc())

if __name__ == '__main__':
    bot.polling(none_stop=True)
