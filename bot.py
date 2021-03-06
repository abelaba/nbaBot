#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
#imports
import logging
from BasketBallBot import BasketBallBot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    bot = BasketBallBot()

    updater = Updater(bot.TOKEN , use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("today", bot.getTodaysGames))
    dp.add_handler(CommandHandler("yesterday", bot.getYesterdaysGames))
    #

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.document, bot.readQRCode))

    # log all errors
    dp.add_error_handler(bot.error)

    PORT = int(os.environ.get('PORT', '8443'))
    # Start the Bot
    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=bot.TOKEN,
        webhook_url='https://ancient-shelf-71885.herokuapp.com/' + bot.TOKEN
    )

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()