# chatbot

##reference
https://learnpython.com/blog/ai-chatbot-in-python/

##create python virtual env
python3 -m venv chatbot_env
source chatbot_env/bin/activate

##install required libraries
pip install chatterbot chatterbot_corpus nltk

##install spacy
pip install -U spacy
python -m spacy download en_core_web_sm

##install pyyaml
pip install pyyaml

##run the program
python3 chatbot.py

