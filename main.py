from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
bar = []
tempName = ""
tempDescription = ""
tempIngredients = {}
addCounter = 0

class Cocktail:
    def __init__(self, name, description, ingredients):
        self.name = name
        self.description = description
        self.ingredients = ingredients


def add(name, description, ingredients):
    bar.append(Cocktail(name, description, ingredients))

def main():
    updater = Updater('441763865:AAEPyAQEUX2JsLxiHn-xX0QvD4rreksBhHY')

    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("add_cocktail", add_cocktail))

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
    global addCounter
    update.message.reply_text(addCounter)
    if addCounter == 1:
        update.message.reply_text('Введите описание коктейля')
        bot.tempName = update.message.text
    if addCounter == 2:
        update.message.reply_text('Введите ингредиенты в формате имя:количество через запятую')
        bot.tempDescription = update.message.text
    if addCounter == 3:
        tArray = update.message.text.replace(' ', '').split(',')
        for a in tArray:
            bot.tempIngredients[a.split(':')[0]] = a.split(':')[1]
        addCounter = 0
        add(bot.tempName, bot.tempDescription, bot.tempIngredients)
        update.message.reply_text('Ваш коктейль добавлен')
    if addCounter > 0:
        addCounter += 1


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def add_cocktail(bot, update):
    update.message.reply_text('Для внесения коктейля впишите название')
    global addCounter
    addCounter = 1


if __name__ == '__main__':
    main()
