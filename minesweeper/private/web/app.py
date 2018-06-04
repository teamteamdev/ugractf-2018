from flask import Flask, request, render_template
from telegram import *
from common.models import *
from common.config import TOKEN

app = Flask(__name__)
bot = Bot(TOKEN)


@app.route('/post/', methods=['POST'])
def send_results():
    try:
        chat_id = request.form["chatId"]
        message_id = request.form["messageId"]
        user_id = request.form["userId"]
        score = request.form["score"]
        bot.setGameScore(user_id=user_id, score=score, chat_id=chat_id, message_id=message_id)
        
        try:
            user = User.get(User.id == user_id)
            user.highscore = max(user.highscore, score)
            user.save()
        except:
            User.create(id=id, highscore=score)        
        
        if score >= 200:
            try:
                bot.sendMessage(chat_id=user_id, text="**Congratulations!** Now you can get your /flag!", parse_mode="Markdown")
            except:
                pass
        
        return "OK"
    except:
        return "Error"


@app.route('/', methods=['GET'])
def minesweeper():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
