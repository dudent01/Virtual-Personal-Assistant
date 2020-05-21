import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
#import urllib2
import json
from bs4 import BeautifulSoup as soup
#from urllib2 import urlopen
import wikipedia
import random
from time import strftime

from gtts import gTTS

def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command

# Used method from Geeks-4-Geeks because the method from Towards Data Science only works for Mac
num = 1
def sofiaResponse(output):
    global num

    # Global value is updated to ensure that all unique files are named uniquely
    num += 1
    print("Assistant: " + output)

    ''' Could be further improved to allow slow speech if prompted to repeat'''
    toSpeak = gTTS(text=output, lang='en', slow=False)

    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file. Then remove the file.
    playsound.playsound(file, True)
    os.remove(file)

sofiaResponse(myCommand())