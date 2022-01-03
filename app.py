import telebot
from telebot import types
import os
import pyautogui as pg

token = "5038153352:AAEFXN0gkE3PlhDbDQB354dola6-z7HBC4o"

bot=telebot.TeleBot(token)

playText = 'Play/Pause \u25b6\ufe0f'
blockText = 'Block Computer \ud83d\udd12'
volumeUpText = 'Up \ud83d\udd0a'
volumeDownText = 'Down \ud83d\udd09'
volumeNoneText = 'Mute \ud83d\udd07'

markup = types.ReplyKeyboardMarkup(row_width=1)
play = types.KeyboardButton(playText)
block = types.KeyboardButton(blockText)
volumeUp = types.KeyboardButton(volumeUpText)
volumeDown = types.KeyboardButton(volumeDownText)
volumeMute = types.KeyboardButton(volumeNoneText)
markup.row(play)
markup.row(block)
markup.row(volumeDown, volumeUp, volumeMute)


def echo_messages(messages):
    for message in messages:
        chatId = message.chat.id
        if message.content_type == "text":
            text = message.text
            if text == playText:
                pg.press("playpause")
                bot.send_message(chatId, "\u2705")
                bot.send_message(chatId, "\u2754", reply_markup=markup)
            elif text.split(" ")[0] == "Block":
                os.system("rundll32.exe user32.dll,LockWorkStation")
                bot.send_message(chatId, "\u2705")
                bot.send_message(chatId, "\u2754", reply_markup=markup)
            elif text.split(" ")[0] == "Block":
                os.system("rundll32.exe user32.dll,LockWorkStation")
                bot.send_message(chatId, "\u2705")
                bot.send_message(chatId, "\u2754", reply_markup=markup)
            elif text.split(" ")[0] == "Up":
                pg.press('volumeup', presses = 5)
                bot.send_message(chatId, "\u2705")
                bot.send_message(chatId, "\u2754", reply_markup=markup)
            elif text.split(" ")[0] == "Down":
                pg.press('volumedown', presses = 5)
                bot.send_message(chatId, "\u2705")
                bot.send_message(chatId, "\u2754", reply_markup=markup)
            elif text.split(" ")[0] == "Mute":
                pg.press('volumemute')
                bot.send_message(chatId, "\u2705")
                bot.send_message(chatId, "\u2754", reply_markup=markup)
            else:
                bot.send_message(chatId, "\u2754", reply_markup=markup)


bot.set_update_listener(echo_messages)
bot.polling(none_stop=True)
