import pyttsx3
from gtts import gTTS

#this possion selects the driver to use on conversion from text to speech
engine = pyttsx3.init(driverName='sapi5')


# get the voice parameter
sound = engine.getProperty('voices')

# print the current voice parameter
print(sound)

# get the rate parameter
rate = engine.getProperty('rate')

# print the current rate parameter
print(rate)

# get the volume parameter
volume = engine.getProperty('volume')

# print the current volume parameters
print(volume)

# change the default parameters to your requirements
engine.setProperty("voice",sound[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 2.0)


# open a text file you saved your text
f = open("code.txt", "r")

# select the language of choice for list of language
# visit the pyttsx3 documentation
language = 'en'

# assign the text in a file to a variable
msg = f.read()

# save the audio in mp3 format
engine.save_to_file(msg, "output.mp3")

# terminate the programe immediately when done translating
engine.runAndWait()







