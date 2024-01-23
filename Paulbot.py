import telebot
import time
from threading import Thread

# Replace 'YOUR_BOT_TOKEN' with the actual token you received from BotFather
bot = telebot.TeleBot('6415657881:AAEcmrS29pF6GBF04Cdq9VTZW2Ol9a9o5mQ')
group_chat_id = -1001221225011  # Replace with your group's chat ID

# Forbidden keywords for deletion
forbidden_keywords = ['Episode', 'series', 'share', 'post', 'link', 'movie', 'movies', 'season 2', 'season 3', 'Upload', 'Adulting','session', 'Lockdown', 'Download', 'save', 'gallery', 'phone', 'anyone' 'any' "Any1]

# Keywords for exclusion
exclusion_keywords = ['Outlaws', 'outlaw', 'this', 'when',  'end', 'ending', 'ending']

# Function to handle messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    text = message.text.lower()

    # Check if the message is from the allowed group
    if chat_id != group_chat_id:
        user_firstname = message.from_user.first_name
        reply_message = f"Ok {user_firstname}, I'm not sure exactly what you're trying to start here."

        # Introduce a 3-second delay
        time.sleep(1)

        bot.reply_to(message, reply_message)
        return

    # Check if the message contains forbidden keywords for deletion
    contains_forbidden_keywords = any(keyword.lower() in text for keyword in forbidden_keywords)
    contains_exclusion_keywords = any(keyword.lower() in text for keyword in exclusion_keywords)

    if contains_forbidden_keywords and not contains_exclusion_keywords:
        # Delete the message containing forbidden words
        bot.delete_message(chat_id, message.message_id)

# Polling loop to keep the bot running
bot.polling(none_stop=True)
