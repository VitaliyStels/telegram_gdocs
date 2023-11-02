from dotenv import load_dotenv
import os
import telebot

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_API_TOKEN'))
CHANNEL_ID = os.getenv('CHANNEL_ID')

def writeUsersData(user):
    with open('data/users.txt', 'a') as f:
        f.write(f"{user.username} {user.id}")

@bot.message_handler(commands=['init'])
def handle_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    giveAwayButton = telebot.types.InlineKeyboardButton(text='Участвовать', callback_data='participate')
    keyboard.add(giveAwayButton)
    bot.send_message(CHANNEL_ID, 'Хотите участвовать?', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)
def handle_callback_query(callback_query):
    if callback_query.data == 'participate':
        writeUsersData(callback_query.from_user)
        bot.send_message(callback_query.from_user.id, 'Вы успешно добавили свое имя в список участников!')

if __name__ == '__main__':
    bot.polling()