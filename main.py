from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def main():
    updater = Updater('441763865:AAEPyAQEUX2JsLxiHn-xX0QvD4rreksBhHY')

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    texttoconvert = update.message.text.upper()
    dict_symbols = {'Q': 'Й', 'W': 'Ц'}
    result=''
    for i in texttoconvert:
        if i in dict_symbols.keys():
            result+=dict_symbols.get(i)
        else:
            result+=i


    update.message.reply_text(result)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def add_cocktail(bot, update):
    # Сюда написать в каком формате добавлять
    update.message.reply_text('Добавьте коктейль в формате: ***')
if __name__ == '__main__':
    main()
