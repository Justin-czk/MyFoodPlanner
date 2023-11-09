#############imports##################
import logging
import logging.handlers
import os

import requests

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

################logging##############
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)
##############Key######################
try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise
#######################################
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)
    
if __name__ == "__main__":

    logger.info(update.message.text)

    """Start the bot."""
    updater = Updater(SOME_SECRET, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.shutdown()

    
    
    #logger.info(f"Token value: {SOME_SECRET}")
    #r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    #if r.status_code == 200:
        #data = r.json()
        #temperature = data["forecast"]["temp"]
        #logger.info(f'Weather in Berlin: {temperature}')





        
