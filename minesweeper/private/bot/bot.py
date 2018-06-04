import logging
from telegram.ext import *
from common.models import *
from common.config import *
import time
import sys

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO)
logger = logging.getLogger(__name__)


def error(bot, update, error):
    logger.warning("Update '%s' caused an error '%s'" % (update, error))
    

def help(bot, update):
    update.message.reply_text(text="/play - Play Minesweeper\n/flag - Get the flag")
    
   
def flag(bot, update):
    if update.message.from_user.id != update.message.chat.id:
        update.message.reply_text(text="I don't send flag in group chats! Please go PM")
    try:
        user = User.get(User.id == update.message.from_user.id)
        
        if user.score < 200:
            update.message.reply_text(text="Please get 200 points to get the flag!")
        else:
            update.message.reply_text(text="You're awesome! Here's your flag: `ugra_html_games_are_not_secure`", parse_mode="Markdown")
    except:
        update.message.reply_text(text="Please play my awesome game to get the flag!")

    
def start(bot, update):
    bot.send_game(chat_id=update.message.chat.id, game_short_name="petersweeper")


def play(bot, update):
    bot.send_game(chat_id=update.message.chat.id, game_short_name="petersweeper")


def callback_handler(bot, update):
    user_id = update.callback_query.from_user.id
    chat_id = update.callback_query.message.chat.id
    message_id = update.callback_query.message.message_id
    game_url = "https://petersweeper.ugractf.ru/?userId={}&chatId={}&messageId={}".format(user_id, chat_id, message_id)
    bot.answerCallbackQuery(update.callback_query.id, url=game_url)


if __name__ == "__main__":
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_error_handler(error)
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("play", play))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("flag", flag))
    dp.add_handler(CallbackQueryHandler(callback_handler))
    
    time.sleep(1.5)
    
    db.connect()
    db.create_tables([User])
    
    print("[+] DB connected", file=sys.stderr)

    updater.start_polling()
    updater.idle()

