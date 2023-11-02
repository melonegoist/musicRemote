import pyautogui
from telebot import *

token = "6483667774:AAGwwCI197mnVZ3KITVfShf9yejIwN4NNB0"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Pause")
    item2 = types.KeyboardButton("Next")
    item3 = types.KeyboardButton("Previous")
    item4 = types.KeyboardButton("Like")
    item5 = types.KeyboardButton("Song")

    markup.add(item1, item2, item3, item4, item5)
    
    bot.send_message(message.chat.id, "choose a command from list:", reply_markup=markup)

@bot.message_handler()
def message_catcher(message):
    if message.text == "Pause":
        with pyautogui.hold("ctrl"):
            pyautogui.press("p")

    elif message.text == "Next":
        with pyautogui.hold("ctrl"):
            pyautogui.press("f")
    
    elif message.text == "Previous":
        with pyautogui.hold("ctrl"):
            pyautogui.press("b")
        
    elif message.text == "Like":
        with pyautogui.hold("ctrl"):
            pyautogui.press("l")

    elif message.text == "Song":
        screenshot = pyautogui.screenshot("screenshot.png")
        bot.send_photo(message.chat.id, screenshot)


    bot.delete_message(message.chat.id, message.id)
    

bot.polling(none_stop = True)

