from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
nlp = spacy.load('en_core_web_sm')
import nltk
from nltk.chat.util import Chat, reflections

# Initialize chatbot
chatbot = ChatBot("AI Assistant")
trainer = ChatterBotCorpusTrainer(chatbot)
 
# Train chatbot with English dataset
trainer.train("chatterbot.corpus.english")

# Define chatbot responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"what is your name?", ["I am a chatbot, created to assist you!"]],
    [r"are you pretty?", ["I am cute!"]]
]
 
chatbot = Chat(pairs, reflections)
while True:
    user_input = input("You: ")
    print("Chatbot:", chatbot.respond(user_input))

 
# Chat loop
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("AI Assistant:", response)
