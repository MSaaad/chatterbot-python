from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

filenumber = int(os.listdir('saved_conversations')[-1])
filenumber = filenumber + 1
file = open('saved_conversations/'+str(filenumber), "w+")
file.close()

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
    userText = request.args.get('msg')
    response = str(docbot.get_response(userText))

    appendfile = os.listdir('saved_conversations')[-1]
    appendfile = open('saved_conversations/'+str(filenumber), "a")
    appendfile.write('user : '+userText+'\n')
    appendfile.write('bot : '+response+'\n')
    appendfile.close()

    return response


if __name__ == '__main__':
    app.run(debug=True)
