import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver

num = 1
def assistant_speaks(output):
    global num

    # Global value is updated to ensure that all unique files are named uniquely
    num += 1
    print("Person: " + output)

    ''' Could be further improved to allow slow speech if prompted to repeat'''
    toSpeak = gTTS(text=output, lang='en', slow=False)

    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file. Then remove the file.
    playsound.playsound(file, True)
    os.remove(file)



def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        ''' Could be further improved by making the phrase_time_limit depend on duration of speech '''
        audio = rObject.listen(source, phrase_time_limit=10)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:

        assistant_speaks("Could not understand your audio, PLease try again !")
        return 0
