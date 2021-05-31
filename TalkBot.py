# Import all the libraries
import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create the bot
myBot = ChatBot('MyBot')

# Create object for speech recognition
r1 = sr.Recognizer()
r2 = sr.Recognizer()

# Set the trainer
myBot.set_trainer(ChatterBotCorpusTrainer)

# Train the bot
myBot.train('chatterbot.corpus.english')

# Initialize python text to speech converter
friend = pyttsx3.init()

# An infinite loop to take the voice input from the user
while True:
    with sr.Microphone() as source:
        print('Listening')
        try:
            audio = r1.listen(source)                   # Record the audio data
            # my_input = r2.recognize_sphinx(audio)     # Recognise the audio input
            my_input = r1.recognize_google(audio)       # Recognise the voice
        except:
            my_input = 'hi'
            # print('You: ', my_input)
        print('You: ', my_input)
        if my_input == 'bye':                  # If input is bye, then quit
            break

        reply = myBot.get_response(my_input)    # Response by the model
        print('Bot: ', reply)
        friend.say(reply)                       # Response said by the bot
        friend.runAndWait()
