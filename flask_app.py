from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

docbot = ChatBot('Bot',
                 storage_adapter='chatterbot.storage.SQLStorageAdapter',
                 logic_adapters=[
                     {
                         'import_path': 'chatterbot.logic.BestMatch'
                     },

                 ],
                 trainer='chatterbot.trainers.ListTrainer')
docbot.set_trainer(ListTrainer)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')  #user query
    response = str(docbot.get_response(userText)) #bot response

    return response


if __name__ == '__main__':
    app.run(debug=True)
