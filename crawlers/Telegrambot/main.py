import telegram
import configparser
import redis

from telegram.ext import Updater, CommandHandler

tokenbot = '585670432:AAGc2Zvl6vz3NVr6SSnpqFYvUBmpCSZtx0Y'
updater = Updater(token=tokenbot)
dispatcher = updater.dispatcher

NadaPraFazer =''
NadaPraFazer = CommandHandler('NadaPraFazer', NadaPraFazer)
dispatcher.add_handler(NadaPraFazer)

def NadaPraFazer_handler(bot, update):
    """
        Shows an welcome message and help info about the available commands.
    """
    me = bot.get_me()

    msg = '[gatos,fofinhos,sorte]'

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)