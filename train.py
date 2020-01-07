from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

try:
	os.remove("db.sqlite3")  #saving in db
	print("Old db removed. Training new database")
except:
	print('No database found. Creating new database.')

docbot = ChatBot('Bot')
docbot.set_trainer(ListTrainer)
for file in os.listdir('data'): #reading all the yml data
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        docbot.train(convData) #training
        print("Training completed for "+file)
    

