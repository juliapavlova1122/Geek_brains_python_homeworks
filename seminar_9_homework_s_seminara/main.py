from telegram import Update
from telegram.ext import Updater, Filters, CommandHandler, MessageHandler, CallbackContext
from bot_commands import *


updater = Updater('5722868369:AAF3G0uYZpCZj2K7CgRuiqsn6IfP7KmANAg')

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('exit', quit_command))

updater.dispatcher.add_handler(MessageHandler(Filters.text, analize_command))

updater.start_polling()
updater.idle()
