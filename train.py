from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

docbot = ChatBot('Bot')
docbot.set_trainer(ListTrainer)
for file in os.listdir('data'):
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        docbot.train(convData)
        print("Training completed for "+file)
    
